
from loguru import logger 
from pathlib import Path

def log_pharms(molecule_path: Path, valid_pharms: list[bool]) -> None:
    """Will give information about the number of valid pharmacophores

    Args:
        molecule_path: molecules whose pharmacophores were checked
        valid_pharms: list of if phamracophores are valid or not
    """
    bool_count = valid_pharms.count(True)
    if bool_count > 3:
        logger.info(f"Mol{molecule_path.stem} has {bool_count} pharms")
    else:
        logger.warning(f"Mol{molecule_path.stem} has {bool_count} pharms. Check manually")
