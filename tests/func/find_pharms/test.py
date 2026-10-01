from threading import local

import pytest
from pathlib import Path
import os
import shutil

from promit_search.func.find_pharms import single_file

LOCAL_DIR = Path(os.path.dirname(__file__))

# test slurm created is correct
def test_slurm(caffeine_sdf):
    pass

# test that web output is valid



# test that local output is valid


# test that local and web are similar


def test_find_pharms_single_slurm():
    """Tests that slurm functionality is complete"""
    caffeine_sdf = (LOCAL_DIR / "input" / "caffeine.sdf").resolve()
    op_dir: Path = (LOCAL_DIR / "output" / "create_pharm_json" / "slurm").resolve()
    if op_dir.is_dir():
        shutil.rmtree(op_dir)
    single_file(caffeine_sdf,op_dir, create_directories=True, pharmit_run="slurm")
    assert((caffeine_sdf.parent / "make_pharms.slurm").is_file())
    



def test_find_pharms_single_web():
    """Tests that web functionality is complete"""
    caffeine_sdf = (LOCAL_DIR / "input" / "caffeine.sdf").resolve()
    op_dir: Path = (LOCAL_DIR / "output" / "create_pharm_json")
    if op_dir.is_dir():
        shutil.rmtree(op_dir)
    op_dir_web = op_dir / "web"
    single_file(caffeine_sdf,op_dir_web, create_directories=True,  pharmit_run="web")
    assert((op_dir_web / "caff_mol.sdf").is_file())



def test_find_pharms_single_local():
    """Tests that local functionality is complete"""
    caffeine_sdf = (LOCAL_DIR / "input" / "caffeine.sdf").resolve()
    op_dir: Path = (LOCAL_DIR / "output" / "create_pharm_json")
    if op_dir.is_dir():
        shutil.rmtree(op_dir)
    op_dir_local = op_dir / "local"
    single_file(caffeine_sdf,op_dir_local, create_directories=True,  pharmit_run="local")
    assert((op_dir_local / "caff_mol.sdf").is_file())