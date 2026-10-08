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
    settings: dict = def_settings | input_setts
    return settings