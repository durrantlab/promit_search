
""" sets up pharmit pharmacophore generation to be run on slurm """

from pathlib import Path
import warnings
from loguru import logger

with warnings.catch_warnings(record=True):
    from rdkit import Chem

warnings.filterwarnings("ignore", category=DeprecationWarning)
warnings.filterwarnings("ignore", category=UserWarning)

from promit_search.io import slurm
from promit_search.io import sdf
from promit_search.io import gen

def pharm_slurm(molecules: Chem.Mol, output_dir: Path,
                slurm_path: Path | None = None):
    """Will print all RDKIT molecules as seperate SDF files,
    will then create slurm batch script to run it async later.

    Places all files into output_dir by default. Overwrites files
    with same name if they already exist.

    Args:
        molecules: RDKIT molecules the pharmacophores are being found for
        output_dir: path where SDFs, slurm script, and Pharmacophore JSONs
        slurm_path: Where slurm will be placed. Defaults to output_dir.
    """
    body: list[str] = []
    # go through each molecule. Make SDF, and add to slurm script.
    for mol in molecules:
        mol_name: str = mol.GetProp("_Name")
        output_file: Path = output_dir / f"{mol_name}.json"
        sdf_inp: Path = output_dir / f"{mol_name}.sdf"
        logger.info(f"Adding {mol_name} to slurm")
        sdf.write_from_rdkit(mol, sdf_inp)
        body.append(f"pixi run pharmit pharma -in {str(sdf_inp)} -out {output_file}")
    # setup batch
    if slurm_path == None:
        slurm_path: Path = output_dir / "make_pharms.slurm"
    slurm.create_single(body, slurm_path)

        
