import typing as t
from dataclasses import dataclass, field
from queue import Queue

from red_log.base import BaseHandlerConfig, BaseLoggingConfig


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
