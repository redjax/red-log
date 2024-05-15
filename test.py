from red_log.core import DEFAULT_FMT, DEFAULT_DATE_FMT

CONFIG_BASE_DICT: dict = {
    "version": 1,
    "disable_existing_loggers": False,
    "propagate": True,
    "root": {},
    "formatters": {},
    "handlers": {},
    "loggers": {},
}

# "format": "[%(asctime)s] [%(levelname)s] > [%(filename)s:%(lineno)d] [%(funcName)s]: %(message)s",
# "datefmt": "%Y-%m-%d %H:%M:%S"


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
    def __init__(self):
        pass


class LoggingLogger:
    def __init__(self):
        pass


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
        assert formatter, ValueError("Missing a LoggingFormatter or dict object")

        if isinstance(formatter, LoggingFormatter):
            formatter: dict = formatter.get_formatter_dict()
        elif isinstance(formatter, dict):
            pass

        self.config_dict["formatters"]

    def get_config_dict(self) -> dict:
        _dict = self.config_dict

        for _formatter in self.formatters:
            _dict["formatters"] |= _formatter.get_formatter_dict()

        return _dict


logconfig_formatter_obj = LoggingFormatter()
logconfig_formatter_dict = logconfig_formatter_obj.get_formatter_dict()

print(f"Logging formatter: {logconfig_formatter_dict}")

logconfig_obj = LoggingConfig(
    formatters=[
        logconfig_formatter_obj,
        # LoggingFormatter(name="test", fmt="%(asctime)s %(levelname)s: %(message)s"),
    ]
)
log_conf = logconfig_obj.get_config_dict()
print(f"Logging configuration: {log_conf}")
