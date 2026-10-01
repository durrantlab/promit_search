
""" Status: working on it """

import pytest
from pathlib import Path

from promit_search.io import sdf

""" Status: working on it """

import pytest
from pathlib import Path
import os

from rdkit import Chem

from promit_search.io import sdf

LOCAL_DIR = Path(os.path.dirname(__file__))


def test_create_rdkit(caffeine_sdf: Path):
    # single molecule file loads into a supplier
    mols = sdf.create_rdkit(caffeine_sdf)
    assert(isinstance(mols, Chem.SDMolSupplier))
    assert(len(mols) == 1)
    assert(mols[0] is not None)
    assert(Chem.MolToSmiles(mols[0]) is not None)


def test_create_rdkit2(multi_sdf: Path):
    # multi molecule file returns every record
    mols = sdf.create_rdkit(multi_sdf)
    assert(len(mols) == 3)
    assert(all(mol is not None for mol in mols))


def test_create_rdkit3(invalid_sdf: Path):
    # malformed sdf blows up
    with pytest.raises(Exception):
        sdf.create_rdkit(invalid_sdf)


def test_create_rdkit4(empty_sdf: Path):
    # file with no records at all
    with pytest.raises(Warning):
        mols = sdf.create_rdkit(empty_sdf)
    assert(len(mols) == 0)


def test_validate(caffeine_sdf: Path):
    mols = sdf.validate(caffeine_sdf)
    assert(isinstance(mols, Chem.SDMolSupplier))
    assert(len(mols) == 1)
    assert(mols[0] is not None)


def test_validate2(multi_sdf: Path):
    # all records parse
    mols = sdf.validate(multi_sdf)
    assert(len(mols) == 3)
    assert(all(mol is not None for mol in mols))


def test_validate3(invalid_sdf: Path):
    # one bad molecule in an otherwise readable file
    with pytest.raises(Exception):
        sdf.validate(invalid_sdf)


def test_write_from_rdkit(caffeine_sdf: Path):
    # supplier round trips through disk
    out_file = LOCAL_DIR / "output" / "caffeine_out.sdf"
    if out_file.is_file():
        out_file.unlink()
    mols = sdf.create_rdkit(caffeine_sdf)
    expected = [Chem.MolToSmiles(mol) for mol in mols]
    sdf.write_from_rdkit(mols, out_file)
    assert(out_file.is_file())
    result = [Chem.MolToSmiles(mol) for mol in sdf.create_rdkit(out_file)]
    assert(expected == result)


def test_write_from_rdkit2(multi_sdf: Path):
    # multi molecule supplier keeps all records
    out_file = LOCAL_DIR / "output" / "multi_out.sdf"
    if out_file.is_file():
        out_file.unlink()
    mols = sdf.create_rdkit(multi_sdf)
    expected = sorted(Chem.MolToSmiles(mol) for mol in mols)
    sdf.write_from_rdkit(mols, out_file)
    result = sorted(Chem.MolToSmiles(mol) for mol in sdf.create_rdkit(out_file))
    assert(expected == result)


def test_write_from_rdkit3(caffeine_sdf: Path):
    # single Chem.Mol instead of a supplier
    out_file = LOCAL_DIR / "output" / "single_out.sdf"
    if out_file.is_file():
        out_file.unlink()
    mol = sdf.create_rdkit(caffeine_sdf)[0]
    sdf.write_from_rdkit(mol, out_file)
    assert(out_file.is_file())
    result = sdf.create_rdkit(out_file)
    assert(len(result) == 1)
    assert(Chem.MolToSmiles(result[0]) == Chem.MolToSmiles(mol))


def test_write_from_rdkit4(caffeine_sdf: Path):
    # overwrite an existing file
    out_file = LOCAL_DIR / "output" / "overwrite_out.sdf"
    mols = sdf.create_rdkit(caffeine_sdf)
    sdf.write_from_rdkit(mols, out_file)
    sdf.write_from_rdkit(mols, out_file)
    assert(len(sdf.create_rdkit(out_file)) == 1)


def test_write_from_rdkit5(caffeine_sdf: Path):
    # cannot write into a directory that does not exist
    mols = sdf.create_rdkit(caffeine_sdf)
    out_file = LOCAL_DIR / "output" / "no_such_dir" / "out.sdf"
    with pytest.raises(Exception):
        sdf.write_from_rdkit(mols, out_file)


def test_write_from_rdkit6(caffeine_sdf: Path):
    # target path is a directory
    mols = sdf.create_rdkit(caffeine_sdf)
    out_file = LOCAL_DIR / "output"
    with pytest.raises(Exception):
        sdf.write_from_rdkit(mols, out_file)
