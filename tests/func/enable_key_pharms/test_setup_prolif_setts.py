
""" Status: working on it """

import pytest
from pathlib import Path
import os

from promit_search.func.enable_key_pharms.lib.setup_prolif_setts import setup_prolif_setts

LOCAL_DIR = Path(os.path.dirname(__file__))

""" Status: working on it """


def test_setup_prolif_setts():
    # nothing passed in returns the defaults untouched
    expected = {
        "vicinity_cutoff": 10,
        "interactions": [
            "Hydrophobic",
            "HBDonor",
            "HBAcceptor",
            "PiStacking",
            "Anionic",
            "Cationic",
            "CationPi",
            "PiCation",
        ],
        "parameters": {
            "Hydrophobic": {"distance": 5},
            "HBDonor": {"distance": 4.0},
            "HBAcceptor": {"distance": 4.0},
            "Anionic": {"distance": 8},
            "Cationic": {"distance": 8},
            "PiStacking": {
                "ftf_kwargs": {"distance": 8},
                "etf_kwargs": {"distance": 8},
            },
        },
    }
    result = setup_prolif_setts({})
    assert(result == expected)


def test_setup_prolif_setts2():
    # a single top level value is replaced, the rest stay default
    default = setup_prolif_setts({})
    result = setup_prolif_setts({"vicinity_cutoff": 6})
    assert(result["vicinity_cutoff"] == 6)
    assert(result["interactions"] == default["interactions"])
    assert(result["parameters"] == default["parameters"])


def test_setup_prolif_setts3():
    # lists are replaced whole, not appended to
    result = setup_prolif_setts({"interactions": ["Hydrophobic"]})
    assert(result["interactions"] == ["Hydrophobic"])
    assert(len(result["interactions"]) == 1)


def test_setup_prolif_setts4():
    # one interaction is edited, the other defaults are kept
    default = setup_prolif_setts({})
    input_setts = {"parameters": {"Hydrophobic": {"distance": 7}}}
    result = setup_prolif_setts(input_setts)
    assert(result["parameters"]["Hydrophobic"] == {"distance": 7})
    assert(result["parameters"]["HBDonor"] == default["parameters"]["HBDonor"])
    assert(sorted(result["parameters"]) == sorted(default["parameters"]))


def test_setup_prolif_setts5():
    # merge goes all the way down the nested dicts
    default = setup_prolif_setts({})
    input_setts = {"parameters": {"PiStacking": {"ftf_kwargs": {"distance": 6}}}}
    result = setup_prolif_setts(input_setts)
    expected = {
        "ftf_kwargs": {"distance": 6},
        "etf_kwargs": default["parameters"]["PiStacking"]["etf_kwargs"],
    }
    assert(result["parameters"]["PiStacking"] == expected)


def test_setup_prolif_setts6():
    # a new key inside a default dict is added, not replacing it
    default = setup_prolif_setts({})
    input_setts = {"parameters": {"VdWContact": {"tolerance": 0.1}}}
    result = setup_prolif_setts(input_setts)
    assert(result["parameters"]["VdWContact"] == {"tolerance": 0.1})
    assert(result["parameters"]["Hydrophobic"] == default["parameters"]["Hydrophobic"])
    assert(len(result["parameters"]) == len(default["parameters"]) + 1)


def test_setup_prolif_setts7():
    # keys that are not defaults get carried through
    result = setup_prolif_setts({"new_sett": "value"})
    assert(result["new_sett"] == "value")
    assert(result["vicinity_cutoff"] == 10)
    assert(len(result) == 4)


def test_setup_prolif_setts8():
    # an empty dict merges nothing, so the defaults survive
    default = setup_prolif_setts({})
    result = setup_prolif_setts({"parameters": {}})
    assert(result["parameters"] == default["parameters"])


def test_setup_prolif_setts9():
    # several levels edited at once
    default = setup_prolif_setts({})
    input_setts = {
        "vicinity_cutoff": 6,
        "interactions": ["Hydrophobic", "HBDonor"],
        "parameters": {
            "Hydrophobic": {"distance": 7},
            "PiStacking": {"etf_kwargs": {"distance": 6}},
        },
    }
    result = setup_prolif_setts(input_setts)
    assert(result["vicinity_cutoff"] == 6)
    assert(result["interactions"] == ["Hydrophobic", "HBDonor"])
    assert(result["parameters"]["Hydrophobic"] == {"distance": 7})
    assert(result["parameters"]["PiStacking"]["etf_kwargs"] == {"distance": 6})
    assert(result["parameters"]["PiStacking"]["ftf_kwargs"] == {"distance": 8})
    assert(result["parameters"]["Anionic"] == default["parameters"]["Anionic"])


def test_setup_prolif_setts10():
    # the dict passed in is not modified
    input_setts = {"parameters": {"Hydrophobic": {"distance": 7}}}
    setup_prolif_setts(input_setts)
    assert(input_setts == {"parameters": {"Hydrophobic": {"distance": 7}}})


def test_setup_prolif_setts11():
    # editing a returned dict does not leak into the next call
    result = setup_prolif_setts({})
    result["vicinity_cutoff"] = 99
    result["parameters"]["Hydrophobic"]["distance"] = 99
    result["interactions"].append("fake")
    default = setup_prolif_setts({})
    assert(default["vicinity_cutoff"] == 10)
    assert(default["parameters"]["Hydrophobic"]["distance"] == 5)
    assert("fake" not in default["interactions"])


def test_setup_prolif_setts12():
    # a dict cannot be merged into a plain value, it replaces it
    result = setup_prolif_setts({"vicinity_cutoff": {"distance": 3}})
    assert(result["vicinity_cutoff"] == {"distance": 3})

