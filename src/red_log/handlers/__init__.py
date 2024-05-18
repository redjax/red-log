from __future__ import annotations

from ._preconfigured_handlers import (
    APP_FILE_HANDLER,
    CLI_CONSOLE_HANDLER,
    CONSOLE_HANDLER,
    ERR_FILE_HANDLER,
    ROTATING_FILE_HANDLER,
    TIMED_ROTATING_FILE_HANDLER,
)
from ._handlers import get_handler
