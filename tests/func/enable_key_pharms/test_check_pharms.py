
""" Status: working on it """

import pytest
from pathlib import Path
import os
from rdkit import Chem
from promit_search.io import json as pms_json

from promit_search.func.enable_key_pharms.lib.check_pharms.get_valid_pharms import get_valid_pharms

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
        assert(not bl)
