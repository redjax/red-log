from __future__ import annotations

import logging

import red_log

print(f"Logging config: {red_log.DEFAULT_LOGGING_CONFIG}")
red_log.configure_root_logger(
    dict_config=red_log.DEFAULT_LOGGING_CONFIG, logger_name=__name__
)
log: logging.Logger = logging.getLogger(__name__)

if __name__ == "__main__":
    log.setLevel(logging.DEBUG)

    red_log.utils.test_log_messages()
