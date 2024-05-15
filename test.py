from logging_config import LOG_CONF
from test_mod import test_log_levels

log = LOG_CONF.get_logger(__name__)

log.debug(f"Logging config: {LOG_CONF}")

log.info("Running logging test")
test_log_levels()
