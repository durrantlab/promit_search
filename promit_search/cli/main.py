from loguru import logger

from .logging import *
from .parsers import *


def main():
    """The main function that powers the promit_search command-line interface."""
    # setup all arguments of parser
    parser = create_parser()
    # get user results
    args = parser.parse_args()
    setup_logging(args)
    logger.info("promit_search by the Durrant Lab <durrantj@pitt.edu>")

    # if the func 'method' is present for this subparser
    # will try to run it
    if hasattr(args, "func"):
        try:
            args.func(args)
        except Exception as e:
            logger.error(e)
            raise SystemExit(1)
    # if not present, somethign wrong with input. Give help
    else:
        if args.command:
            parser.parse_args([args.command, "--help"])
        else:
            parser.print_help()


if __name__ == "__main__":
    main()