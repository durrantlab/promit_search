
""" Status: working on it """

import pytest
from pathlib import Path
import os

from promit_search.io import slurm
from promit_search.io import gen

LOCAL_DIR = Path(os.path.dirname(__file__))

def test_create_single1():
    """Status: runs and validates all functions in promit_search.io.slurm"""
    # basic single slurm
    test_file1: Path = LOCAL_DIR / "input" / "check1.slurm"
    op_file: Path = LOCAL_DIR / "input" / "output.slurm"
    if op_file.is_file():
        op_file.unlink()
    body: list[str] = ["line 1","line 2","line 3"]
    settings = {"mem": "4G", "job-name": "pharm_search",
        "cpus-per-task": "4", "output":"test.out"}
    slurm.create_single(body, op_file, settings)
    with open(test_file1, "r") as f:
        with open(op_file, "r") as f2:
            assert(f.read() == f2.read())

def test_create_multi1():
    # basic multi slurm test
    test_file1: Path = LOCAL_DIR / "input" / "check2.slurm"
    test_file2: Path = LOCAL_DIR / "input" / "check2.sh"
    test_file3: Path = LOCAL_DIR / "input" / "job_list.txt"
    op_file: Path = LOCAL_DIR / "output" / "output.slurm"
    op_file2: Path = LOCAL_DIR / "output" / "output.sh"
    op_file3: Path = LOCAL_DIR / "output" / "job_list.txt"
    if op_file.is_file():
        op_file.unlink()
    if op_file2.is_file():
        op_file2.unlink()
    if op_file3.is_file():
        op_file3.unlink()
    body: list[str] = ["line 1","line 2","line 3"]
    settings = {"mem": "4G", "job-name": "pharm_search",
        "cpus-per-task": "4", "output":"test.out"}
    slurm.create_multi(body, op_file, settings)
    with open(test_file1, "r") as f:
        with open(op_file, "r") as f2:
            assert(f.read() == f2.read())
    with open(test_file2, "r") as f:
        with open(op_file2, "r") as f2:
            assert(f.read() == f2.read())
    with open(test_file3, "r") as f:
        with open(op_file3, "r") as f2:
            assert(f.read() == f2.read())
    