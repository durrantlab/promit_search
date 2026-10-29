
from pathlib import Path
import os
import warnings

with warnings.catch_warnings(record=True):
    import prolif as plf
    from rdkit import Chem

from promit_search.func.enable_key_pharms.lib.setup_prolif_setts import setup_prolif_setts
from promit_search.func.enable_key_pharms.lib.find_interactions import find_interactions

from display_interaction import write_interaction_pymol_script

LOCAL_DIR = Path(os.path.dirname(__file__))
INPUT_DIR = (LOCAL_DIR / ".." /  ".." / "tests" / "input").resolve()
PROT_FILE: Path = (INPUT_DIR / "prot.pdb").resolve()
SDF_DIR: Path = (INPUT_DIR / "find_pharms_op").resolve()

def test():
    rdkit_prot = Chem.MolFromPDBFile(str(PROT_FILE), removeHs=False)
    protein_mol = plf.Molecule(rdkit_prot)
    prolif_settings = setup_prolif_setts({})  
    result = find_interactions((SDF_DIR / "mole5.sdf"), 
        protein_mol, prolif_settings)
    print(result)

    write_interaction_pymol_script(result, (SDF_DIR / "mole5.sdf"), PROT_FILE, 
        (LOCAL_DIR / "output" / "test.pml"), 7)





if __name__ == "__main__":
    test()