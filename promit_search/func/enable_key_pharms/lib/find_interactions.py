from pathlib import Path 
import prolif as plf

def find_interactions(sdf_file: Path, protein_mol: plf.Molecule, prolif_settings: dict) -> dict[str, list[int]]:
    """Will find all interactions between the molecule and protein using prolif. Will return
    as a dictionary of all interactions, with the values being each atom involved in an interaction
    of that type

    Args:
        sdf_file: sdf that holds molecule being checked
        protein_mol: prolif molecule version of protein docked to
        prolif_settings: settings to change how prolif works

    Returns:
        dictionary that matches each interaction type to the atoms involved in that interaction
    """

    pose_iterable = plf.sdf_supplier(str(sdf_file))
    fp = plf.Fingerprint(**prolif_settings)
    fp.run_from_iterable(pose_iterable, protein_mol)

    lig_inter_list: dict[str, list[int]] = {}
    """D1: each interaction D2: list of atoms interacting"""
    for mol_indx in range(len(pose_iterable)):  # go through every molecule
        for (lig_res, prot_res), interactions in fp.ifp[
            mol_indx
        ].items():  # go through every interaction for this one
            for int_name, metadata_list in interactions.items(): # go through each interaction type
                if not int_name in lig_inter_list.keys():
                    lig_inter_list[int_name] = []
                for md in metadata_list:
                    lig_atoms: tuple[int] = md["parent_indices"]["ligand"]
                    for lig_atom_ in lig_atoms:
                        lig_atom = lig_atom_ + 1
                        if not lig_atom in lig_inter_list[int_name]:
                            lig_inter_list[int_name].append(lig_atom)

    return lig_inter_list