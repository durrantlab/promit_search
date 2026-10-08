
import json
from pathlib import Path


def write_concat(objects: list[dict], path: Path, indent: int =2) -> None:
    """Takes in a list of dictionaries and writes them as a
    concatened json

    Args:
        objects: list of dictionaries written as json
        path: where they are placed
        indent: size of indent for json. Defaults to 2.
    """
    with open(path, "w") as f:
        for i, obj in enumerate(objects):
            if i:
                f.write("\n")
            json.dump(obj, f, indent=indent)