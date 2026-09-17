
from pathlib import Path
import warnings

with warnings.catch_warnings(record=True):
    from rdkit import Chem

warnings.filterwarnings("ignore", category=DeprecationWarning)
warnings.filterwarnings("ignore", category=UserWarning)

from promit_search.io import slurm
from promit_search.io import sdf



def make_pharms(molecules: Chem.Mol, output_dir: Path):
    """Will print all RDKIT molecules as seperate SDF files,
    will then upload each to website, then download resulting pharmacophore
    JSON.

    Places all files into output_dir by default. Overwrites files
    with same name if they already exist.

    Args:
        molecules: RDKIT molecules the pharmacophores are being found for
        output_dir: path where SDFs, and Pharmacophore JSONs are placed
    """
