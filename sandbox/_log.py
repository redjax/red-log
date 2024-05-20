import logging
import logging.config
import red_log

simple_formatter = red_log.formatters.FormatterConfig(
    name="simple", fmt=red_log.constants.SIMPLE_FMT
)
detail_formatter = red_log.formatters.FormatterConfig(
    name="detail", fmt=red_log.constants.DETAIL_FMT
)

console_handler = red_log.handlers.StreamHandlerConfig(
    name="console", level="DEBUG", formatter=simple_formatter
)

logger_config = red_log.loggers.LoggerConfig(
    name="sandbox", level="DEBUG", handlers=[console_handler]
)

logging_config = red_log.LoggingConfig(
    formatters=[simple_formatter, detail_formatter],
    handlers=[console_handler],
    loggers=logger_config,
)

logging.config.dictConfig(logging_config.get_config())
