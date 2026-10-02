
import pytest
from promit_search import enable_logging
from pathlib import Path

DIR_SCRIPT: Path = Path(__file__).parent.resolve()

# files
@pytest.fixture(scope="session", autouse=True)
def turn_on_logging():
    enable_logging(10)

@pytest.fixture
def caffeine_sdf():
    return DIR_SCRIPT / "input" / "caffeine.sdf"

@pytest.fixture
def multi_sdf():
    return DIR_SCRIPT / "input" / "multi.sdf"


@pytest.fixture
def empty_sdf():
    return DIR_SCRIPT / "input" / "empty.sdf"

@pytest.fixture
def invalid_sdf():
    return DIR_SCRIPT / "input" / "invalid.sdf"

@pytest.fixture
def multi_sdf_simple():
    return DIR_SCRIPT / "input" / "multi_sdf_simple"



# helper functions
import json

@pytest.fixture()
def json_compare():
    def _json_compare(json_file1: Path, json_file2: Path, 
                      tol: float = 0.1, valid_keys: list[str] = []) -> bool:
        """Compares two JSON files. Every key must be present in both
        files and every value must match. Numbers only need to match
        within a tolerance.
        Assumes both files' existance is already validated.
    
        Args:
            json_file1: first JSON file
            json_file2: second JSON file
            tol: allowed difference between two numbers
            valid_keys: keys that will be checked. Default is checking all.
    
        Returns:
            True if the two files match
    
        Raises:
            Exception: if the files differ, listing every difference
        """
        data1 = json.loads(Path(json_file1).read_text())
        data2 = json.loads(Path(json_file2).read_text())
    
        diffs = []
        _compare(data1, data2, "root", tol, diffs, valid_keys)
    
        if diffs:
            report = "\n".join(diffs)
            raise Exception(
                f"{json_file1} and {json_file2} do not match:\n{report}"
            )
        return True
    return _json_compare
 
def _is_num(value) -> bool:
    """Checks if a value is a number. Bools are ints in python,
    so they are excluded on purpose.
 
    Args:
        value: any json value
 
    Returns:
        True if the value should be compared with a tolerance
    """
    return isinstance(value, (int, float)) and not isinstance(value, bool)
 
 
def _compare(val1, val2, path: str, tol: float, diffs: list[str], valid_keys: list[str]):
    """Walks two json structures together and records every
    difference it finds into diffs.
 
    Args:
        val1: value from the first file
        val2: value from the second file
        path: location of this value, used in the messages
        tol: allowed difference between two numbers
        diffs: running list of differences, added to in place
    """
    if isinstance(val1, dict) and isinstance(val2, dict):
        if len(valid_keys) > 0:
            keys1 = set(val1).intersection(valid_keys)
            keys2 = set(val2).intersection(valid_keys)
        else:
            keys1 = set(val1)
            keys = set(val2)
        for key in sorted(keys1 - keys2):
            diffs.append(f"{path}.{key}: only in first file")
        for key in sorted(keys2 - keys1):
            diffs.append(f"{path}.{key}: only in second file")
        for key in sorted(keys1 & keys2):
            _compare(val1[key], val2[key], f"{path}.{key}", tol, diffs, valid_keys)
        return
 
    if isinstance(val1, list) and isinstance(val2, list):
        if len(val1) != len(val2):
            diffs.append(f"{path}: length {len(val1)} != {len(val2)}")
        for i in range(min(len(val1), len(val2))):
            _compare(val1[i], val2[i], f"{path}[{i}]", tol, diffs, valid_keys)
        return
 
    if _is_num(val1) and _is_num(val2):
        if abs(val1 - val2) > tol:
            diffs.append(f"{path}: {val1} != {val2} (tol {tol})")
        return
 
    if type(val1) != type(val2):
        diffs.append(f"{path}: type {type(val1).__name__} != {type(val2).__name__}")
        return
 
    if val1 != val2:
        diffs.append(f"{path}: {val1!r} != {val2!r}")
 
 
