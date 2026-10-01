""" Status: working on it """

import pytest
from pathlib import Path
import os

from promit_search.io import text

LOCAL_DIR = Path(os.path.dirname(__file__))


def test_write():
    # list of strings, one per line
    out_file = LOCAL_DIR / "output" / "text_out.txt"
    if out_file.is_file():
        out_file.unlink()
    expected = ["first line", "second line", "third line"]
    text.write(expected, out_file)
    assert(out_file.is_file())
    result = out_file.read_text().splitlines()
    assert(expected == result)


def test_write2():
    # single string writes a single line
    out_file = LOCAL_DIR / "output" / "text_single.txt"
    if out_file.is_file():
        out_file.unlink()
    text.write("only line", out_file)
    assert(out_file.is_file())
    result = out_file.read_text().splitlines()
    assert(result == ["only line"])


def test_write3():
    # empty list still makes the file
    out_file = LOCAL_DIR / "output" / "text_empty.txt"
    if out_file.is_file():
        out_file.unlink()
    text.write([], out_file)
    assert(out_file.is_file())
    assert(out_file.read_text().splitlines() == [])


def test_write4():
    # existing file is replaced, not appended to
    out_file = LOCAL_DIR / "output" / "text_overwrite.txt"
    text.write(["old"], out_file)
    text.write(["new"], out_file)
    assert(out_file.read_text().splitlines() == ["new"])


def test_write5():
    # missing directory and no permission to make it
    out_dir = LOCAL_DIR / "output" / "text_dir"
    out_file = out_dir / "text_out.txt"
    if out_file.is_file():
        out_file.unlink()
    if out_dir.is_dir():
        out_dir.rmdir()
    with pytest.raises(Exception):
        text.write(["first line"], out_file)
    assert(not out_file.is_file())


def test_write6():
    # missing directory is created when asked
    out_dir = LOCAL_DIR / "output" / "text_dir"
    out_file = out_dir / "text_out.txt"
    if out_file.is_file():
        out_file.unlink()
    if out_dir.is_dir():
        out_dir.rmdir()
    expected = ["first line", "second line"]
    text.write(expected, out_file, create_dir=True)
    assert(out_dir.is_dir())
    assert(out_file.read_text().splitlines() == expected)


def test_write7():
    # create_dir on a directory that already exists is a no-op
    out_file = LOCAL_DIR / "output" / "text_exists.txt"
    if out_file.is_file():
        out_file.unlink()
    text.write(["first line"], out_file, create_dir=True)
    assert(out_file.read_text().splitlines() == ["first line"])


def test_write8():
    # target path is a directory
    out_file = LOCAL_DIR / "output"
    with pytest.raises(Exception):
        text.write(["first line"], out_file)