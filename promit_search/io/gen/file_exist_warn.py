
""" Determines if a file exists """

from pathlib import Path
from loguru import logger

from .file_verify import file_verify

def file_exist_warn(file_path: Path, warn_mess: str = "") -> bool:
    """Determines if file already exists, and
    raises a warning if it does. If it is a directory, will crash

    Args:
        file_path: path of file being checked
        warn_mess: additional message adding to warning
    
    Warning:
        If passed in file is a directory

    Returns:
        If the file exists or not
    """
    if file_path.is_dir():
        raise Exception("File is a directory. {}".format(file_path))
    try:
        file_verify(file_path)
        logger.warning("File already exists {}. {}".format(file_path, warn_mess))
        return True
    except:
        return False

