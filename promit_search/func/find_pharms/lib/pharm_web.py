
""" runs pharmit's pharmacophore generation using web api"""

from pathlib import Path
import warnings
from loguru import logger

with warnings.catch_warnings(record=True):
    from rdkit import Chem

warnings.filterwarnings("ignore", category=DeprecationWarning)
warnings.filterwarnings("ignore", category=UserWarning)

from promit_search.io import slurm
from promit_search.io import sdf
from promit_search.pharmit.web import get_pharms


def pharm_web(molecules: Chem.Mol, output_dir: Path):
    """Will print all RDKIT molecules as seperate SDF files,
    will then upload each to website, then download resulting pharmacophore
    JSON.

    Places all files into output_dir by default. Overwrites files
    with same name if they already exist.

    Args:
        molecules: RDKIT molecules the pharmacophores are being found for
        output_dir: path where SDFs, and Pharmacophore JSONs are placed
    """

    # go through each molecule. Make SDF, and send to site.
    for mol in molecules:
        mol_name: str = mol.GetProp("_Name")
        output_file: Path = output_dir / f"{mol_name}.json"
        sdf_inp: Path = output_dir / f"{mol_name}.sdf"
        sdf.write_from_rdkit(mol, sdf_inp)
        get_pharms.main(sdf_inp, output_file)
