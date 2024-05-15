from __future__ import annotations

DEFAULT_FMT: str = (
    "[%(asctime)s] [%(levelname)s] > [%(filename)s:%(lineno)d] [%(funcName)s]: %(message)s"
)

DEFAULT_DATE_FMT: str = "%Y-%m-%d %H:%M:%S"

VALID_LOG_LEVELS: str = ["NOTSET", "DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]
