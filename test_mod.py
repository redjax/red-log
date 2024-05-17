import logging
from logging.config import dictConfig
import red_log

dictConfig(red_log.DEFAULT_LOGGING_CONFIG)
log = logging.getLogger("red_log")


def test_log_levels():
    print("Testing log levels")

    log.debug("Test DEBUG")
    log.info("Test INFO")
    log.warning("Test WARNING")
    log.error("Test ERROR")
    log.critical("Test CRITICAL")
