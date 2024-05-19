from __future__ import annotations

from red_log.formatters import (
    DEFAULT_LOG_FORMATTER,
)
from red_log.handlers.prefab import (
    APP_FILE_HANDLER,
    CLI_CONSOLE_HANDLER,
    CONSOLE_HANDLER,
    ERR_FILE_HANDLER,
    ROTATING_FILE_HANDLER,
    TIMED_ROTATING_FILE_HANDLER,
)
from red_log.loggers import DEFAULT_ROOT_LOGGER

## The base configuration dict for a logging.Logger
CONFIG_DICT_BASE: dict = {
    "version": 1,
    "disable_existing_loggers": False,
    "propagate": True,
    "root": {},
    "formatters": {},
    "handlers": {},
    "loggers": {},
}

DEFAULT_LOGGING_CONFIG = dict(
    version=1,
    disable_existing_loggers=False,
    propagate=True,
    root=DEFAULT_ROOT_LOGGER,
    formatters=DEFAULT_LOG_FORMATTER,
    handlers={**CONSOLE_HANDLER},
    loggers={**DEFAULT_ROOT_LOGGER},
)