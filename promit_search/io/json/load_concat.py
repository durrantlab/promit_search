
from pathlib import Path
import json

def load_concat(path: Path) -> list[dict]:
    """Will take in a concatanated JSON file (basically multiple JSONs in one)
    and return a list of JSON objects for each one

    Args:
        path: location of json

    Returns:
        list of the jsons in the file
    """
    with open(path) as f:
        text = f.read()

    decoder = json.JSONDecoder()
    objects = []
    idx = 0
    n = len(text)
    while idx < n:
        while idx < n and text[idx].isspace():
            idx += 1
        if idx >= n:
            break
        obj, end = decoder.raw_decode(text, idx)
        objects.append(obj)
        idx = end
    return objects