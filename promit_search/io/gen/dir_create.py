
""" Creates a dir path if it doesnt exist """

from pathlib import Path
from loguru import logger

def dir_create(dir_path: Path) -> bool:
    """Determines if the dir exists or not.
    If it does not, creates it

    Args:
        dir_path: path of dir being checked

    Returns:
        If the dir existed or not
    
    Raise:
        Exception: if could not create directory
    """
    if_dir: bool = dir_path.is_dir()
    try:
        if not if_dir:
            logger.info(f"Creating directory at {dir_path}")
            dir_path.mkdir(parents=True, exist_ok=True)
    except: 
        mess = f"Could not create directory {dir_path}"
        logger.error(mess)
        raise Exception(mess)
    return if_dir
