## https://medium.com/geekculture/create-a-reusable-logger-factory-for-python-projects-419ad408665d

import logging
import logging.handlers
from logging.config import dictConfig

import red_log
from pathlib import Path


# class LoggerFactory:
#     _LOG: logging.Logger | None = None

#     @staticmethod
#     def __create_logger(
#         name: str,
#         log_level: str,
#         formatters: list[logging.Formatter] = None,
#         handlers: list[logging.Handler] = None,
#     ) -> logging.Logger:
#         """Internal class method to handle creating a logger."""
#         log_level = log_level.upper()

#         # Initialize class variable with a logger object
#         LoggerFactory._LOG = logging.getLogger(name)
#         LoggerFactory._LOG.setLevel(log_level)

#         # Clear any existing handlers to avoid duplicates
#         for handler in LoggerFactory._LOG.handlers:
#             LoggerFactory._LOG.removeHandler(handler)

#         # Set formatters and handlers
#         if formatters:
#             for formatter in formatters:
#                 for handler in handlers:
#                     handler.setFormatter(formatter)
#                     LoggerFactory._LOG.addHandler(handler)

#         return LoggerFactory._LOG

#     @staticmethod
#     def get_logger(
#         name: str,
#         log_level: str,
#         formatters: list[logging.Formatter] = None,
#         handlers: list[logging.Handler] = None,
#     ) -> logging.Logger:
#         """Initialize a logger."""
#         logger = LoggerFactory.__create_logger(
#             name=name, log_level=log_level, formatters=formatters, handlers=handlers
#         )

#         return logger


# file_formatter = logging.Formatter(
#     fmt=red_log.DEFAULT_FMT, datefmt=red_log.DEFAULT_DATE_FMT
# )
# file_handler = logging.handlers.RotatingFileHandler(
#     "app.log", maxBytes=10240, backupCount=3
# )
# file_handler.setLevel(logging.DEBUG)
# file_handler.setFormatter(red_log.DEFAULT_FMT)

# ## Initilize logger
# log = LoggerFactory.get_logger(
#     name=__name__,
#     log_level="debug",
#     formatters=[file_formatter],
#     handlers=[file_handler],
# )

# log.debug("Test DEBUG")
# log.info("Test INFO")

# ---


class LoggerFactory:
    _LOG: logging.Logger | None = None

    @staticmethod
    def __create_logger(
        name: str,
        log_level: str,
        handlers: dict[str, dict],
        formatters: dict[str, dict],
        loggers: dict[str, dict],
    ) -> logging.Logger:
        """Internal class method to handle creating a logger."""
        log_level = log_level.upper()

        # Configure logging using dictConfig
        logging_config = {
            "version": 1,
            "handlers": handlers,
            "formatters": formatters,
            "loggers": loggers,
            "root": {
                "level": log_level,
                "handlers": list(handlers.keys()),
            },
        }

        dictConfig(logging_config)

        # Get or create logger
        LoggerFactory._LOG = logging.getLogger(name)

        return LoggerFactory._LOG

    @staticmethod
    def get_logger(
        name: str,
        log_level: str,
        handlers: dict[str, dict],
        formatters: dict[str, dict],
        loggers: dict[str, dict],
    ) -> logging.Logger:
        """Initialize a logger."""
        logger = LoggerFactory.__create_logger(
            name=name,
            log_level=log_level,
            handlers=handlers,
            formatters=formatters,
            loggers=loggers,
        )

        return logger


# Define formatters dictionary
formatters = {
    "console_formatter": {
        "format": red_log.DEFAULT_FMT,
        "datefmt": red_log.DEFAULT_DATE_FMT,
    },
    "file_formatter": {
        "format": red_log.DEFAULT_FMT,
        "datefmt": red_log.DEFAULT_DATE_FMT,
    },
}

# Define handlers dictionary
handlers = {
    "console_handler": {
        "class": "logging.StreamHandler",
        "level": "DEBUG",
        "formatter": "console_formatter",
    },
    "file_handler": {
        "class": "logging.handlers.RotatingFileHandler",
        "level": "DEBUG",
        "formatter": "file_formatter",
        "filename": "app.log",
        "maxBytes": 10240,
        "backupCount": 3,
    },
}

# Define loggers dictionary
loggers = {
    "": {  # Root logger
        "level": "DEBUG",
        "handlers": ["console_handler", "file_handler"],
    }
}

# Initialize logger
logger = LoggerFactory.get_logger(
    name=__name__,
    log_level="DEBUG",
    handlers=handlers,
    formatters=formatters,
    loggers=loggers,
)

logger.debug("Test DEBUG")
logger.info("Test INFO")
