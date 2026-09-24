
""" Determines if a directory exists and returns if does or not"""

from pathlib import Path
from loguru import logger

from .dir_create import dir_create

def dir_verify(dir_path: Path, create: bool = False) -> bool:
    """Determines if the dir exists or not. Can create it

    Args:
        dir_path: path of dir being checked
        create: if the directory is created if it is not present
    
    Returns:
        If the dir exists or not. If it was just created, still True.

    Raise:
        FileNotFound: if directory passed does not exist, and not
            set to create it
        Exception: if tried to create directory and could not
    """
    present: bool = dir_path.is_dir()
    if present:
        return True 
    else:
        if create:
            dir_create(dir_path)
            return True
        else:
            message = f"{dir_path} directory does not exist"
            logger.error(message)
            raise FileNotFoundError(message)

