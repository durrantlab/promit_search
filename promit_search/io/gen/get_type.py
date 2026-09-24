
""" Determiens type of a file """

from pathlib import Path
from loguru import logger

def get_type(file: Path) -> str | None:
    """Returns the type of the file. Always lowercase

    Args:
        file (Path): file being checked

    Returns:
        the type of the file in lowercase, no .
        if it has no suffix it returns None
    
    Raise:
        FileNotFoundError: if file does not exist
    """
    try:
        ending: str = file.suffix
        if ending.startswith("."):
            return file.suffix[1:].lower()
        else:
            return None
    except:
        mess: str = f"The file {file} is not found"
        logger.error(mess)
        raise FileNotFoundError(mess)