import typing as t
import logging
from typing import Optional

import red_log


class LoggerFactory:
    def __init__(self, name: str, level: int = logging.INFO):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(level)

    def add_handler(self, handler: logging.Handler):
        self.logger.addHandler(handler)

    def get_logger(self) -> logging.Logger:
        return self.logger


class HandlerFactory:
    @staticmethod
    def create_stream_handler(
        level: t.Union[int, str] = logging.INFO,
        formatter: Optional[logging.Formatter] = None,
    ) -> logging.StreamHandler:
        level = HandlerFactory._get_log_level(level)
        handler = logging.StreamHandler()
        handler.setLevel(level)
        if formatter:
            handler.setFormatter(formatter)
        return handler

    @staticmethod
    def create_file_handler(
        filename: str,
        level: t.Union[int, str] = logging.INFO,
        formatter: Optional[logging.Formatter] = None,
    ) -> logging.FileHandler:
        level = HandlerFactory._get_log_level(level)
        handler = logging.FileHandler(filename)
        handler.setLevel(level)
        if formatter:
            handler.setFormatter(formatter)
        return handler

    @staticmethod
    def _get_log_level(level: t.Union[int, str]) -> int:
        if isinstance(level, str):
            level = level.upper()
            return logging._nameToLevel.get(level, logging.INFO)
        return level


class FormatterFactory:
    @staticmethod
    def create_formatter(
        fmt: str = red_log.constants.DEFAULT_FMT,
        date_fmt: str = red_log.constants.DEFAULT_DATE_FMT,
        style: str = red_log.constants.DEFAULT_LOGGER_STYLE,
        validate: bool = True,
    ) -> logging.Formatter:
        return logging.Formatter(
            fmt=fmt, datefmt=date_fmt, style=style, validate=validate
        )


if __name__ == "__main__":
    # Create a formatter
    simple_formatter = FormatterFactory.create_formatter()

    # Create a stream handler
    stream_handler = HandlerFactory.create_stream_handler(
        level=logging.DEBUG, formatter=simple_formatter
    )

    # Create a logger
    logger_factory = LoggerFactory(name=__name__, level="DEBUG")
    logger_factory.add_handler(stream_handler)
    logger = logger_factory.get_logger()

    # Log some messages
    logger.debug("This is a debug message")
    logger.info("This is an info message")
    logger.warning("This is a warning message")
    logger.error("This is an error message")
    logger.critical("This is a critical message")
