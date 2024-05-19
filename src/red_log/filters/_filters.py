from dataclasses import dataclass
import logging

from red_log.base import BaseLoggingConfig


@dataclass
class FilterConfig(BaseLoggingConfig):
    name: str
    func: callable

    def get_filter(self) -> logging.Filter:
        filter_obj = logging.Filter(name=self.name)
        filter_obj.filter = self.func
        return filter_obj
