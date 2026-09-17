
from pathlib import Path

from promit_search.pharmit.web import get_pharms


def test_web_search():
    get_pharms.main(Path("input/caffeine.sdf"), Path("output/pharmit_search/op.json"))
