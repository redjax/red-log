from dataclasses import dataclass

from red_log.base import BaseLoggingConfig
from red_log.constants import DEFAULT_FMT, DEFAULT_DATE_FMT, DEFAULT_LOGGER_STYLE


@dataclass
class FormatterConfig(BaseLoggingConfig):
    name: str = None
    fmt: str = DEFAULT_FMT
    datefmt: str = DEFAULT_DATE_FMT
    style: str = DEFAULT_LOGGER_STYLE
    validate: bool = True

    def get_configdict(self) -> dict[str, dict[str, str]]:
        formatter_dict: dict[str, dict[str, str]] = {self.name: {"fmt": self.fmt}}
        if self.datefmt:
            formatter_dict[self.name]["datefmt"] = self.datefmt
        if self.style:
            formatter_dict[self.name]["style"] = self.style
        formatter_dict[self.name]["validate"] = self.validate
        return formatter_dict
