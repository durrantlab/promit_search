
""" writes a list of lists to a csv """

from pathlib import Path 


def write_list(lst: list[list[str]], csv_path: Path):
    """Takes in a list and writes it. Each 2D index
    seperated by , each 1D index seperated by new line

    Args:
        lst: 2D list of strings
        csv_path: where csv will be printed
    """

    with open(csv_path, "w") as f:
        f.write("\n".join([",".join(item) for item in lst]))