"""Define formatters, handlers, and loggers for third-party dependencies."""

from __future__ import annotations

from . import red_log_logging
from .red_log_logging import (
    get_red_log_console_handler,
    get_red_log_formatter,
    get_red_log_logger,
)
