
""" Status: working on it """

import pytest
from pathlib import Path
import os

from promit_search.pharmit.web import get_pharms
from promit_search.pharmit.local import get_pharms as get_pharms_local

LOCAL_DIR = Path(os.path.dirname(__file__))

def test_web_search(caffeine_sdf, json_compare):
    """Tests the web search features for a valid molecule"""
    output = LOCAL_DIR / "output" / "op.json"
    if output.is_file():
        output.unlink()
    assert(get_pharms.main(caffeine_sdf, output))
    assert(output.is_file())
    test = LOCAL_DIR / "input" / "web_pharms.json"
    assert(json_compare(output, test, 0.1, ["points","name","radius","x","y","z"]))
    output2 = LOCAL_DIR / "output" / "op2.json"
    if output2.is_file():
        output2.unlink()
    get_pharms_local(caffeine_sdf, out_file=output2)
    assert(json_compare(output, output2, 0.1, ["points","name","radius","x","y","z"]))


