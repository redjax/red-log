import typing as t
from dataclasses import dataclass, field

from red_log.base import BaseHandlerConfig, BaseLoggingConfig
from red_log.formatters import FormatterConfig
from red_log.loggers import LoggerConfig
from red_log.handlers import (
    FileHandlerConfig,
    QueueHandlerConfig,
    SocketHandlerConfig,
    StreamHandlerConfig,
    RotatingFileHandlerConfig,
    TimedRotatingFileHandlerConfig,
    SMTPHandlerConfig,
    QueueListenerConfig,
)


@dataclass
class LoggingConfig:
    """Assemble a logging configdict from input handlers, formatters, and loggers."""

    version: int = 1
    disable_existing_loggers: bool = False
    propagate: bool = True
    # root: dict = field(default_factory=dict)
    formatters: dict = field(default_factory=dict)
    handlers: dict = field(default_factory=dict)
    loggers: dict = field(default_factory=dict)

    ## Root logger config overrides
    root_level: str = "WARNING"
    root_formatter: str = "[%(levelname)s][%(filename)s:%(lineno)d]: %(message)s"
    root_datefmt: str = "%Y-%m-%d %H:%M:%S"
    root_handlers: list = field(default_factory=lambda: ["root_console"])

    def add_formatters(self, formatter_configs: list[FormatterConfig]):
        for formatter in formatter_configs:
            self.formatters.update(formatter.get_configdict())

    def add_handlers(self, handler_configs: list[BaseHandlerConfig]):
        for handler in handler_configs:
            self.handlers.update(handler.get_configdict())

    def add_loggers(self, logger_configs: list[LoggerConfig]):
        for logger in logger_configs:
            self.loggers.update(logger.get_configdict())

    def get_config(self) -> dict:
        root_formatter_config = FormatterConfig(
            name="root_formatter", fmt=self.root_formatter, datefmt=self.root_datefmt
        )
        root_handler_config = StreamHandlerConfig(
            name="root_console",
            level="DEBUG",
            formatter="root_formatter",
            stream="ext://sys.stdout",
        )

        # Add root formatter and handler configs
        self.add_formatters([root_formatter_config])
        self.add_handlers([root_handler_config])

        # Define the root logger configuration
        root_logger_config = LoggerConfig(
            name="",
            level=self.root_level,
            handlers=["root_console"],
            propagate=self.propagate,
        )

        # Add root logger config
        self.add_loggers([root_logger_config])

        # Assemble the complete logging configuration
        return {
            "version": self.version,
            "disable_existing_loggers": self.disable_existing_loggers,
            "propagate": self.propagate,
            "root": root_logger_config.get_configdict(),
            "formatters": self.formatters,
            "handlers": self.handlers,
            "loggers": self.loggers,
        }
