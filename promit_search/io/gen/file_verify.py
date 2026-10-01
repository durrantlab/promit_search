
""" Determines if a file exists """

from pathlib import Path
from loguru import logger

def file_verify(file_path: Path) -> bool:
    """Determines if the file exists or not

    Args:
        file_path: path of file being checked

    Returns:
        If the file exists or not
    
    Raises:
        FileNotFoundError: if file does not exist
    """
    if not file_path.is_file():
        raise FileNotFoundError("File does not exist {}".format(file_path))
    else:
        return True
