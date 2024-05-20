import logging

from . import constants

from . import base
from . import filters
from . import formatters
from . import handlers
from . import configs
from . import loggers

from .configs import LoggingConfig

rootlogger = logging.getLogger("red_log")
if rootlogger.level == logging.NOTSET:
    rootlogger.setLevel(logging.WARN)
