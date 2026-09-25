
""" writes a list of lists to a csv """

from pathlib import Path 
from promit_search.io import gen

def write_list(lst: list[list[str]], csv_path: Path, create_dir: bool = False):
    """Takes in a list and writes it. Each 2D index
    seperated by , each 1D index seperated by new line

    Args:
        lst: 2D list of strings
        csv_path: where csv will be printed
        create_dir: if create the dir if it does not exist
    
    Raise:
        FileNotFound: if directory does not exist, and create_dir is false
        Exception: if tried to create directory and could not
    """
    gen.dir_verify(csv_path, create_dir)
    gen.file_exist_warn(csv_path, "overwriting file")

    with open(csv_path, "w") as f:
        f.write("\n".join([",".join(item) for item in lst]))