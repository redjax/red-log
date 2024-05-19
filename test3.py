from __future__ import annotations
import typing as t

from queue import Queue

from dataclasses import dataclass, asdict, field
from abc import ABC, abstractmethod

import logging
import logging.handlers
import logging.config


@dataclass
class BaseLoggingConfig(ABC):
    @abstractmethod
    def get_configdict(self) -> None:
        pass


@dataclass
class FilterConfig(BaseLoggingConfig):
    name: str
    func: callable

    def get_filter(self) -> logging.Filter:
        filter_obj = logging.Filter(name=self.name)
        filter_obj.filter = self.func
        return filter_obj


@dataclass
class FormatterConfig(BaseLoggingConfig):
    name: str
    fmt: str
    datefmt: str = None
    style: str = "%"
    validate: bool = True

    def get_configdict(self) -> dict[str, dict[str, str]]:
        formatter_dict: dict[str, dict[str, str]] = {self.name: {"fmt": self.fmt}}
        if self.datefmt:
            formatter_dict[self.name]["datefmt"] = self.datefmt
        if self.style:
            formatter_dict[self.name]["style"] = self.style
        formatter_dict[self.name]["validate"] = self.validate
        return formatter_dict


@dataclass
class BaseHandlerConfig(BaseLoggingConfig):
    name: str = None
    level: str = "NOTSET"
    formatter: str = None
    filters: list | None = field(default=None)

    @abstractmethod
    def get_configdict(self) -> None:
        handler_dict: dict[str, dict[str, t.Any]] = {
            self.name: {
                "class": self.get_handler_class(),
                "level": self.level,
                "formatter": self.formatter,
            }
        }
        if self.filters:
            handler_dict[self.name]["filters"] = self.filters
        return handler_dict

    def get_handler_class(self) -> str:
        raise NotImplementedError("Subclasses must implement get_handler_class method")


@dataclass
class StreamHandlerConfig(BaseHandlerConfig):
    stream: t.Any | None = "ext://sys.stdout"

    def get_configdict(self) -> dict[str, dict[str, str]]:
        handler_dict: dict[str, dict[str, str]] = {
            self.name: {
                "class": self.get_handler_class(),
                "level": self.level,
                "formatter": self.formatter,
                "stream": self.stream,
            }
        }
        if self.filters:
            handler_dict["filters"] = self.filters
        return handler_dict

    def get_handler_class(self) -> str:
        return "logging.StreamHandler"


@dataclass
class FileHandlerConfig(BaseHandlerConfig):
    filename: str | None = field(default="app.log")

    def get_configdict(self) -> dict[str, dict[str, str]]:
        handler_dict: dict[str, dict[str, str]] = {
            self.name: {
                "class": self.get_handler_class(),
                "level": self.level,
                "formatter": self.formatter,
                "filename": self.filename,
            }
        }
        return handler_dict

    def get_handler_class(self) -> str:
        return "logging.FileHandler"


@dataclass
class RotatingFileHandlerConfig(BaseHandlerConfig):
    filename: str | None = field(default="app.log")
    maxBytes: int = 0
    backupCount: int = 0

    def get_configdict(self) -> dict[str, dict[str, t.Any]]:
        handler_dict: dict[str, dict[str, t.Any]] = {
            self.name: {
                "class": self.get_handler_class(),
                "level": self.level,
                "formatter": self.formatter,
                "filename": self.filename,
                "maxBytes": self.maxBytes,
                "backupCount": self.backupCount,
            }
        }
        return handler_dict

    def get_handler_class(self) -> str:
        return "logging.handlers.RotatingFileHandler"


@dataclass
class TimedRotatingFileHandlerConfig(BaseHandlerConfig):
    filename: str | None = field(default="app.log")
    when: str | None = field(default="midnight")
    interval: int = 1
    backupCount: int = 0

    def get_configdict(self) -> dict[str, dict[str, t.Any]]:
        handler_dict: dict[str, dict[str, t.Any]] = {
            self.name: {
                "class": self.get_handler_class(),
                "level": self.level,
                "formatter": self.formatter,
                "filename": self.filename,
                "when": self.when,
                "interval": self.interval,
                "backupCount": self.backupCount,
            }
        }
        return handler_dict

    def get_handler_class(self) -> str:
        return "logging.handlers.TimedRotatingFileHandler"


@dataclass
class SocketHandlerConfig(BaseHandlerConfig):
    host: str = "localhost"
    port: int = 0

    def get_configdict(self) -> dict[str, dict[str, t.Any]]:
        handler_dict: dict[str, dict[str, t.Any]] = {
            self.name: {
                "class": self.get_handler_class(),
                "level": self.level,
                "formatter": self.formatter,
                "host": self.host,
                "port": self.port,
            }
        }
        return handler_dict

    def get_handler_class(self) -> str:
        return "logging.handlers.SocketHandler"


@dataclass
class SMTPHandlerConfig(BaseHandlerConfig):
    mailhost: t.Any = None
    fromaddr: str = "from@example.com"
    toaddrs: list = field(default_factory=lambda: [])
    subject: str = "SMTPHandler Log Event"
    credentials: tuple | None = None
    secure: tuple | None = None

    def get_configdict(self):
        handler_dict = {
            self.name: {
                "class": self.get_handler_class(),
                "level": self.level,
                "formatter": self.formatter,
                "mailhost": self.mailhost,
                "fromaddr": self.fromaddr,
                "toaddrs": self.toaddrs,
                "subject": self.subject,
            }
        }
        if self.credentials:
            handler_dict[self.name]["credentials"] = self.credentials
        if self.secure:
            handler_dict[self.name]["secure"] = self.secure
        return handler_dict

    def get_handler_class(self) -> str:
        return "logging.handlers.SMTPHandler"


@dataclass
class QueueHandlerConfig(BaseHandlerConfig):
    queue: Queue = field(default=None)

    def get_configdict(self) -> dict[str, dict[str, t.Any]]:
        handler_dict: dict[str, dict[str, t.Any]] = {
            self.name: {
                "class": self.get_handler_class(),
                "level": self.level,
                "formatter": self.formatter,
                "queue": self.queue,
            }
        }
        return handler_dict

    def get_handler_class(self) -> str:
        return "logging.handlers.QueueHandler"


@dataclass
class QueueListenerConfig(BaseLoggingConfig):
    name: str
    queue: Queue
    handlers: list

    def get_configdict(self) -> dict[str, dict[str, t.Any]]:
        listener_dict: dict[str, dict[str, t.Any]] = {
            self.name: {
                "class": self.get_handler_class(),
                "queue": self.queue,
                "handlers": self.handlers,
            }
        }
        return listener_dict

    def get_handler_class(self) -> str:
        return "logging.handleres.QueueListener"


@dataclass
class LoggerConfig(BaseLoggingConfig):
    name: str
    level: str
    handlers: list
    propagate: bool = True

    def get_configdict(self) -> dict:
        logger_dict: dict[str, dict[str, t.Any]] = {
            self.name: {
                "level": self.level,
                "handlers": self.handlers,
                "propagate": self.propagate,
            }
        }
        return logger_dict


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


BASE_LOGGING_CONFIG_DICT: dict = {
    "version": 1,
    "disable_existing_loggers": False,
    "propagate": True,
    "root": {},
    "formatters": {},
    "handlers": {},
    "loggers": {},
}


def error_filter(record: logging.LogRecord):
    """Filter to only show ERROR and above."""
    return record.levelno >= logging.ERROR


if __name__ == "__main__":
    formatter = FormatterConfig(
        name="simple",
        fmt="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )
    formatter_config: dict[str, dict[str, str]] = formatter.get_configdict()

    stream_handler = StreamHandlerConfig(
        name="console", level="DEBUG", formatter="simple", stream=None
    )
    file_handler = FileHandlerConfig(
        name="file", level="INFO", formatter="simple", filename="app.log"
    )
    err_file_handler = FileHandlerConfig(
        name="err_file",
        level="ERROR",
        formatter="simple",
        filename="err.log",
        filters=["error_filter"],
    )
    rotating_file_handler = RotatingFileHandlerConfig(
        name="rotating_file",
        level="WARNING",
        formatter="simple",
        filename="app.log",
        maxBytes=1024 * 1024,
        backupCount=5,
    )
    timed_rotating_file_handler = TimedRotatingFileHandlerConfig(
        name="timed_rotating_file",
        level="ERROR",
        formatter="simple",
        filename="timed_app.log",
        when="midnight",
        interval=1,
        backupCount=7,
    )
    socket_handler = SocketHandlerConfig(
        name="socket_handler",
        level="DEBUG",
        formatter="simple",
        host="localhost",
        port=1234,
    )
    smtp_handler = SMTPHandlerConfig(
        name="smtp",
        level="CRITICAL",
        formatter="simple",
        mailhost=("localhost", 25),
        fromaddr="from@example.com",
        toaddrs=["to@example.com"],
        subject="Critical Error",
        credentials=("user", "password"),
        secure=None,
    )

    ## Initialize a queue for queue handler
    queue = Queue()
    queue_handler = QueueHandlerConfig(
        name="queue", level="DEBUG", formatter="simple", queue=queue
    )
    queue_listener = QueueListenerConfig(
        name="queue_listener", queue=queue, handlers=["file", "console"]
    )

    custom_console_handler = StreamHandlerConfig(
        name="console_custom", formatter="simple"
    )

    custom_logger = LoggerConfig(
        name="custom",
        level="DEBUG",
        handlers=["console_custom"],
    )

    logging_config = LoggingConfig()
    logging_config.add_formatters([formatter])
    logging_config.add_handlers(
        [
            stream_handler,
            file_handler,
            rotating_file_handler,
            timed_rotating_file_handler,
            socket_handler,
            smtp_handler,
            queue_handler,
            custom_console_handler,
        ]
    )
    logging_config.add_loggers([custom_logger])

    # print(f"Logging config: {logging_config.get_config()}")

    logging.config.dictConfig(logging_config.get_config())
    log = logging.getLogger("custom")

    log.debug("Test DEBUG")
    log.info("Test INFO")
    log.warning("Test WARNING")
    log.error("Test ERROR")
    log.critical("Test CRITICAL")
