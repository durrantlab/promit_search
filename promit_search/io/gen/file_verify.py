
from pathlib import Path


def file_verify(file_path: Path) -> bool:
    """Determines if the file exists or not

    Args:
        file_path: path of file being checked

    Returns:
        If the file exists or not
    """
    return file_path.is_file()
