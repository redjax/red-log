## https://medium.com/geekculture/create-a-reusable-logger-factory-for-python-projects-419ad408665d

import logging

import red_log
from pathlib import Path


class LoggerFactory(object):
    _LOG: logging.Logger = None

    @staticmethod
    def __create_logger(name, log_level: str) -> logging.Logger:
        """Internal class method to handle creating a logger."""
        log_level: str = log_level.upper()
        ## Set logging format
        fmt = red_log.DEFAULT_FMT
        datefmt = red_log.DEFAULT_DATE_FMT

        ## Initialize class variable with a logger object
        LoggerFactory._LOG = logging.getLogger(name)
        logging.basicConfig(level=log_level, format=fmt, datefmt=datefmt)

        ## Set logging level based on user selection
        LoggerFactory._LOG.setLevel(log_level)

        return LoggerFactory._LOG

    @staticmethod
    def get_logger(name: str, log_level: str) -> logging.Logger:
        """Initialize a logger."""
        logger: logging.Logger = LoggerFactory.__create_logger(
            name=name, log_level=log_level
        )

        return logger


## Initilize logger
log = LoggerFactory.get_logger(name=__name__, log_level="debug")

log.debug("Test DEBUG")
log.info("Test INFO")
