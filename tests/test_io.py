
from pathlib import Path

from promit_search import io

caffeine_file: Path = Path("input/caffeine.sdf").resolve()
invalid_file: Path = Path("input/caffeine").resolve()

def get_type_test():
    if not io.get_type(caffeine_file) == "sdf":
        raise Exception("Get type invalid for .sdf")
    if not io.get_type(invalid_file) == None:
        raise Exception("Get type invalid for invalid file type")
    print("get_type_test is valid")


if __name__ == "__main__":
    get_type_test()