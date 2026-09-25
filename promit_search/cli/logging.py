from argparse import Namespace

from psma1_vs import enable_logging


def setup_logging(args: Namespace):
    """Based on inputs will edit logging

    Args:
        args: inputs from cli
    """
    if args.vv:
        log_level = 0  # TRACE
    elif args.v:
        log_level = 10  # DEBUG
    else:
        log_level = 20  # INFO

    enable_logging(
        log_level,
        True,
        args.logfile,
        log_format="<level>{level: <8}</level> | {message}",
    )