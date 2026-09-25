
import pytest
from promit_search import enable_logging
from pathlib import Path

DIR_SCRIPT: Path = Path(__file__).parent.resolve()


@pytest.fixture(scope="session", autouse=True)
def turn_on_logging():
    enable_logging(10)

@pytest.fixture
def caffeine_sdf():
    return DIR_SCRIPT / "input" / "caffeine.sdf"
