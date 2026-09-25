import argparse
import sys

from psma1_vs.cli.visualize import main as visualize_main


def create_parser() -> argparse.ArgumentParser:
    """Creates the parser. Sets up general arguments, and adds in the subparsers

    Returns:
        argparse.ArgumentParser: _description_
    """
    parser = argparse.ArgumentParser(
        "psma1-vs",
        description="PSMA1-VS: Tools for computational drug design targeting PSMA1 and related targets.",
    )
    parser.add_argument("-v", action="store_true", help="More log verbosity.")
    parser.add_argument("-vv", action="store_true", help="Even more log verbosity.")
    parser.add_argument("--logfile", help="Specify a file to write logs to.")
    parser.add_argument("--config", help="Path to YAML configuration file.")

    subparsers = parser.add_subparsers(dest="command")
    visualize_main.add_subparsers(subparsers)
    return parser


def print_subcommand_help(
    parser: argparse.ArgumentParser, args: argparse.Namespace
) -> None:
    """_summary_

    Args:
        parser (argparse.ArgumentParser): _description_
        args (argparse.Namespace): _description_
    """
    if not args.command:
        parser.print_help()
        sys.exit(0)