
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
        mess = f"File does not exist {file_path}"
        logger.error(mess)
        raise FileNotFoundError(mess)
    else:
        return True
