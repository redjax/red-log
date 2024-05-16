from __future__ import annotations

import logging

from enum import Enum

DEFAULT_FMT: str = (
    "[%(asctime)s] [%(levelname)s] > [%(filename)s:%(lineno)d] [%(funcName)s]: %(message)s"
)

DEFAULT_DATE_FMT: str = "%Y-%m-%d %H:%M:%S"

VALID_LOG_LEVELS: str = ["NOTSET", "DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]


class LogLevels(Enum):
    """Enum to convert input string to logging.LEVELNAME."""

    NOTSET = logging.NOTSET
    DEBUG = logging.DEBUG
    INFO = logging.INFO
    WARNING = logging.WARNING
    ERROR = logging.ERROR
    CRITICAL = logging.CRITICAL
