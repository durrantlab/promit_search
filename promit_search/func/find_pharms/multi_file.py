
from pathlib import Path

from promit_search.io import gen 
from promit_search.func.find_pharms.single_file import single_file

def create_pharm_JSON(molecule_dir: str, output_dir: str,
    create_directories: bool = False, pharmit_run: str = "local"):
    """Takes in a folder, reads in all
    files of a known type and outputs a pharmacophore JSON
    that can be used with Pharmit

    Determines file type from suffix of file. Suffix of file
    must align with data type inside file.
    Types allowed: sdf


    Args:
        molecule_file: file path that holds molecule
        output_dir: dir path that holds all outputs
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

    # find all the files and check if dir is valid
    molecule_dir: Path = Path(molecule_dir).resolve()
    all_files: list[Path] = gen.find_files_rec(molecule_dir, ["sdf"])
    # check if output dir exists
    output_dir: Path = Path(output_dir).resolve()
    if not gen.dir_verify(output_dir, create_directories):
        raise Exception("Output directory input not present")
    # go through files and run
    for file in all_files:
        file_op_dir: Path = output_dir / file.name 
        single_file(file, file_op_dir, create_directories=True, pharmit_run=pharmit_run)