import logging
import logging.config

import red_log

from _log import setup_logging

setup_logging()

log = logging.getLogger("sandbox.main")


if __name__ == "__main__":
    print(log.root.__dict__)
    log.debug("Test DEBUG")
    log.info("Test INFO")
    log.warning("Test WARNING")
    log.error("Test ERROR")
    log.critical("Test CRITICAL")
