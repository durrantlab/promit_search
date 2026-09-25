
""" Status: working on it """

import pytest
from pathlib import Path
import os

from promit_search.io import gen

LOCAL_DIR = Path(os.path.dirname(__file__))

def test_dir_create():
    fake_dir = LOCAL_DIR / "output" / "test_dir"
    if fake_dir.is_dir():
        fake_dir.rmdir()
    assert(not gen.dir_create(fake_dir))
    assert(gen.dir_create(fake_dir))


def test_dir_verify():
    fake_dir = LOCAL_DIR / "output" / "test_dir"
    if fake_dir.is_dir():
        fake_dir.rmdir()
    with pytest.raises(FileNotFoundError):
        gen.dir_verify(fake_dir)

def test_dir_verify2():
    fake_dir = LOCAL_DIR / "output" / "test_dir"
    if fake_dir.is_dir():
        fake_dir.rmdir()
    assert(gen.dir_verify(fake_dir, create=True))
    assert(fake_dir.is_dir())


def test_file_exist_warn(caffeine_sdf: Path):
    assert(gen.file_exist_warn(caffeine_sdf))
    fake_dir = LOCAL_DIR / "output" / "test.txt"
    assert(not gen.file_exist_warn(fake_dir))


def test_file_verify(caffeine_sdf: Path):
    assert(gen.file_verify(caffeine_sdf))
    fake_dir = LOCAL_DIR / "output" / "test.txt"
    with pytest.raises(FileNotFoundError):
        gen.file_verify(fake_dir)


def test_find_file_rec1():
    # test returns from a folder
    fake_dir = LOCAL_DIR / "input"
    expected = [LOCAL_DIR / "input" / "rec.sdf", LOCAL_DIR / "input" / "rec.txt", 
        LOCAL_DIR / "input" / "rec_test" / "rec.sdf",  LOCAL_DIR / "input" / "rec_test" / "rec.html",
        LOCAL_DIR / "input" / "none"]
    result = gen.find_files_rec(fake_dir)
    assert(sorted(expected) == sorted(result))
    
    expected = [LOCAL_DIR / "input" / "rec.sdf",  LOCAL_DIR / "input" / "rec_test" / "rec.sdf"]
    result = gen.find_files_rec(fake_dir, ["sdf"])
    assert(sorted(expected) == sorted(result))

    expected = [LOCAL_DIR / "input" / "rec.txt"]
    result = gen.find_files_rec(fake_dir, ["txt"])
    assert(sorted(expected) == sorted(result))

    expected = [LOCAL_DIR / "input" / "rec.txt", LOCAL_DIR / "input" / "rec_test" / "rec.html"]
    result = gen.find_files_rec(fake_dir, ["txt", "html"])
    assert(sorted(expected) == sorted(result))

    expected = []
    result = gen.find_files_rec(fake_dir, ["pdf"])
    assert(sorted(expected) == sorted(result))

def test_find_file_rec2():
    # check error works
    fake_dir = LOCAL_DIR / "input"
    with pytest.raises(Exception):
        result = gen.find_files_rec(fake_dir, ["pdf"], True)


def test_get_type(caffeine_sdf):
    assert gen.get_type(caffeine_sdf) == "sdf"
    fake_dir = LOCAL_DIR / "input" / "fake.txt"
    with pytest.raises(FileNotFoundError):
        gen.get_type(fake_dir)
    fake_dir = LOCAL_DIR / "input" / "none"
    assert gen.get_type(fake_dir) == None
    fake_dir = LOCAL_DIR / "input" / "rec.Sdf"
    assert gen.get_type(fake_dir) == "sdf"


def test_type_verify(caffeine_sdf):
    assert(gen.type_verify(caffeine_sdf, ["sdf"]) == "sdf")
    assert(gen.type_verify(caffeine_sdf, ["sdf","txt"]) == "sdf")
    with pytest.raises(Exception):
        gen.type_verify(caffeine_sdf, ["txt"])
    fake_dir = LOCAL_DIR / "input" / "none"
    with pytest.raises(Exception):
        gen.type_verify(fake_dir, ["txt"])
    with pytest.raises(Exception):
        gen.type_verify(caffeine_sdf, [])


