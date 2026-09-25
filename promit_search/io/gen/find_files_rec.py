
""" finds files with a list of endings in a directory recursively """

from pathlib import Path
from loguru import logger

from .dir_verify import dir_verify

def find_files_rec(dir: Path, valid_types: list[str] = [],
                   empty_error: bool = False) -> list[Path]:
    """Will recursively check through directory to find all files of 
    a certain type.

    Will crash if directory is invalid

    Args:
        dir: the directory checked
        valid_files: all valid file endings. If not include, will grab all files
            Will always skip directories
        empty_error: if an erorr should be thrown if there are no found files
    
    Returns:
        List of paths of all the files of correct type(s)
    
    Raise:
        Exception: if empty_error is True, raises error if no valid files found
        FileNotFound: if directory passed does not exist, and not set to create it
    """
    # check directory valid
    logger.info(f"Searching for files in {dir}")
    dir_verify(dir)

    # normalize: guarantee a leading dot, lowercase for case-insensitive matching
    valid = [s.lower() if s.startswith(".") else f".{s.lower()}" for s in valid_types]
    items = dir.rglob("*")
    if len(valid) > 0:
        files: list[Path] = sorted(p for p in items if p.is_file() and p.suffix.lower() in valid)
    else:
        files: list[Path] = sorted(p for p in items if p.is_file())

    # raise error if invalid file
    if empty_error and len(files) == 0:
        mess = f"No files with valid ending file found in {dir}"
        logger.error(mess)
        raise Exception(mess)
    
    return files