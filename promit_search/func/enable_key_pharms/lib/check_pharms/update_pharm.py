

def update_pharm(mol_pharm: dict, valid_pharms: list[bool]) -> dict:
    """Will update the the pharm JSONs so that are enabled / disabled based
    on valid pharm list

    Args:
        mol_pharm: list of all pharms for this mol
        valid_pharms: which pharms should be enabled / disabled

    Returns:
        dict: pharms now enabled / disabled correctly
    """

    for index in range(len(mol_pharm["points"])):
        if not valid_pharms[index]:
            mol_pharm["points"][index]["enabled"] = False

    return mol_pharm
