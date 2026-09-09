


def create_pharm_JSON(molecule_file: str, output_dir: str,
    create_directories: bool = False):
    """Takes in a folder (currently just SDF), reads in all
    files of a known type (SDF) and outputs a pharmacophore JSON
    that can be used with Pharmit

    Args:
        molecule_file: file path that holds molecule
        output_dir: dir path that holds all outputs
            If file already present, will replace file.
            Name based on molecule's name
        create_directories: if the output file's
            directory is not present, will create full tree.
            Else will crash
    """

