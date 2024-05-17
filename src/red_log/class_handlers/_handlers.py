import logging
from logging.config import dictConfig
from logging import StreamHandler, Handler, FileHandler, NullHandler
import logging.config

from red_log.constants import DEFAULT_DATE_FMT, DEFAULT_FMT, LogLevels

log: logging.Logger = logging.getLogger("red_log")


def get_config_dict(
    name: str = None,
    level: str = "WARNING",
    disable_existing_loggers: bool = False,
    propagate: bool = True,
    extra_formatters: list[dict] | None = None,
    extra_handlers: list[dict] | None = None,
) -> dict:

    level: str = str(level).upper()

    cfg: dict = {
        "version": 1,
        "disable_existing_loggers": disable_existing_loggers,
        "propagate": propagate,
        # "root": {"": {"handlers": ["console"], "level": "WARNING"}},
        "formatters": {
            f"{name}_default": {
                "format": "[%(asctime)s] [%(levelname)s] > [%(filename)s:%(lineno)d] [%(funcName)s]: %(message)s",
                "datefmt": "[%(asctime)s]: %(message)s",
            }
        },
        "handlers": {
            f"{name}_console": {
                "class": "logging.StreamHandler",
                "formatter": f"{name}_default",
                "level": "DEBUG",
                "stream": "ext://sys.stdout",
            }
        },
        # "loggers": {"": {"handlers": ["console"], "level": "WARNING"}},
        "logggers": {name: {"level": level, "handlers": [f"{name}_console"]}},
    }

    return cfg


class LogConfig:

    def __init__(
        self,
        name: str,
        level: str = "NOTSET",
        fmt: str = DEFAULT_FMT,
        datefmt: str = DEFAULT_DATE_FMT,
        disable_existing_loggers: bool = False,
        propagate: bool = True,
    ):
        if name == "__main__":
            self.name = "main"
        else:
            self.name = name
        self.level = LogLevels[level.upper()]
        # self.level = level.upper()
        self.fmt = fmt
        self.datefmt = datefmt
        self.disable_existing_loggers = disable_existing_loggers
        self.propagate = propagate

    def get_logger(
        self,
        extra_formatters: list[dict] | None = None,
        extra_handlers: list[dict] | None = None,
    ) -> logging.Logger:
        try:
            cfg: dict = get_config_dict(
                name=self.name,
            )
        except Exception as exc:
            msg = Exception(
                f"Unhandled exception getting logger config dict. Details: {exc}"
            )
            log.error(msg)
            log.warning("Error getting configuration dict")

        try:
            dictConfig(cfg)
        except Exception as exc:
            msg = Exception(
                f"Unhandled exception configuring logger '{self.name}'. Details: {exc}"
            )
            log.error(msg)
            log.warning(f"Error configuring logger '{self.name}'.")

        return logging.getLogger(self.name)


class RootLogConfig:
    def __init__(
        self,
        level: str = "NOTSET",
        propagate: bool = True,
        disable_existing_loggers: bool = False,
    ) -> None:
        self.name = ""
        # self.level = LogLevels[level.upper()].value
        self.level = level.upper()
        self.propagate = propagate
        self.disable_existing_loggers = disable_existing_loggers

    @property
    def cfg(self) -> dict:
        """Store root config"""
        cfg: dict = {
            "version": 1,
            "disable_existing_loggers": self.disable_existing_loggers,
            "propagate": self.propagate,
            # "root": {"": {"handlers": ["console"], "level": "WARNING"}},
            "formatters": {
                f"default": {
                    "format": DEFAULT_FMT,
                    "datefmt": DEFAULT_DATE_FMT,
                }
            },
            "handlers": {
                f"console": {
                    "class": "logging.StreamHandler",
                    "formatter": "default",
                    "level": "DEBUG",
                    "stream": "ext://sys.stdout",
                }
            },
            "loggers": {"": {"handlers": ["console"], "level": self.level}},
        }

        return cfg

    def get_config(self) -> dict:
        """Get root logger config"""
        return self.cfg

    def get_logger(self) -> logging.Logger:
        """Get root logger"""
        cfg: dict = self.get_config()

        dictConfig(cfg)

        return logging.getLogger(self.name)
