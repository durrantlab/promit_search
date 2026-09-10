
from pathlib import Path

from promit_search.io import gen
from promit_search.io import csv
from promit_search.io import slurm


def gen_test():
    caffeine_file: Path = Path("input/caffeine.sdf").resolve()
    invalid_file: Path = Path("input/caffeine").resolve()
    if not gen.get_type(caffeine_file) == "sdf":
        raise Exception("Get type invalid for .sdf")
    if not gen.get_type(invalid_file) == None:
        raise Exception("Get type invalid for invalid file type")
    
    if not gen.file_verify(caffeine_file):
        raise Exception("File verify is invalid")
    if not gen.dir_verify(caffeine_file.parent):
        raise Exception("Dir verify is invalid")    
    
    print("gen_test is valid")



def csv_test():
    csv_file: Path = Path("input/test1.csv").resolve()
    test_list: list[list[str]] = [
        ["2","4","6","8"],
        ["10","12","14","16"],
        ["18","20","22","24"]
        ]
    read_list = csv.read_list(csv_file)
    if not test_list == read_list:
        raise Exception("csv read is invalid")
    
    csv_file: Path = Path("input/test2.csv").resolve()
    test_list: list[list[str]] = [
        ["0","1","2","3","4"],
        ["5","6","7","8","9"],
        ["10","11","12","13","14"]
        ]
    csv.write_list(test_list, csv_file)
    read_list = csv.read_list(csv_file)
    if not test_list == read_list:
        raise Exception("csv read or write is invalid")
    print("csv_test is valid")
    csv_file.unlink()

def slurm_test():
    # basic single slurm
    test_file1: Path = Path("input/check1.slurm").resolve()
    op_file: Path = Path("output/output.slurm").resolve()
    gen.dir_create(Path("output"))
    body: list[str] = ["line 1","line 2","line 3"]
    settings = {"mem": "4G", "job-name": "pharm_search",
        "cpus-per-task": "4", "output":"test.out"}
    slurm.create_single(body, op_file, settings)
    with open(test_file1, "r") as f:
        with open(op_file, "r") as f2:
            if not f.read() == f2.read():
                raise Exception("Single slurm creation invalid")
    op_file.unlink()

    # basic multi slurm test
    test_file1: Path = Path("input/check2.slurm").resolve()
    test_file2: Path = Path("input/check2.sh").resolve()
    test_file3: Path = Path("job_list.txt").resolve()
    op_file: Path = Path("output/output.slurm").resolve()
    op_file2: Path = Path("output/output.sh").resolve()
    op_file3: Path = Path("output/job_list.txt").resolve()
    body: list[str] = ["line 1","line 2","line 3"]
    settings = {"mem": "4G", "job-name": "pharm_search",
        "cpus-per-task": "4", "output":"test.out"}
    slurm.create_multi(body, op_file, settings)
    with open(test_file1, "r") as f:
        with open(op_file, "r") as f2:
            if not f.read() == f2.read():
                raise Exception("Multi slurm creation invalid - slurm")
    with open(test_file2, "r") as f:
        with open(op_file2, "r") as f2:
            if not f.read() == f2.read():
                raise Exception("Multi slurm creation invalid - sh")
    with open(test_file3, "r") as f:
        with open(op_file3, "r") as f2:
            if not f.read() == f2.read():
                raise Exception("Multi slurm creation invalid - txt")

    op_file.unlink()

    print("slurm_test is valid")
    



if __name__ == "__main__":
    gen_test()
    csv_test()
    slurm_test()