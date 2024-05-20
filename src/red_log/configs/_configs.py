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
        return {
            "version": self.version,
            "disable_existing_loggers": self.disable_existing_loggers,
            "propagate": self.propagate,
            "formatters": self.formatters,
            "handlers": self.handlers,
            "loggers": self.loggers,
        }
