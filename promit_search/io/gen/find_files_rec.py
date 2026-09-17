
from pathlib import Path

def find_files_rec(dir: Path, valid_types: list[str] = []) -> list[Path]:
    """Will recursively check through directory to find all files of 
    a certain type.

    Will crash if directory is invalid

    Args:
        dir: the directory checked
        valid_files: all valid file endings. If not include, will grab all files
            Will always skip directories
    
    Returns:
        List of paths of all the files of correct type(s)
    """
    # check directory valid
    if not dir.is_dir():
        raise Exception(f"Directory {dir} is not a valid directory")

    # normalize: guarantee a leading dot, lowercase for case-insensitive matching
    valid = [s.lower() if s.startswith(".") else f".{s.lower()}" for s in valid_types]
    items = dir.rglob("*")
    return sorted(p for p in items if p.is_file() and p.suffix.lower() in valid)