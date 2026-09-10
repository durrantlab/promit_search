
from pathlib import Path


def dir_verify(dir_path: Path) -> bool:
    """Determines if the dir exists or not

    Args:
        dir_path: path of dir being checked

    Returns:
        If the dir exists or not
    """
    return dir_path.is_dir()
