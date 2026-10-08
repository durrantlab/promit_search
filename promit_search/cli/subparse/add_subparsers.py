
import argparse

from .find_pharms import find_pharms

def add_subparsers(subparse_group: argparse._SubParsersAction) -> None:
    """Will take in the subparse group, and add in all the different
    subparsers to it

    Args:
        subparse_group (subparse group): the group all the subparsers are added to
    """
    find_pharms(subparse_group)
