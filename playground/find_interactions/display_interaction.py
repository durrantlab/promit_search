from collections import defaultdict
from pathlib import Path

from loguru import logger

# interaction type (lowercase) -> PyMOL color
INTERACTION_COLORS: dict[str, str] = {
    "hydrophobic": "green",
    "hbdonor": "white",
    "hbacceptor": "yellow",
    "pistacking": "purple",
    "cationic": "blue",
    "anionic": "red",
}
MULTI_INTERACTION_COLOR = "cyan"
LIGAND_COLOR = "gray"


def _atom_selection(obj: str, indices: list[int]) -> str:
    """PyMOL selection for 0-based atom indices of an object.

    PyMOL's `rank` is the 0-based atom order in the loaded file, which matches
    RDKit/ProLIF indices when the SDF was read with removeHs=False.
    """
    ranks = " or id ".join(f"rank {i}" for i in sorted(indices))
    return f"{obj} and id ({ranks})"


def write_interaction_pymol_script(
    interactions: dict[str, list[int]],
    sdf_file: Path,
    pdb_file: Path,
    output_pml: Path,
    cutoff: float = 8.0,
) -> Path:
    """Writes a PyMOL script that shows a ligand's interacting atoms by color.

    The ligand is shown as gray sticks. Each atom involved in an interaction is
    colored by interaction type, and atoms involved in more than one type are
    colored cyan. Protein residues with any atom within `cutoff` angstroms of
    the ligand are shown as sticks; the rest of the protein is a cartoon.

    Args:
        interactions: interaction type -> list of 0-based ligand atom indices
        sdf_file: SDF holding the ligand (first molecule is used)
        pdb_file: PDB of the protein
        output_pml: where to write the PyMOL script
        cutoff: distance in angstroms defining the active site

    Warns:
        If an interaction type has no assigned color, it is skipped

    Returns:
        Path to the written PyMOL script
    """
    # collect every interaction type each ligand atom takes part in
    atom_types: dict[int, set[str]] = defaultdict(set)
    for int_type, atoms in interactions.items():
        if int_type.lower() not in INTERACTION_COLORS:
            logger.warning(f"No color assigned for interaction '{int_type}', skipping")
            continue
        for atom in atoms:
            atom_types[int(atom)].add(int_type.lower())

    # group atoms by their final color
    atoms_by_color: dict[str, list[int]] = defaultdict(list)
    for atom, types in atom_types.items():
        if len(types) > 1:
            color = MULTI_INTERACTION_COLOR
        else:
            color = INTERACTION_COLORS[next(iter(types))]
        atoms_by_color[color].append(atom)

    protein_path = Path(pdb_file).resolve().as_posix()
    ligand_path = Path(sdf_file).resolve().as_posix()

    lines = [
        f'load "{protein_path}", protein',
        f'load "{ligand_path}", ligand',
        "hide everything",
        "show cartoon, protein",
        "color gray80, protein",
        # active site: whole residues with any atom within the cutoff of the ligand
        f"select active_site, byres (protein within {cutoff} of ligand)",
        "show sticks, active_site",
        "util.cbao active_site",  # orange carbons, so they don't clash with green
        "hide sticks, active_site and hydro and (neighbor elem C)",  # nonpolar H
        "show sticks, ligand",
        f"color {LIGAND_COLOR}, ligand",
    ]

    for color, atoms in sorted(atoms_by_color.items()):
        sel_name = f"inter_{color}"
        lines.append(f"select {sel_name}, {_atom_selection('ligand', atoms)}")
        lines.append(f"color {color}, {sel_name}")
        lines.append(f"show spheres, {sel_name}")

    lines += [
        "set sphere_scale, 0.25",
        "deselect",
        "orient ligand",
        "zoom active_site, 2",
    ]

    output_pml = Path(output_pml)
    output_pml.parent.mkdir(parents=True, exist_ok=True)
    output_pml.write_text("\n".join(lines) + "\n")
    return output_pml