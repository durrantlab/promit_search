
from pathlib import Path
import os
import warnings

with warnings.catch_warnings(record=True):
    import prolif as plf
    from rdkit import Chem

from promit_search.func.enable_key_pharms.lib.setup_prolif_setts import setup_prolif_setts
from promit_search.func.enable_key_pharms.lib.find_interactions import find_interactions

LOCAL_DIR = Path(os.path.dirname(__file__))
INPUT_DIR = (LOCAL_DIR / ".." /  ".." / "tests" / "input").resolve()
PROT_FILE: Path = (INPUT_DIR / "prot.pdb").resolve()

def test():
    rdkit_prot = Chem.MolFromPDBFile(str(PROT_FILE), removeHs=False)
    protein_mol = plf.Molecule(rdkit_prot)
    prolif_settings = setup_prolif_setts({})  
    result = find_interactions((INPUT_DIR / "mole5.sdf"), 
        protein_mol, prolif_settings)
    print(result)

if __name__ == "__main__":
    test()