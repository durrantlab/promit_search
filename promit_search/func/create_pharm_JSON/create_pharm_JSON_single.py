
import logging
from pathlib import Path

from promit_search.io.gen import get_type
from promit_search.io import sdf
from promit_search.io import gen

from .pharm_slurm import pharm_slurm

def create_pharm_JSON_single(molecule_file: str, output_file: str,
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
    if(gen.file_verify(mole_file_path)):
        raise Exception("Molecule file input not present")
    
    # get molecule_file type
    file_type: str | None = get_type(mole_file_path)
    if not file_type in ["sdf"]:
        raise Exception("Not a valid file type")

    # check validity of output_file path
    op_file_path: Path = Path(output_file).resolve()
    if(not op_file_path.is_dir()):
        if create_directories:
            op_file_path.mkdir(parents=True, exist_ok=True)
        else:
            raise Exception("Output directory input not present")

    ## validate file type, and get molecules inside
    # IF SDF, run SDF specific code. validate / return molecule(s)
    if file_type == "sdf":
        mols = sdf.validate(mole_file_path)

    ## create pharmacophores
    # if doing via slurm job (default)
    if pharmit_run == "slurm":
        pharm_slurm(mole_file_path, mols, op_file_path)
    # if doing via website
    if pharmit_run == "web":
        pharm_slurm(mole_file_path, mols, op_file_path)

    # if doing via local install
     


