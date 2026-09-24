
""" writes a csv to a list of lists """

from pathlib import Path 


def read_list(file_path: Path) -> list[list[str]]:
    """Takes in a csv file path and reads it in

    Args:
        file_path: location of csv

    Returns:
        the csv contents as a list of lists
    """

    with open(file_path, "r") as f:
        ret: list[list[str]] = [item.split(",") for item in f.read().split("\n")]
    return ret