from __future__ import annotations

import typing as t
from enum import Enum
import logging


DEFAULT_FMT: str = (
    "[%(asctime)s] [%(levelname)s] > [%(filename)s:%(lineno)d] [%(funcName)s]: %(message)s"
)

DEFAULT_DATE_FMT: str = "%Y-%m-%d %H:%M:%S"

DEFAULT_LOGGER_STYLE: str = "%"


class LogLevelsEnum(Enum):
    """Enum to convert input string to logging.LEVELNAME."""

    NOTSET = logging.NOTSET
    DEBUG = logging.DEBUG
    INFO = logging.INFO
    WARNING = logging.WARNING
    ERROR = logging.ERROR
    CRITICAL = logging.CRITICAL


class LogLevelIntsEnum(Enum):
    """Use input string to get log level as integer value.

    Example:
            log_level: int = LogLevelIntEnum("INFO").value  # = 20
    """

    NOTSET: int = 0
    DEBUG: int = 10
    INFO: int = 20
    WARNING: int = 30
    ERROR: int = 40
    CRITICAL: int = 50
