import logging

from logging_config import LOG_CONF

log = LOG_CONF.get_logger(__name__)


def test_log_levels():
    print("Testing log levels")

    log.debug("Test DEBUG")
    log.info("Test INFO")
    log.warning("Test WARNING")
    log.error("Test ERROR")
    log.critical("Test CRITICAL")
