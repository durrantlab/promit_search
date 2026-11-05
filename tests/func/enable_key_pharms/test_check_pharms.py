
""" Status: working on it """

import pytest
from pathlib import Path
import os
from rdkit import Chem

from promit_search.func.enable_key_pharms.lib.check_pharms.get_valid_pharms import get_valid_pharms

LOCAL_DIR = Path(os.path.dirname(__file__))

def test_get_valid_pharms1(file1, find_pharms_op):
    # check it returns all false if there are no interactions found
    supplier = Chem.SDMolSupplier(
        str(find_pharms_op / "mole5.sdf"), sanitize=True, removeHs=False, strictParsing=True
    )
    result = get_valid_pharms({}, supplier[0], {})
    for bl in result:
        assert(not bl)

