import argparse
import sys

from .subparse.add_subparsers import add_subparsers


def create_parser() -> argparse.ArgumentParser:
    """Creates the parser. Sets up general arguments, and adds in the subparsers

    Returns:
        argparse.ArgumentParser: the arguments + subparsers added in
    """
    parser = argparse.ArgumentParser(
        "promit_search",
        description="Promit Search: protein-ligand based interaction pharmacophore searching.",
    )
    parser.add_argument("-v", action="store_true", help="More log verbosity.")
    parser.add_argument("-vv", action="store_true", help="Even more log verbosity.")
    parser.add_argument("--logfile", help="Specify a file to write logs to.")
    parser.add_argument("--config", help="Path to YAML configuration file.")

    subparse_group = parser.add_subparsers(dest="command")
    add_subparsers(subparse_group)
    return parser
