
""" Checks that a SDF file is valid """

from pathlib import Path
import warnings
from loguru import logger

with warnings.catch_warnings(record=True):
    from rdkit import Chem

warnings.filterwarnings("ignore", category=DeprecationWarning)
warnings.filterwarnings("ignore", category=UserWarning)


from .create_rdkit import create_rdkit


def validate(sdf_file: Path) -> Chem.SDMolSupplier:
    """Takes in an SDF file, creates an RDKIT molecule
    then checks that all are valid

    Args:
        sdf_file: SDF with molecules

    Returns:
        all molecules in file

    Raises:
        Exception: if a molecule in SDF is invalid
    """
    
    
    # validate SDF and get rdkit molecule(s)
    supplier = create_rdkit(sdf_file)

    for mol in supplier:
        if mol == None:
            mess = f"Invalid molecule in SDF {sdf_file}"
            logger.info(mess)
            raise Exception(mess)

    return supplier
