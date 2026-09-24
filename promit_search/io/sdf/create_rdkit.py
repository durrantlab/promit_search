
""" Create an rdkit molecule list from a sdf file """

from pathlib import Path
import warnings

with warnings.catch_warnings(record=True):
    from rdkit import Chem

warnings.filterwarnings("ignore", category=DeprecationWarning)
warnings.filterwarnings("ignore", category=UserWarning)



def create_rdkit(sdf_file: Path) -> Chem.SDMolSupplier:
    """Takes in an SDF file, creates an RDKIT molecule

    Args:
        sdf_file: SDF with molecules

    Returns:
        all molecules in file
    """
    # validate SDF and get rdkit molecule(s)
    supplier = Chem.SDMolSupplier(
        str(sdf_file), sanitize=True, removeHs=False, strictParsing=True
    )
    return supplier
