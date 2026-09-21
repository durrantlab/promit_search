import os

import pytest
from promit_search import enable_logging
from pathlib import Path

TEST_DIR = os.path.dirname(__file__)


@pytest.fixture(scope="session", autouse=True)
def turn_on_logging():
    enable_logging(10)

@pytest.fixture
def caffeine_sdf():
    return Path("input/caffeine.sdf").resolve()
