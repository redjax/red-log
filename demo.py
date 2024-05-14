from __future__ import annotations

import json
import logging

import red_log

red_log.configure_root_logger(
    dict_config=red_log.DEFAULT_LOGGING_CONFIG, logger_name=__name__
)
log: logging.Logger = logging.getLogger(__name__)
# log.setLevel(logging.DEBUG)

if __name__ == "__main__":
    red_log.utils.test_log_messages()
