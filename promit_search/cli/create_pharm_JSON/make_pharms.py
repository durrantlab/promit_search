
from pathlib import Path
import warnings

with warnings.catch_warnings(record=True):
    from rdkit import Chem

warnings.filterwarnings("ignore", category=DeprecationWarning)
warnings.filterwarnings("ignore", category=UserWarning)



def make_pharms(file_path: Path, molecules: Chem.Mol, output_dir: Path, as_batch: bool = True,
                slurm_path: Path | None = None):
    for mol in molecules:
        # get name of molecule and create op
        mol_name: str = mol.GetProp("_Name")
        output_file = output_dir / f"{mol_name}.json"
        
        # run pharmacophore creation
        # if creating batch job
        if as_batch:
            pass

        
