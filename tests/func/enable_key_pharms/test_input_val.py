
""" Status: working on it """

import pytest
from pathlib import Path
import os

from promit_search.func.enable_key_pharms.lib.get_validate_recursive import get_validate_recursive
from promit_search.io import sdf
from promit_search.io import json

LOCAL_DIR = Path(os.path.dirname(__file__))

def test_get_validate_recursive1():
    # quickly check that validate recursive actually works
    files_list = get_validate_recursive((LOCAL_DIR / "input"), "sdf", sdf.validate)
    assert(len(files_list) == 8)

    for num in range(1, 9):
        assert (f"mole{num}.sdf" in [item.name for item in files_list])

def test_get_validate_recursive2():
    # quickly check that validate recursive actually works
    files_list = get_validate_recursive((LOCAL_DIR / "input"), "json", json.validate)
    assert(len(files_list) == 8)

    for num in range(1, 9):
        assert (f"mole{num}.json" in [item.name for item in files_list])