import red_log
import red_log.loggers

import logging
import logging.config

import json

if __name__ == "__main__":
    simple_formatter = red_log.formatters.FormatterConfig(
        name="simple",
        fmt=red_log.constants.SIMPLE_FMT,
    )
    detail_formatter = red_log.formatters.FormatterConfig(
        name="detail", fmt=red_log.constants.DETAIL_FMT
    )
    # print(f"Simple formatter: {simple_formatter.get_configdict()}")
    # print(f"Detail formatter: {detail_formatter.get_configdict()}")

    console_handler = red_log.handlers.StreamHandlerConfig(
        name="console", level="DEBUG", formatter="simple"
    )
    err_file_handler = red_log.handlers.FileHandlerConfig(
        name="err_file",
        level="ERROR",
        formatter="detail",
        filters=["error_filter"],
        filename="err.log",
    )

    app_logger = red_log.loggers.LoggerConfig(
        name=__name__, level="DEBUG", handlers=["console", "err_file"]
    )

    logger_config = red_log.configs.LoggingConfig()

    logger_config.add_formatters([simple_formatter, detail_formatter])
    logger_config.add_handlers([console_handler, err_file_handler])
    logger_config.add_loggers([app_logger])

    print(f"Logger config: {logger_config.get_config()}")

    with open("ex_config.json", "w") as f:
        data = json.dumps(logger_config.get_config(), indent=2)
        f.write(data)

    logging.config.dictConfig(logger_config.get_config())

    log = logging.getLogger(__name__)
    log.setLevel("DEBUG")

    log.debug("Test DEBUG")
    log.info("Test INFO")
    log.warning("Test WARNING")
    log.error("Test ERROR")
    log.critical("Test CRITICAL")
