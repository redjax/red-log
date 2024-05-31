"""Pre-defined logging configs that can be imported and added to a `assemble_dictconfig()` call."""

from __future__ import annotations

from . import third_party
from .third_party.red_log_logging import (
    get_red_log_console_handler,
    get_red_log_formatter,
    get_red_log_logger,
)
