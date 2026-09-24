
""" Check if file of file is valid"""

from pathlib import Path
from loguru import logger

from .get_type import get_type

def type_verify(file: Path, valid_types: list[str]) -> str:
    """Check if type of a file matches list

    Args:
        file: file being checked
        valid_types: the valid types

    Returns:
        the type of the file
    
    Raises:
        FileNotFoundError: if file does not exist
        Exception: if the type of file is invalid
    """
    file_type: str | None = get_type(file)
    if file_type == None or not file_type in [item.lower().removeprefix(".") for item in valid_types]:
        mess = f"Type of file is invalid {file}"
        logger.error(mess)
        raise Exception(mess)
    else:
        return file_type