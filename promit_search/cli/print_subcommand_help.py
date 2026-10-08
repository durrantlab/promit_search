
import argparse
import sys

def print_help(
    parser: argparse.ArgumentParser, args: argparse.Namespace
) -> None:
    """_summary_

    Args:
        parser (argparse.ArgumentParser): _description_
        args (argparse.Namespace): _description_
    """
    if args.command:
        parser.parse_args([args.command, "--help"])
    else:
        parser.print_help()