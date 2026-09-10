
from pathlib import Path


def write(text: list[str] | str, output_file: Path):
    """Takes in a list of strings and writes them
    to a file. Each string is a different line

    Args:
        text: the text to be printed
        output_file: path where it is printed
    """

    with open(output_file, "w") as f:
        if isinstance(text, list):
            f.write("\n".join(text))
        else:
            f.write(text)