
""" Status: working on it """

import pytest
from pathlib import Path
import os
from promit_search.io import json as pms_json
import warnings
with warnings.catch_warnings(record=True):
    import prolif as plf
    from rdkit import Chem

from promit_search.func.enable_key_pharms.lib.check_pharms.get_valid_pharms import get_valid_pharms
from promit_search.func.enable_key_pharms.lib.setup_prolif_setts import setup_prolif_setts
from promit_search.func.enable_key_pharms.lib.find_interactions import find_interactions

LOCAL_DIR = Path(os.path.dirname(__file__))

def test_get_valid_pharms1(find_pharms_op):
    # check it returns all false if there are no interactions found
    pharms: dict = pms_json.load(find_pharms_op / "mole5.json")
    supplier = Chem.SDMolSupplier(
        str(find_pharms_op / "mole5.sdf"), sanitize=True, removeHs=False, strictParsing=True
    )
    result = get_valid_pharms(pharms, supplier[0], {})
    for bl in result:
        assert(not bl)
    assert(len(result) == len(pharms["points"]))

def test_get_valid_pharms2(find_pharms_op):
    # check it returns all true if there are every interaction found
    pharms: dict = pms_json.load(find_pharms_op / "mole5.json")
    supplier = Chem.SDMolSupplier(
        str(find_pharms_op / "mole5.sdf"), sanitize=True, removeHs=False, strictParsing=True
    )
    inter_dict = {"Hydrophobic":list(range(1,37)), "PiStacking":list(range(1,37)),
        "HBDonor":list(range(1,37)), "HBAcceptor":list(range(1,37))}
    result = get_valid_pharms(pharms, supplier[0], inter_dict)
    for bl in result:
        assert(bl)
    assert(len(result) == len(pharms["points"]))

def test_get_valid_pharms3(find_pharms_op, protein_file):
    # real situation check. Make sure some on and off

    protein_file: Path = Path(protein_file).resolve()
    rdkit_prot = Chem.MolFromPDBFile(str(protein_file), removeHs=False)
    protein_mol = plf.Molecule(rdkit_prot)
    prolif_settings = setup_prolif_setts({})
    inter_dict = find_interactions((find_pharms_op / "mole5.sdf"), 
        protein_mol, prolif_settings)

    pharms: dict = pms_json.load(find_pharms_op / "mole5.json")
    supplier = Chem.SDMolSupplier(
        str(find_pharms_op / "mole5.sdf"), sanitize=True, removeHs=False, strictParsing=True
    )
    result = get_valid_pharms(pharms, supplier[0], inter_dict)
    assert(result.count(True) > 3)
    assert(result.count(False) > 3)
    assert(len(result) == len(pharms["points"]))

def test_get_valid_pharms4(find_pharms_op, protein_file):
    # check that a H-bond acceptor pharmacophore is correctly enbled
    pharms: dict = pms_json.load(find_pharms_op / "mole5.json")
    supplier = Chem.SDMolSupplier(
        str(find_pharms_op / "mole5.sdf"), sanitize=True, removeHs=False, strictParsing=True
    )
    inter_dict = {"HBAcceptor":[23]}
    result = get_valid_pharms(pharms, supplier[0], inter_dict)
    assert(result[5])
    assert(not result[6])
