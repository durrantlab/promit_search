
""" Creates a dir path if it doesnt exist """

from pathlib import Path

def dir_create(dir_path: Path) -> bool:
    """Determines if the dir exists or not.
    If it does not, creates it

    Args:
        dir_path: path of dir being checked

    Returns:
        If the dir existed or not
    """
    if_dir: bool = dir_path.is_dir()
    if not if_dir:
        dir_path.mkdir(parents=True, exist_ok=True)
    return if_dir
