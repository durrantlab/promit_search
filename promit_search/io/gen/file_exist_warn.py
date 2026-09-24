
""" Determines if a file exists """

from pathlib import Path
from loguru import logger

from .file_verify import file_verify

def file_exist_warn(file_path: Path, warn_mess: str = "") -> bool:
    """Determines if file already exists, and
    raises a warning if it does

    Args:
        file_path: path of file being checked
        warn_mess: additional message adding to warning

    Returns:
        If the file exists or not
    """
    try:
        file_verify(file_path)
        logger.warning(f"File already exists {file_path}. {warn_mess}")
        return True
    except:
        return False

