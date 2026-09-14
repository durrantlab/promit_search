"""Reproducible workflow for generating protein-ligand based interaction pharmacophore searching."""

from importlib.metadata import version, PackageNotFoundError
import os
import sys
from ast import literal_eval
from typing import Any

from loguru import logger

try:
    __version__ = version("promit_search")
except PackageNotFoundError:
    __version__ = "0.0.0"


logger.disable("promit_search")

LOG_FORMAT = (
    "<green>{time:HH:mm:ss}</green> | "
    "<level>{level: <8}</level> | "
    "<level>{message}</level>"
)


def enable_logging(
    level_set: int,
    stdout_set: bool = True,
    file_path: str | None = None,
    log_format: str = LOG_FORMAT,
    colorize: bool = True,
) -> None:
    r"""Enable logging.

    Args:
        level: Requested log level: `10` is debug, `20` is info.
        file_path: Also write logs to files here.
    """
    config: dict[str, Any] = {"handlers": []}
    if stdout_set:
        config["handlers"].append(
            {
                "sink": sys.stdout,
                "level": level_set,
                "format": log_format,
                "colorize": colorize,
            }
        )
    if isinstance(file_path, str):
        config["handlers"].append(
            {
                "sink": file_path,
                "level": level_set,
                "format": log_format,
                "colorize": colorize,
            }
        )
    # https://loguru.readthedocs.io/en/stable/api/logger.html#loguru._logger.Logger.configure
    logger.configure(**config)

    logger.enable("promit_search")


if literal_eval(os.environ.get("PROMIT_SEARCH_LOG", "False")):
    level = int(os.environ.get("PROMIT_SEARCH_LOG_LEVEL", 20))
    stdout = literal_eval(
        os.environ.get("PROMIT_SEARCH_STDOUT", "True")
    )
    log_file_path = os.environ.get(
        "PROMIT_SEARCH_LOG_FILE_PATH", None
    )
    enable_logging(level, stdout, log_file_path)
