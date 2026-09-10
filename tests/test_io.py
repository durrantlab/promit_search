
from pathlib import Path

from promit_search import io


def get_type_test():
    caffeine_file: Path = Path("input/caffeine.sdf").resolve()
    invalid_file: Path = Path("input/caffeine").resolve()
    if not io.get_type(caffeine_file) == "sdf":
        raise Exception("Get type invalid for .sdf")
    if not io.get_type(invalid_file) == None:
        raise Exception("Get type invalid for invalid file type")
    print("get_type_test is valid")



def csv_test():
    csv_file: Path = Path("input/test1.csv").resolve()
    test_list: list[list[str]] = [
        ["2","4","6","8"],
        ["10","12","14","16"],
        ["18","20","22","24"]
        ]
    read_list = io.csv.read_list(csv_file)
    if not test_list == read_list:
        raise Exception("csv read is invalid")
    
    csv_file: Path = Path("input/test2.csv").resolve()
    test_list: list[list[str]] = [
        ["0","1","2","3","4"],
        ["5","6","7","8","9"],
        ["10","11","12","13","14"]
        ]
    io.csv.write_list(test_list, csv_file)
    read_list = io.csv.read_list(csv_file)
    if not test_list == read_list:
        raise Exception("csv read or write is invalid")
    print("get_type_test is valid")


if __name__ == "__main__":
    get_type_test()
    csv_test()