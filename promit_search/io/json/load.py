from pathlib import Path 
import json


def load(path: Path) -> dict:
    """Takes in a JSON file and returns as a dictionary

    Args:
        path: location of json

    Returns:
        dictionary version of json
    """
    with open("data.json") as f:
        data = json.load(f)
    return data