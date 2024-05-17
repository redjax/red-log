from enum import Enum
import logging
from logging.config import dictConfig

import red_log
from test_mod import test_log_levels


# log.info("Running logging test")
# test_log_levels()


# dictConfig(red_log.DEFAULT_LOGGING_CONFIG)
# log = logging.getLogger("red_log")


formatter = red_log.formatters.get_formatter(as_dict=True)
print(f"Formatter ({type(formatter)}): {formatter}")


input("PAUSE")


class LogLevelIntEnum(Enum):
    """Use input string to get log level as integer value.

    Example:
            log_level: int = LogLevelIntEnum("INFO").value  # = 20
    """

    NOTSET = 0
    DEBUG = 10
    INFO = 20
    WARNING = 30
    ERROR = 40
    CRITICAL = 50


log_level = LogLevelIntEnum["INFO"]
log.debug(f"Log level: {log_level}")
