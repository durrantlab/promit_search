
"""Takes in a molecule file and runs pharmit's pharmacophore generation"""

import logging
from pathlib import Path

from promit_search.io import sdf
from promit_search.io import gen

from .lib import *

def single_file(molecule_file: str, output_dir: str,
    create_directories: bool = False, pharmit_run: str = "slurm"):
    """Takes in a file, reads in
    the molecule(s) and outputs pharmacophore JSON(s)
    that can be used with Pharmit.

    Determines file type from suffix of file. Suffix of file
    must align with data type inside file.
    Types allowed: sdf

    Args:
        molecule_file: file path that holds molecule(s)
        output_dir: dir path that holds output
            If file already present, will replace file.
            Name based on molecule's name
        create_directories: if the output file's
            directory is not present, will create full tree.
            Else will crash
        pharmit_run: how pharmit will be run. 
            "slurm": creates batch job script in output
                directory that submits Pharmit job
            "web": will use the website's API to get
                pharmacophores
            "local": will use locally installed version
                of pharmit
    """

    # check validity of molecule_file path
    mole_file_path: Path = Path(molecule_file).resolve()
    if(not gen.file_verify(mole_file_path)):
        raise Exception(f"Molecule file input not present. {mole_file_path}")
    
    # get molecule_file type
    file_type: str | None = gen.get_type(mole_file_path)
    if not file_type in ["sdf"]:
        raise Exception("Not a valid file type")

    # check validity of output_file path
    output_dir: Path = Path(output_dir).resolve()
    if not gen.dir_verify(output_dir, create_directories):
        raise Exception("Output directory input not present")

    ## validate file type, and get molecules inside
    # IF SDF, run SDF specific code. validate / return molecule(s)
    if file_type == "sdf":
        mols = sdf.validate(mole_file_path)

    ## create pharmacophores
    # if doing via slurm job (default)
    if pharmit_run == "slurm":
        pharm_slurm(mols, output_dir)
    # if doing via website
    if pharmit_run == "web":
        pharm_web(mols, output_dir)
    # if doing via local install
    if pharmit_run == "local":
        pharm_local(mols, output_dir)



