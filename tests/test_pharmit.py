
from pathlib import Path

from promit_search.pharmit.web import get_pharms
from promit_search import enable_logging


def test_web_search():
    """Status: runs, doesnt check promit_search.pharmit.web"""
    Path("output/pharmit_search").mkdir(parents=True,exist_ok=True)
    enable_logging(level_set=20,file_path="output/pharmit_search/op.log")
    get_pharms.main(Path("input/caffeine.sdf"), Path("output/pharmit_search/op.json"))

