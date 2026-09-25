
import os
import pytest
from pathlib import Path

LOCAL_DIR = Path(os.path.dirname(__file__))


@pytest.fixture
def file1():
    return LOCAL_DIR / "input" / "test1.csv"

def file2():
    return LOCAL_DIR / "output" / "test2.csv"

def file3():
    return LOCAL_DIR / "input" / "test3.csv"
