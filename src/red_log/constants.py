from __future__ import annotations

import typing as t
from enum import Enum
import logging


DEFAULT_FMT: str = (
    "[%(asctime)s] [%(levelname)s] > [%(filename)s:%(lineno)d] [%(funcName)s]: %(message)s"
)

DEFAULT_DATE_FMT: str = "%Y-%m-%d %H:%M:%S"

DEFAULT_LOGGER_STYLE: str = "%"


class LogLevels(Enum):
    """Enum to convert input string to logging.LEVELNAME."""

    NOTSET = logging.NOTSET
    DEBUG = logging.DEBUG
    INFO = logging.INFO
    WARNING = logging.WARNING
    ERROR = logging.ERROR
    CRITICAL = logging.CRITICAL
