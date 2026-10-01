from threading import local

import pytest
from pathlib import Path
import os
import shutil
from rdkit import Chem

from promit_search.func.find_pharms import single_file
from promit_search.io import sdf

LOCAL_DIR = Path(os.path.dirname(__file__))

# test slurm created is correct
def test_slurm(caffeine_sdf):
    pass

# test that web output is valid



# test that local output is valid


# test that local and web are similar


def test_find_pharms_single_slurm1():
    """Tests that slurm functionality is complete for sdfs with 1 molecule"""
    caffeine_sdf = (LOCAL_DIR / "input" / "caffeine.sdf").resolve()
    op_dir: Path = (LOCAL_DIR / "output" / "create_pharm_json" / "slurm").resolve()
    if op_dir.is_dir():
        shutil.rmtree(op_dir)
    single_file(caffeine_sdf,op_dir, create_directories=True, pharmit_run="slurm")
    assert((op_dir / "make_pharms.slurm").is_file())
    assert((op_dir / "caff_mol.sdf").is_file())
    assert(sdf.validate((op_dir / "caff_mol.sdf")) != None)
    assert(Chem.MolToSmiles(sdf.validate((op_dir / "caff_mol.sdf"))[0])
            == Chem.MolToSmiles(caffeine_sdf))

def test_find_pharms_sigle_slurm2(multi_sdf):
    """Tests that slurm functionality is complete for sdfs with 2+ molecule"""
    op_dir: Path = (LOCAL_DIR / "output" / "create_pharm_json2" / "slurm").resolve()
    if op_dir.is_dir():
        shutil.rmtree(op_dir)
    single_file(multi_sdf,op_dir, create_directories=True, pharmit_run="slurm")
    
    assert((op_dir / "make_pharms.slurm").is_file())
    assert((op_dir / "mole1.sdf").is_file())
    assert((op_dir / "mole4.sdf").is_file())
    assert(sdf.validate((op_dir / "mole4.sdf")) != None)
    for ind, mol in enumerate(sdf.validate(multi_sdf)):
        assert(Chem.MolToSmiles(sdf.validate((op_dir / f"mole{ind+1}.sdf"))[0]) 
            == Chem.MolToSmiles(mol))



def test_find_pharms_single_web():
    """Tests that web functionality is complete"""
    op_dir: Path = (LOCAL_DIR / "output" / "create_pharm_json" / "web").resolve()
    _local_web_test1(op_dir, "web")

def test_find_pharms_single_local(json_compare):
    """Tests that local functionality is complete"""
    op_dir: Path = (LOCAL_DIR / "output" / "create_pharm_json" / "local").resolve()
    _local_web_test1(op_dir, "local")
    assert(json_compare((op_dir / "caff_mol.json"), (op_dir / ".." / "web" / "caff_mol.json"), 
                        0.1, ["points","name","radius","x","y","z"]))




"""Local and web are nearly identical so have same tests"""
def _local_web_test1(op_dir, type):
    """tests that works with a sdf with a single molecule"""
    caffeine_sdf = (LOCAL_DIR / "input" / "caffeine.sdf").resolve()
    if op_dir.is_dir():
        shutil.rmtree(op_dir)
    single_file(caffeine_sdf,op_dir, create_directories=True,  pharmit_run=type)
    assert((op_dir / "caff_mol.sdf").is_file())
    assert(sdf.validate((op_dir / "caff_mol.sdf")) != None)
    assert(Chem.MolToSmiles(sdf.validate((op_dir / "caff_mol.sdf"))[0]) 
            == Chem.MolToSmiles(caffeine_sdf))
    assert((op_dir / "caff_mol.json").is_file())
