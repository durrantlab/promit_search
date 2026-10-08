
import argparse
import sys

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