
""" Status: working on it """

import pytest
from pathlib import Path
import os
import warnings

with warnings.catch_warnings(record=True):
    import prolif as plf
    from rdkit import Chem

from promit_search.func.enable_key_pharms.lib.setup_prolif_setts import setup_prolif_setts
from promit_search.func.enable_key_pharms.lib.find_interactions import find_interactions

LOCAL_DIR = Path(os.path.dirname(__file__))

def test_find_inter1(protein_file):
    # this just makes sure that the output is of the right format
    protein_file: Path = Path(protein_file).resolve()
    rdkit_prot = Chem.MolFromPDBFile(str(protein_file), removeHs=False)
    protein_mol = plf.Molecule(rdkit_prot)
    prolif_settings = setup_prolif_setts({})
    result = find_interactions((LOCAL_DIR / "input" / "mole5.sdf"), 
        protein_mol, prolif_settings)
    assert(len(result) > 1)
    for value in result.values():
        assert(len(value) > 0)
