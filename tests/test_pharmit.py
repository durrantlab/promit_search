
from pathlib import Path

from promit_search.pharmit.web import get_pharms
from promit_search import enable_logging


def test_web_search():
    enable_logging(10)
    get_pharms.main(Path("input/caffeine.sdf"), Path("output/pharmit_search/op.json"))
