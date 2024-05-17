## Initialize app logger high up in the package heirarchy to ensure child loggers
#  instantiated with logging.getLogger(__name__) inherit defaults from the root logger.
from __future__ import annotations

import logging
from logging.config import dictConfig

from .configs import DEFAULT_LOGGING_CONFIG
from .constants import DEFAULT_DATE_FMT, DEFAULT_FMT
from .constants import LogLevels
from .formatters import DEFAULT_LOG_FORMATTER
from .handlers import (
    APP_FILE_HANDLER,
    CLI_CONSOLE_HANDLER,
    CONSOLE_HANDLER,
    ERR_FILE_HANDLER,
    ROTATING_FILE_HANDLER,
    TIMED_ROTATING_FILE_HANDLER,
)
from .loggers import DEFAULT_ROOT_LOGGER, REQUESTS_LOGGER, SILENT_LOGGER, UVICORN_LOGGER
from .utils import configure_root_logger


## Dict config for library logger
dictConfig(
    config={
        "version": 1,
        "disable_existing_loggers": False,
        "propagate": False,
        "formatters": {
            f"default": {
                "format": "[%(asctime)s] [%(levelname)s]: %(message)s",
                "datefmt": DEFAULT_DATE_FMT,
            }
        },
        "handlers": {
            f"console": {
                "class": "logging.StreamHandler",
                "formatter": "default",
                "level": "DEBUG",
                "stream": "ext://sys.stdout",
            }
        },
        "loggers": {"red_log": {"handlers": ["console"], "level": "WARNING"}},
    }
)
