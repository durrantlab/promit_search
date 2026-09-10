
from pathlib import Path
import warnings

with warnings.catch_warnings(record=True):
    from rdkit import Chem

warnings.filterwarnings("ignore", category=DeprecationWarning)
warnings.filterwarnings("ignore", category=UserWarning)

from promit_search.io.slurm import create_single
from promit_search.io.sdf import write_from_rdkit


def make_pharms(molecules: Chem.Mol, output_dir: Path,
                slurm_path: Path | None = None):
    body: list[str] = []
    for mol in molecules:
        # get name of molecule and create op
        mol_name: str = mol.GetProp("_Name")
        output_file: Path = output_dir / f"{mol_name}.json"
        # create input file
        sdf_inp: Path = output_dir / f"{mol_name}.sdf"
        write_from_rdkit(mol_name, sdf_inp)
        # batch job
        body.append(f"pixi run -e pharmit pharmit pharma -in {str(sdf_inp)} -out {output_file}")
    # setup batch
    if slurm_path == None:
        slurm_path: Path = output_dir / "make_pharms.slurm"
    create_single(body, slurm_path)

        
