from loguru import logger

from .logging import *
from .parsers import *


def main():
    """The main function that powers the promit_search command-line interface."""
    parser = create_parser()
    args = parser.parse_args()
    print_subcommand_help(parser, args)
    setup_logging(args)
    logger.info("promit_search by the Durrant Lab <durrantj@pitt.edu>")

    if hasattr(args, "func"):
        try:
            args.func(args)
        except Exception as e:
            logger.error(e)
            raise SystemExit(1)
    else:
        if args.command:
            parser.parse_args([args.command, "--help"])
        else:
            parser.print_help()


if __name__ == "__main__":
    main()