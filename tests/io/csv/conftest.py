
import os
import pytest
from pathlib import Path

LOCAL_DIR = Path(os.path.dirname(__file__))


@pytest.fixture
def test1_csv():
    return LOCAL_DIR / "input" / "test1.csv"

@pytest.fixture
def test2_csv():
    return LOCAL_DIR / "output" / "test2.csv"

@pytest.fixture
def test3_csv():
    return LOCAL_DIR / "input" / "test3.csv"
