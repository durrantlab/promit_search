
PHARMACOPHORE_TO_PROLIF: dict[str,str] = {
    "Hydrophobic": "Hydrophobic",
    "HydrogenDonor": "HBDonor",
    "HydrogenAcceptor": "HBAcceptor",
    "Aromatic": "PiStacking",
    "PositiveIon": "Cationic",
    "NegativeIon": "Anionic",
}

def get_valid_pharms(
    mol_pharm: dict,
    mol,
    inter_dict: dict[str, list[int]]
) -> list[bool]:
    """For a single molecule, takes in it's pharmacophore JSON and compares it to present
    interactions. If the pharmacophore is close to interacting atoms (of the same type), enable it.
    Else disable it

    Args:
        mol_pharm: list of pharmacophores for molecule
        mol: the molecule being locked at
        inter_dict: list of interacitons and the atoms involved

    Returns:
        list[bool]: list of pharmacophores for this molecule that are valid
    """
    if_pharm: list[bool] = []
    # for every pharmacophore
    for pharm in mol_pharm["points"]:
        # get data about pharmacophore
        pharm_loc = [pharm["x"], pharm["y"], pharm["z"]]
        pharm_type: str = pharm["name"]
        prolif_inter_type: str = PHARMACOPHORE_TO_PROLIF[pharm_type]

        # go through each atom interacting with that type
        if_any_inside: bool = False
        for atom in inter_dict[prolif_inter_type]:
            conf = mol.GetConformer()
            atom_pos = list(conf.GetAtomPosition(int(atom) - 1))
            # determine distance and if valid
            dist: float = _eucl_dist(atom_pos, pharm_loc)
            if_any_inside = _if_inside_pharm(dist, prolif_inter_type)
            if if_any_inside:
                break
        if if_any_inside:
            if_pharm.append(True)
        else:
            if_pharm.append(False)

    return if_pharm


def _if_inside_pharm(dist: float, inter_type: str) -> bool:
    if inter_type == "Hydrophobic" or inter_type == "Aromatic":
        if dist < 2:
            return True
    if inter_type == "HydrogenDonor" or inter_type == "HydrogenAcceptor":
        if dist < 2:
            return True
    if inter_type == "Cationic" or inter_type == "Anionic":
        if dist < 2:
            return True
    return False


def _eucl_dist(a: list[int], b: list[int]) -> int:
    return ((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2 + (a[2] - b[2]) ** 2) ** 0.5
