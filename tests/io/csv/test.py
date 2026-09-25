
""" Status: fully tests all CSV functions """

import pytest
from pathlib import Path

from promit_search.io import csv

def test_read(test1_csv: Path):
    test_list: list[list[str]] = [
        ["2","4","6","8"],
        ["10","12","14","16"],
        ["18","20","22","24"]
        ]
    read_list = csv.read_list(test1_csv)
    assert(test_list == read_list)

def test_read_dne(test3_csv: Path):
    with pytest.raises(FileNotFoundError):
        csv.read_list(test3_csv)

def test_write(test2_csv: Path):
    test2_csv.unlink()
    test_list: list[list[str]] = [
        ["0","1","2","3","4"],
        ["5","6","7","8","9"],
        ["10","11","12","13","14"]
        ]
    csv.write_list(test_list, test2_csv, create_dir=True)
    read_list = csv.read_list(test2_csv)
    assert(test_list == read_list)
