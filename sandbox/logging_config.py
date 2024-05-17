from classes import LoggingConfig, LoggingFormatter, LoggingHandler, LoggingLogger


LOG_CONF = LoggingConfig(
    formatters=[
        LoggingFormatter(),
    ],
    handlers=[
        LoggingHandler(),
        LoggingHandler(
            name="app_file", class_name="logging.FileHandler", filename="app.log"
        ),
    ],
    loggers=[
        LoggingLogger(logger_name=__name__, level_name="warning"),
        LoggingLogger(
            logger_name="__main__",
            handler_names=["console"],
            level_name="warning",
        ),
        LoggingLogger(
            logger_name="test_mod",
            handler_names=["console", "app_file"],
            level_name="debug",
        ),
    ],
)
