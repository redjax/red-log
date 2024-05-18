from __future__ import annotations

import logging
import logging.handlers
from enum import Enum

from .validators import VALID_HANDLER_CLASSES


class HandlerObjectsEnum(Enum):
    """Return a logging.Handler class matching an input string.

    Note that enum keys are uppercase versions of the logging.Handler, without the "Handler" at the end. For example,
    FILE = logging.FILEHANDLER

    Usage:
        ```python title="HandlerObjectsEnum usage" linenums="1"

        ## Note that you do not retrieve the enum value with `.value`. Instead, return the handler directly.
        stream_handler = HandlerObjectsEnum["STREAM"]
        ```
    """

    FILE: logging.Handler = logging.FileHandler
    ROTATINGFILE: logging.Handler = logging.handlers.RotatingFileHandler
    TIMEBASEDROTATINGFILE: logging.Handler = logging.handlers.TimedRotatingFileHandler
    QUEUE: logging.Handler = logging.handlers.QueueHandler
    QUEUELISTENER: logging.Handler = logging.handlers.QueueListener
    NULL: logging.Handler = logging.NullHandler
    STREAM: logging.Handler = logging.StreamHandler
    SYSLOG: logging.Handler = logging.handlers.SysLogHandler
    SMTP: logging.Handler = logging.handlers.SMTPHandler
    BUFFERING: logging.Handler = logging.handlers.BufferingHandler
    DATAGRAM: logging.Handler = logging.handlers.DatagramHandler
    HTTP: logging.Handler = logging.handlers.HTTPHandler
    MEMORY: logging.Handler = logging.handlers.MemoryHandler
    NTEVENTLOG: logging.Handler = logging.handlers.NTEventLogHandler
    SOCKET: logging.Handler = logging.handlers.SocketHandler
    WATCHEDFILE: logging.Handler = logging.handlers.WatchedFileHandler


def __handler_dict() -> dict:
    pass


def __handler_obj() -> logging.Handler:
    pass


def get_handler(
    name: str | None = "default",
    handler_class: str | None = "stream",
    formatter_name: str = "default",
    log_level: str = "NOTSET",
    stream: str | None = "ext://sys.stdout",
    filename: str | None = "app.log",
    max_bytes: int = 2000000,
    backup_count: int = 3,
    as_dict: bool = False,
) -> dict | logging.Handler:
    # Normalize handler_class to uppercase
    handler_class = handler_class.upper() if handler_class else "STREAM"

    # Ensure the handler_class is valid
    try:
        handler_enum = HandlerObjectsEnum[handler_class]
    except KeyError:
        raise ValueError(f"Invalid handler_class: {handler_class}")

    handler_cls = handler_enum.value

    if as_dict:
        assert name, ValueError("When as_dict=True, a handler name must be given.")
        # Create the dict configuration for the handler
        handler_config = {
            name: {
                "class": f"{handler_cls.__module__}.{handler_cls.__name__}",
                "level": log_level,
                "formatter": formatter_name,
            }
        }
        if handler_cls in (
            logging.FileHandler,
            logging.handlers.RotatingFileHandler,
            logging.handlers.TimedRotatingFileHandler,
            logging.handlers.WatchedFileHandler,
        ):
            assert filename, ValueError(
                "When requesting a file handler, a filename must be given."
            )
            handler_config["filename"] = filename
        if handler_cls == logging.handlers.RotatingFileHandler:
            assert filename, ValueError(
                "When requesting a rotating file handler, a filename must be given."
            )
            handler_config["maxBytes"] = max_bytes
            handler_config["backupCount"] = backup_count
        if handler_cls == logging.StreamHandler:
            handler_config["stream"] = stream

        return handler_config
    else:
        # Initialize and return the handler instance
        if handler_cls == logging.FileHandler:
            handler = handler_cls(filename, mode="a")
        elif handler_cls == logging.handlers.RotatingFileHandler:
            handler = handler_cls(
                filename, maxBytes=max_bytes, backupCount=backup_count
            )
        elif handler_cls == logging.StreamHandler:
            handler = handler_cls(stream=stream)
        else:
            # Handle other handler classes that may need specific parameters
            handler = handler_cls()

        # Set the log level for the handler
        handler.setLevel(log_level.upper())
        return handler
