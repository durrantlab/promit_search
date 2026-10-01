
import pytest
from pathlib import Path

@pytest.fixture
def slurm():
    return Path("output/make_pharms.slurm").resolve()