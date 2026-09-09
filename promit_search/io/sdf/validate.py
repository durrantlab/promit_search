from pathlib import Path
import warnings

with warnings.catch_warnings(record=True):
    from rdkit import Chem

warnings.filterwarnings("ignore", category=DeprecationWarning)
warnings.filterwarnings("ignore", category=UserWarning)



def validate(sdf_file: Path) -> Chem.SDMolSupplier:
    
    
    # validate SDF and get rdkit molecule(s)
    supplier = Chem.SDMolSupplier(
        str(sdf_file), sanitize=True, removeHs=False, strictParsing=True
    )

    return (supplier)
