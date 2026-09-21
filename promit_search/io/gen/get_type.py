
from pathlib import Path
from loguru import logger

def get_type(file: Path) -> str | None:
    """Returns the type of the file

    Args:
        file (Path): file being checked

    Returns:
        the type of the file, and if it has
        no suffix it returns None
    """
    try:
        ending: str = file.suffix
        if ending.startswith("."):
            return file.suffix[1:]
        else:
            return None
    except:
        mess: str = f"The file {file} is not found"
        logger.error(mess)
        raise FileNotFoundError(mess)