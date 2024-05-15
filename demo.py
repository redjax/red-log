# from __future__ import annotations

import json

# import logging

import red_log

# red_log.configure_root_logger(
#     dict_config=red_log.DEFAULT_LOGGING_CONFIG, logger_name=__name__
# )
# log: logging.Logger = logging.getLogger(__name__)


# if __name__ == "__main__":
#     red_log.utils.test_log_messages()

import logging.config
from red_log.class_handlers import LogConfig, RootLogConfig
from red_log.core.constants import DEFAULT_DATE_FMT

logging.config.dictConfig(RootLogConfig().get_config())

# log: logging.config.Logger = LogConfig(name=__name__, level="INFO").get_logger()


# log.debug("Test DEBUG")
# log.info("Test INFO")
# log.warning("Test WARNING")
# log.error("Test ERROR")
# log.critical("Test CRITICAL")

# try:
#     1 / 0
# except ZeroDivisionError as exc:
#     msg = Exception(f"Unhandled exception dividing number. Details: {exc}")
#     log.critical(msg)


# with open("logging_config_ex.json", "w") as f:
#     _data = json.dumps(red_log.DEFAULT_LOGGING_CONFIG)
#     f.write(_data)
