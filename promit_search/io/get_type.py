
from pathlib import Path

def get_type(file: Path) -> str:
    """Returns the type of the file

    Args:
        file (Path): file being checked

    Returns:
        str: the type of the file
    """

    return file.suffix[1:]