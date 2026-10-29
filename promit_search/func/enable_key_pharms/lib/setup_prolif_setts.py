from pathlib import Path 
import prolif as plf


def setup_prolif_setts(input_setts: dict) -> dict:
    """Will take in list of prolif settings to edit the defaults,
    then return the complete settings list

    Args:
        input_setts: list of settings to change

    Returns:
        default settings with new settings added on top
    """
    def_settings: dict = {
        "vicinity_cutoff": 10,
        "interactions": [
            "Hydrophobic",
            "HBDonor",
            "HBAcceptor",
            "PiStacking",
            "Anionic",
            "Cationic",
            "CationPi",
            "PiCation",
        ],
        "parameters": {
                "Hydrophobic": {"distance": 5},
                "HBDonor": {"distance": 4.0},
                "HBAcceptor": {"distance": 4.0},
                "Anionic": {"distance": 8},
                "Cationic": {"distance": 8},
                "PiStacking": {
                    "ftf_kwargs": {"distance": 8},
                    "etf_kwargs": {"distance": 8},
                },
            }
    }
    merged: dict = dict(def_settings)
    merged: dict = dict_merge(merged, input_setts)
    return merged


def dict_merge(merged: dict, new: dict) -> dict:
    """Will take in a dictionary, and add in / overwrite all
    values from the new dictionary into it. Recursive

    Args:
        merged: the dictionary being added to
        new: dictionary taking from

    Returns:
        dictionary with new added on top of merge
    """
    for key, value in new.items():
        if isinstance(merged.get(key), dict) and isinstance(value, dict):
            merged[key] = dict_merge(merged[key], value)
        else:
            merged[key] = value
    return merged