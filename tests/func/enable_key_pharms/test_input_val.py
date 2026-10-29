
""" Status: working on it """

import pytest
from pathlib import Path
import os

from promit_search.func.enable_key_pharms.lib.get_validate_recursive import get_validate_recursive
from promit_search.func.enable_key_pharms.lib.match_sdf_json import match_sdf_json
from promit_search.func.enable_key_pharms.lib.get_op_path import get_op_path

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

def test_get_op_path():
    # file sat directly in the parent keeps its name
    op_dir = LOCAL_DIR / "output"
    input_parent = LOCAL_DIR / "input"
    input_path = input_parent / "rec.sdf"
    expected = (op_dir / "rec.sdf").resolve()
    assert(get_op_path(op_dir, input_parent, input_path, False) == expected)
 
 
def test_get_op_path2():
    # directory structure is replicated under op_dir
    op_dir = LOCAL_DIR / "output"
    input_parent = LOCAL_DIR / "input"
    input_path = input_parent / "rec_test" / "rec.sdf"
    expected = (op_dir / "rec_test" / "rec.sdf").resolve()
    assert(get_op_path(op_dir, input_parent, input_path, False) == expected)
 
 
def test_get_op_path3():
    # several levels deep is replicated too
    op_dir = LOCAL_DIR / "output"
    input_parent = LOCAL_DIR / "input"
    input_path = input_parent / "a" / "b" / "c" / "rec.sdf"
    expected = (op_dir / "a" / "b" / "c" / "rec.sdf").resolve()
    assert(get_op_path(op_dir, input_parent, input_path, False) == expected)
 
 
def test_get_op_path4():
    # a directory is handled the same as a file
    op_dir = LOCAL_DIR / "output"
    input_parent = LOCAL_DIR / "input"
    input_path = input_parent / "rec_test"
    expected = (op_dir / "rec_test").resolve()
    assert(get_op_path(op_dir, input_parent, input_path, False) == expected)
 
 
def test_get_op_path5():
    # the parent itself maps onto op_dir
    op_dir = LOCAL_DIR / "output"
    input_parent = LOCAL_DIR / "input"
    result = get_op_path(op_dir, input_parent, input_parent, False)
    assert(result == op_dir.resolve())
 
 
def test_get_op_path6():
    # flatten drops the structure and puts the file in the root
    op_dir = LOCAL_DIR / "output"
    input_parent = LOCAL_DIR / "input"
    input_path = input_parent / "rec_test" / "rec.sdf"
    expected = (op_dir / "rec.sdf").resolve()
    assert(get_op_path(op_dir, input_parent, input_path, True) == expected)
 
 
def test_get_op_path7():
    # flatten ignores the parent entirely
    op_dir = LOCAL_DIR / "output"
    input_path = LOCAL_DIR / "input" / "rec.sdf"
    expected = (op_dir / "rec.sdf").resolve()
    result = get_op_path(op_dir, LOCAL_DIR / "unrelated", input_path, True)
    assert(result == expected)
 
 
def test_get_op_path8():
    # same file name in two folders collides once flattened
    op_dir = LOCAL_DIR / "output"
    input_parent = LOCAL_DIR / "input"
    path1 = input_parent / "rec.sdf"
    path2 = input_parent / "rec_test" / "rec.sdf"
    result1 = get_op_path(op_dir, input_parent, path1, True)
    result2 = get_op_path(op_dir, input_parent, path2, True)
    assert(result1 == result2)
 
 
def test_get_op_path9():
    # input outside the parent cannot be made relative
    op_dir = LOCAL_DIR / "output"
    input_parent = LOCAL_DIR / "input"
    input_path = LOCAL_DIR / "unrelated" / "rec.sdf"
    with pytest.raises(ValueError):
        get_op_path(op_dir, input_parent, input_path, False)
 
 
def test_get_op_path10():
    # the parent being below the input is not the same as the reverse
    op_dir = LOCAL_DIR / "output"
    input_parent = LOCAL_DIR / "input" / "rec_test"
    input_path = LOCAL_DIR / "input"
    with pytest.raises(ValueError):
        get_op_path(op_dir, input_parent, input_path, False)
 
 
def test_get_op_path11():
    # relative paths come back absolute
    result = get_op_path(Path("output"), Path("input"), Path("input/rec.sdf"), False)
    assert(result.is_absolute())
    assert(result == (Path("output") / "rec.sdf").resolve())
    result = get_op_path(Path("output"), Path("input"), Path("input/rec.sdf"), True)
    assert(result.is_absolute())
 
 
def test_get_op_path12():
    # a Path is returned, not a string
    op_dir = LOCAL_DIR / "output"
    input_parent = LOCAL_DIR / "input"
    input_path = input_parent / "rec.sdf"
    assert(isinstance(get_op_path(op_dir, input_parent, input_path, False), Path))