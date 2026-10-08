

import argparse

from promit_search.func.find_pharms import cli

def find_pharms(subparse_group: argparse._SubParsersAction) -> None:
    """Sets up the subparser for the find_pharms function

    Args:
        subparse_group: the subparser group it is added to
    """
    help: str = "Will take in molecule file(s) and return pharmacophore structures for them"
    subparser = subparse_group.add_parser("find_pharms",help=help)
    subparser.set_defaults(func=cli)
    help = "file path that holds molecule(s)"
    subparser.add_argument("-i", "--sdf_path", help=help)
    help = "dir path that holds output. If file already present, will replace file. \
        Name based on molecule's name"
    subparser.add_argument("-o", "--output_path", help=help)
    help = "if the output file's directory is not present, will create full tree. \
            Else will crash"
    subparser.add_argument("-c", "--create_dir", help=help, action="store_true")
    help = """how pharmit will be run.
            "slurm": creates batch job script in output
            directory that submits Pharmit job.
            Called make_pharms.slurm in output dir.
            "web": will use the website's API to get
            pharmacophores
            "local": will use locally installed version
            of pharmit"""
    subparser.add_argument("-r", "--run_type", help=help)
