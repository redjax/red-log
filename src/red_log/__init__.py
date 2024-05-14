## Initialize app logger high up in the package heirarchy to ensure child loggers
#  instantiated with logging.getLogger(__name__) inherit defaults from the root logger.
from __future__ import annotations

import logging
from logging.config import dictConfig

from .configs import DEFAULT_LOGGING_CONFIG
from .core.constants import DEFAULT_DATE_FMT, DEFAULT_FMT
from .formatters import DEFAULT_LOG_FORMATTER
from .handlers import (
    APP_FILE_HANDLER,
    CLI_CONSOLE_HANDLER,
    CONSOLE_HANLDER,
    ERR_FILE_HANDLER,
    ROTATING_FILE_HANDLER,
    TIMED_ROTATING_FILE_HANDLER,
)
from .loggers import DEFAULT_ROOT_LOGGER, REQUESTS_LOGGER, SILENT_LOGGER, UVICORN_LOGGER
from .utils import configure_root_logger

## Configure logging for red_log using the default logging config
# dictConfig(DEFAULT_LOGGING_CONFIG)
# logging.getLogger(__name__).addHandler(logging.NullHandler())