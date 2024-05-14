import logging
from logging.config import dictConfig

REDLOG_ERR_STR: str = "[ERROR] (red_log):"

log = logging.getLogger(__name__)


def configure_root_logger(
    dict_config: dict = None,
    logger_name: str = None,
    handler: logging.Handler = logging.NullHandler(),
) -> bool:
    if dict_config is None:
        msg = ValueError("dict_config cannot be None")

        print(f"{REDLOG_ERR_STR} {msg}")

        return False

    if not isinstance(dict_config, dict):
        msg = TypeError(f"dict_config must be a dict. Got type: ({type(dict_config)})")
        print(f"{REDLOG_ERR_STR} {msg}")

        return False

    if handler is None:
        msg = ValueError("Missing handler. Default=logging.NullHandler()")

        print(f"{REDLOG_ERR_STR} {msg}")

        return False

    try:
        dictConfig(dict_config)
    except Exception as exc:
        msg = Exception(f"Error configuring root logger from dict. Details: {exc}")

        print(f"{REDLOG_ERR_STR} {msg}")

        return False

    try:
        logging.getLogger(name=logger_name).addHandler(handler)
    except Exception as exc:
        msg = Exception(
            f"Unhandled exception getting logger for '{logger_name}'. Details: {exc}"
        )
        print(f"{REDLOG_ERR_STR} {msg}")

        return False

    return True


def test_log_messages() -> None:
    log.debug("Test DEBUG")
    log.info("Test INFO")
    log.warning("Test WARNING")
    log.error("Test ERROR")
    log.critical("Test CRITICAL")
