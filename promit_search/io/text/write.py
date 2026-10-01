
""" write out a .txt file from a string """

from pathlib import Path
from promit_search.io import gen

def write(text: list[str] | str, output_file: Path, create_dir: bool = False):
    """Takes in a list of strings and writes them
    to a file. Each string is a different line.

    Args:
        text: the text to be printed
        output_file: path where it is printed
        create_dir: if the directory will be created if it doesnt
            exist
    
    Exception:
        If directory for file does not exist and it can not create it.
        If file path passed as a directory type.
    
    Warns:
        If the file already exists
    """
    gen.dir_verify(output_file.parent, create_dir)
    gen.file_exist_warn(output_file, "Overwriting file.")

    with open(output_file, "w") as f:
        if isinstance(text, list):
            f.write("\n".join(text))
        else:
            f.write(text)