from pathlib import Path 
import json


def write(dictionary: dict, path: Path) -> None:
    """Takes in a dictionary and writes as a json

    Args:
        dictionary: dictionary to be written
        path: location of json
    """
    with open(path, "w") as f:
        json.dump(dictionary, f, indent=2)