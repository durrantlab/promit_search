
from pathlib import Path
import warnings

with warnings.catch_warnings(record=True):
    from rdkit import Chem

warnings.filterwarnings("ignore", category=DeprecationWarning)
warnings.filterwarnings("ignore", category=UserWarning)



def make_pharms(file_path: Path, molecules: Chem.Mol, output_dir: Path):


    # get name of molecule
    # create output file name
    # run pharmacophore creation
