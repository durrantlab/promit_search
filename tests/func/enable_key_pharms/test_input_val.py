
""" Status: working on it """

import pytest
from pathlib import Path
import os

from promit_search.func.enable_key_pharms.lib.get_validate_recursive import get_validate_recursive
from promit_search.func.enable_key_pharms.lib.match_sdf_json import match_sdf_json

from promit_search.io import sdf
from promit_search.io import json

LOCAL_DIR = Path(os.path.dirname(__file__))

def test_get_validate_recursive1():
    # quickly check that validate recursive actually works. 7 and 8 broken
    files_list = get_validate_recursive((LOCAL_DIR / "input"), "sdf", sdf.validate)
    assert(len(files_list) == 6)

    for num in range(1, 7):
        assert (f"mole{num}.sdf" in [item.name for item in files_list])

def test_get_validate_recursive2():
    # quickly check that validate recursive actually works. 6 and 8 broken.
    files_list = get_validate_recursive((LOCAL_DIR / "input"), "json", json.validate)
    assert(len(files_list) == 6)

    for num in range(1, 6):
        assert (f"mole{num}.json" in [item.name for item in files_list])

def test_match_sdf_json():
    # check that sdf and json match works
    sdf_list = get_validate_recursive((LOCAL_DIR / "input"), "sdf", sdf.validate)
    json_list = get_validate_recursive((LOCAL_DIR / "input"), "json", json.validate)
    matched = match_sdf_json(sdf_list, json_list)
    assert(len(matched) == 5)
    for key, value in matched.items():
        assert(key.stem == value.stem)