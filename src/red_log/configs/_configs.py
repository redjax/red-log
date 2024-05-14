from __future__ import annotations

from red_log.formatters import (
    DEFAULT_LOG_FORMATTER,
)
from red_log.handlers import (
    CLI_CONSOLE_HANDLER,
    CONSOLE_HANLDER,
    APP_FILE_HANDLER,
    ERR_FILE_HANDLER,
    ROTATING_FILE_HANDLER,
    TIMED_ROTATING_FILE_HANDLER,
)
from red_log.loggers import DEFAULT_ROOT_LOGGER

DEFAULT_LOGGING_CONFIG = dict(
    version=1,
    disable_existing_loggers=False,
    propagate=True,
    formatters=DEFAULT_LOG_FORMATTER,
    handlers=[CONSOLE_HANLDER],
    root=DEFAULT_ROOT_LOGGER,
)
