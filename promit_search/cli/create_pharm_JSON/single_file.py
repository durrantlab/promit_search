
import logging
from pathlib import Path

from promit_search.io import get_type
from promit_search.io.gen import validate_file

def create_pharm_JSON(molecule_file: str, output_file: str,
    molecule_file_type: str | None = None, create_directories: bool = False):
    """Takes in a file (valid types: SDF), reads in
    the molecule and outputs a pharmacophore JSON
    that can be used with Pharmit

    Args:
        molecule_file: file path that holds molecule
        output_dir: dir path that holds output
            If file already present, will replace file.
            Name based on molecule's name
        molecule_file_type: the type of the file input
            If None, will assume from suffix of molecule_file
            If suffix != this type, crashes
        create_directories: if the output file's
            directory is not present, will create full tree.
            Else will crash
    """

    # check validity of molecule_file path
    if(not validate_file(molecule_file)):
        raise Exception("Molecule file input not present")
    molefile_path: Path = Path(molecule_file).resolve()
    
    # get molecule_file type
    file_type: str = get_type(molefile_path)
    if molecule_file_type != None:
        if file_type != molecule_file_type:
            raise Exception("Molecule file type not equal to input")
    if not file_type in ["sdf"]:
        raise Exception("Not a valid file type")



    # check validity of output_file path

    # IF SDF, run SDF specific code. validate / return molecule(s)

    # for every molecule


