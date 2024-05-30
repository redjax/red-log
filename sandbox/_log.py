import logging
import logging.config
import red_log


def setup_logging():
    simple_formatter = red_log.config_classes.formatters.FormatterConfig(
        name="simple", fmt=red_log.fmts.MESSAGE_FMT_BASIC
    )
    detail_formatter = red_log.config_classes.formatters.FormatterConfig(
        name="detail", fmt=red_log.fmts.MESSAGE_FMT_DETAILED
    )

    console_handler = red_log.config_classes.handlers.StreamHandlerConfig(
        name="console", level="DEBUG", formatter="simple"
    )

    logger_config = red_log.config_classes.loggers.LoggerConfig(
        name="sandbox", level="DEBUG", handlers=["console"]
    )
    root_logger_config = red_log.config_classes.loggers.LoggerConfig(
        name="", level="DEBUG", handlers=["console"]
    )

    logging_config = red_log.assemble_configdict(
        formatters=[simple_formatter, detail_formatter],
        handlers=[console_handler],
        loggers=[logger_config, root_logger_config],
    )

    logging.config.dictConfig(logging_config)

    red_log.print_configdict(logging_config)
