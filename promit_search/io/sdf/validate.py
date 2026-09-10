from pathlib import Path
import warnings

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

    Raises:
        Exception: if a molecule in SDF is invalid

    Returns:
        all molecules in file
    """
    
    
    # validate SDF and get rdkit molecule(s)
    supplier = create_rdkit(sdf_file)

    for mol in supplier:
        if mol == None:
            raise Exception("Invalid molecule in SDF")

    return supplier
