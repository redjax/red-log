from red_log.core import DEFAULT_FMT, DEFAULT_DATE_FMT
import logging
from logging.config import dictConfig

CONFIG_BASE_DICT: dict = {
    "version": 1,
    "disable_existing_loggers": False,
    "propagate": True,
    "root": {},
    "formatters": {},
    "handlers": {},
    "loggers": {},
}


class LoggingFormatter:
    def __init__(
        self,
        name: str = "default",
        fmt: str = DEFAULT_FMT,
        datefmt: str = DEFAULT_DATE_FMT,
    ):
        self.name = name
        self.fmt = fmt
        self.datefmt = datefmt

    def get_formatter_dict(self) -> dict:
        _dict = {self.name: {"format": self.fmt, "datefmt": self.datefmt}}

        return _dict


class LoggingHandler:
    def __init__(
        self,
        name: str = "console",
        class_name: str = "logging.StreamHandler",
        formatter_name: str = "default",
        level: str = "DEBUG",
        stream: str = "ext://sys.stdout",
    ):
        self.name = name
        self.class_name = class_name
        self.formatter_name = formatter_name
        self.level = level.upper()
        self.stream = stream

    def get_handler_dict(self) -> dict:
        _dict = {
            self.name: {
                "class": self.class_name,
                "formatter": self.formatter_name,
                "level": self.level,
                "stream": self.stream,
            }
        }

        return _dict


class LoggingLogger:
    def __init__(
        self,
        logger_name: str = "",
        handler_names: list[str] = ["console"],
        level_name: str = "NOTSET",
    ):
        self.name = logger_name
        self.handlers = handler_names
        self.level = level_name.upper()

    def get_logger_dict(self) -> dict:
        _dict = {self.name: {"handlers": self.handlers, "level": self.level}}

        return _dict


class LoggingConfig:
    def __init__(
        self,
        version: int = 1,
        disable_existing_loggers: bool = False,
        propagate: bool = True,
        root: dict = {},
        formatters: list[LoggingFormatter] = [{}],
        handlers: list[LoggingHandler] = [{}],
        loggers: list[LoggingLogger] = [{}],
    ):
        self.version = version
        self.disable_existing_loggers = disable_existing_loggers
        self.propagate = propagate
        self.root = root
        self.formatters = formatters
        self.handlers = handlers
        self.loggers = loggers

        self.config_dict = {
            "version": 1,
            "disable_existing_loggers": self.disable_existing_loggers,
            "propagate": self.propagate,
            "root": {},
            "formatters": {},
            "handlers": {},
            "loggers": {},
        }

    def add_formatter(self, formatter: LoggingFormatter | dict = None):
        """Add a new log formatter to the config."""

        assert formatter, ValueError("Missing a LoggingFormatter or dict object")

        if isinstance(formatter, LoggingFormatter):
            formatter: dict = formatter.get_formatter_dict()
        elif isinstance(formatter, dict):
            pass
        else:
            raise TypeError(
                f"Invalid type for formatter: ({type(formatter)}). Must be a LoggingFormatter or dict object."
            )

        self.config_dict["formatters"] |= formatter

    def add_handler(self, handler: LoggingHandler | dict = None):
        """Add a new log handler to the config."""

        assert handler, ValueError("Missing a LoggingHandler or dict object")

        if isinstance(handler, LoggingHandler):
            handler: dict = handler.get_handler_dict()
        elif isinstance(handler, dict):
            pass
        else:
            raise TypeError(
                f"Invalid type for handler: ({type(handler)}). Must be a LoggingHandler or dict object."
            )

        self.config_dict["handlers"] |= handler

    def add_logger(self, logger: LoggingLogger | dict = None):
        """Add a new logger config."""

        assert logger, ValueError("Missing a LoggingLogger or dict object")

        if isinstance(logger, LoggingLogger):
            logger: dict = logger.get_logger_dict()
        elif isinstance(logger, dict):
            pass
        else:
            raise TypeError(
                f"Invalid type for logger: ({type(logger)}). Must be a LoggingLogger or dict object."
            )

        self.config_dict["loggers"] |= logger

    def get_config_dict(self) -> dict:
        """Return an initialized logging config dict object for this class."""

        for _formatter in self.formatters:
            self.add_formatter(formatter=_formatter)

        for _handler in self.handlers:
            self.add_handler(handler=_handler)

        for _logger in self.loggers:
            self.add_logger(logger=_logger)

        return self.config_dict


logconfig_obj = LoggingConfig(
    formatters=[
        LoggingFormatter(),
        # LoggingFormatter(name="test", fmt="%(asctime)s %(levelname)s: %(message)s"),
    ],
    handlers=[LoggingHandler()],
    loggers=[LoggingLogger(level_name="warning")],
)
log_conf = logconfig_obj.get_config_dict()
print(f"Logging configuration: {log_conf}")

dictConfig(log_conf)
log = logging.getLogger(__name__)

log.debug("Test DEBUG")
log.info("Test INFO")
log.warning("Test WARNING")
