
from pathlib import Path

from promit_search.io.gen import dir_create

def dir_verify(dir_path: Path, create: bool = False) -> bool:
    """Determines if the dir exists or not. Can create it

    Args:
        dir_path: path of dir being checked
        create: if the directory is created if it is not present

    Returns:
        If the dir exists or not. If it was just created, still True.
    """
    present: bool = dir_path.is_dir()
    if present:
        return True 
    else:
        if create:
            dir_create(dir_path)
            return True
        else:
            return False

