import logging


log = logging.getLogger("sandbox.main")


if __name__ == "__main__":
    log.debug("Test DEBUG")
    log.info("Test INFO")
    log.warning("Test WARNING")
    log.error("Test ERROR")
    log.critical("Test CRITICAL")
