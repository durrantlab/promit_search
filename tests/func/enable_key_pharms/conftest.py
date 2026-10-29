
import os
import pytest
from pathlib import Path

LOCAL_DIR = Path(os.path.dirname(__file__))


@pytest.fixture
def protein_file():
    return LOCAL_DIR / "input" / "prot.pdb"

