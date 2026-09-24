
""" Create an rdkit molecule list from a sdf file """

from pathlib import Path
import warnings
from loguru import logger

with warnings.catch_warnings(record=True):
    from rdkit import Chem

warnings.filterwarnings("ignore", category=DeprecationWarning)
warnings.filterwarnings("ignore", category=UserWarning)



def create_rdkit(sdf_file: Path) -> Chem.SDMolSupplier:
    """Takes in an SDF file, creates an RDKIT molecule.
    Assumes file's existance is already validated.

    Args:
        sdf_file: SDF with molecules

    Returns:
        all molecules in file as rdkit supploer
    
    Raises:
        Exception: if sdf is invalid somehow
    
    Warns:
        Warning: if the SDF file already exists
    """
    # validate SDF and get rdkit molecule(s)
    logger.info(f"Reading in {sdf_file}")
    supplier = Chem.SDMolSupplier(
        str(sdf_file), sanitize=True, removeHs=False, strictParsing=True
    )
    # check through
    if len(supplier) == 0:
        mess = f"SDF file is empty {sdf_file}"
        logger.error(mess)
        raise Exception(mess)
    for mol in supplier:
        if mol == None:
            mess = f"SDF file has invalid molecule {sdf_file}"
            logger.error(mess)
            raise Exception(mess)

    return supplier
