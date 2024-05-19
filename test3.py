import typing as t

from queue import Queue

from dataclasses import dataclass, asdict, field
from abc import ABC, abstractmethod

import logging
import logging.handlers


@dataclass
class BaseLoggingConfig(ABC):
    @abstractmethod
    def get_configdict(self) -> None:
        pass


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
    name: str
    level: str
    formatter: str

    @abstractmethod
    def get_configdict(self) -> None:
        pass


@dataclass
class StreamHandlerConfig(BaseHandlerConfig):
    stream: t.Any | None = None

    def get_configdict(self) -> dict[str, dict[str, str]]:
        handler_dict: dict[str, dict[str, str]] = {
            self.name: {
                "class": "logging.StreamHandler",
                "level": self.level,
                "formatter": self.formatter,
            }
        }
        if self.stream is not None:
            handler_dict[self.name]["stream"] = self.stream
        return handler_dict


@dataclass
class FileHandlerConfig(BaseHandlerConfig):
    filename: str

    def get_configdict(self) -> dict[str, dict[str, str]]:
        handler_dict: dict[str, dict[str, str]] = {
            self.name: {
                "class": "logging.FileHandler",
                "level": self.level,
                "formatter": self.formatter,
                "filename": self.filename,
            }
        }
        return handler_dict


@dataclass
class RotatingFileHandlerConfig(BaseHandlerConfig):
    filename: str
    maxBytes: int = 0
    backupCount: int = 0

    def get_configdict(self) -> dict[str, dict[str, t.Any]]:
        handler_dict: dict[str, dict[str, t.Any]] = {
            self.name: {
                "class": "logging.handlers.RotatingFileHandler",
                "level": self.level,
                "formatter": self.formatter,
                "filename": self.filename,
                "maxBytes": self.maxBytes,
                "backupCount": self.backupCount,
            }
        }
        return handler_dict


@dataclass
class TimedRotatingFileHandlerConfig(BaseHandlerConfig):
    filename: str
    when: str
    interval: int = 1
    backupCount: int = 0

    def get_configdict(self) -> dict[str, dict[str, t.Any]]:
        handler_dict: dict[str, dict[str, t.Any]] = {
            self.name: {
                "class": "logging.handlers.TimedRotatingFileHandler",
                "level": self.level,
                "formatter": self.formatter,
                "filename": self.filename,
                "when": self.when,
                "interval": self.interval,
                "backupCount": self.backupCount,
            }
        }
        return handler_dict


@dataclass
class SocketHandlerConfig(BaseHandlerConfig):
    host: str
    port: int

    def get_configdict(self) -> dict[str, dict[str, t.Any]]:
        handler_dict: dict[str, dict[str, t.Any]] = {
            self.name: {
                "class": "logging.handlers.SocketHandler",
                "level": self.level,
                "formatter": self.formatter,
                "host": self.host,
                "port": self.port,
            }
        }
        return handler_dict


@dataclass
class SMTPHandlerConfig(BaseHandlerConfig):
    mailhost: t.Any
    fromaddr: str
    toaddrs: list
    subject: str
    credentials: tuple | None = None
    secure: tuple | None = None

    def get_configdict(self):
        handler_dict = {
            self.name: {
                "class": "logging.handlers.SMTPHandler",
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


@dataclass
class QueueHandlerConfig(BaseHandlerConfig):
    queue: Queue

    def get_configdict(self) -> dict[str, dict[str, t.Any]]:
        handler_dict: dict[str, dict[str, t.Any]] = {
            self.name: {
                "class": "logging.handlers.QueueHandler",
                "level": self.level,
                "formatter": self.formatter,
                "queue": self.queue,
            }
        }
        return handler_dict


@dataclass
class QueueListenerConfig(BaseLoggingConfig):
    name: str
    queue: Queue
    handlers: list

    def get_configdict(self) -> dict[str, dict[str, t.Any]]:
        listener_dict: dict[str, dict[str, t.Any]] = {
            self.name: {
                "class": "logging.handlers.QueueListener",
                "queue": self.queue,
                "handlers": self.handlers,
            }
        }
        return listener_dict


@dataclass
class LoggingConfig:
    """Assemble a logging configdict from input handlers, formatters, and loggers."""

    version: int = 1
    disable_existing_loggers: bool = False
    propagate: bool = True
    root: dict = field(default_factory=dict)
    formatters: dict = field(default_factory=dict)
    handlers: dict = field(default_factory=dict)
    loggers: dict = field(default_factory=dict)

    def add_formatters(self, formatter_configs: list[FormatterConfig]):
        for formatter in formatter_configs:
            self.formatters.update(formatter.get_configdict())

    def add_handlers(self, handler_configs: list[BaseHandlerConfig]):
        for handler in handler_configs:
            self.handlers.update(handler.get_configdict())

    def get_config(self) -> dict:
        return {
            "version": self.version,
            "disable_existing_loggers": self.disable_existing_loggers,
            "propagate": self.propagate,
            "root": self.root,
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
    rotating_file_handler = RotatingFileHandlerConfig(
        name="rotating_file",
        level="WARNING",
        formatter="formatter",
        filename="app.log",
        maxBytes=1024 * 1024,
        backupCount=5,
    )
    timed_rotating_file_handler = TimedRotatingFileHandlerConfig(
        name="timed_rotating_file",
        level="ERROR",
        formatter="formatter",
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
        formatter="detailed",
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
        name="queue", level="DEBUG", formatter="detailed", queue=queue
    )
    queue_listener = QueueListenerConfig(
        name="queue_listener", queue=queue, handlers=["file", "console"]
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
        ]
    )

    print(f"Logging config: {logging_config.get_config()}")
