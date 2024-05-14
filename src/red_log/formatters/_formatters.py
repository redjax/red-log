from __future__ import annotations

import logging
from red_log.core.constants import DEFAULT_DATE_FMT, DEFAULT_FMT

DEFAULT_LOG_FORMATTER: dict = {
    "default": {
        "format": DEFAULT_FMT,
        "datefmt": DEFAULT_DATE_FMT,
    }
}

## Only timestamp and message
TS_MSG: dict = {"ts_msg": {"format": "[%(asctime)s]: %(message)s"}}

## Only level and message
LEVEL_MSG: dict = {"level_msg": {"format": "[%(levelname)s]"}}
