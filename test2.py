import red_log

if __name__ == "__main__":
    formatter = red_log.FormatterFactory.create_formatter()
    stream_handler = red_log.HandlerFactory.create_stream_handler(
        level="DEBUG", formatter=formatter
    )
    app_file_handler = red_log.HandlerFactory.create_file_handler(
        filename="logs/app.log", formatter=formatter
    )
    err_file_handler = red_log.HandlerFactory.create_file_handler(
        filename="logs/err.log", formatter=formatter
    )

    logger_factory = red_log.LoggerFactory(name="red_log", level="WARNING")
    logger_factory.add_handler(stream_handler)
    logger_factory.add_handler(app_file_handler)
    logger_factory.add_handler(err_file_handler)

    log = logger_factory.get_logger()

    log.debug("Test DEBUG")
    log.info("Test INFO")
    log.warning("Test WARNING")
    log.error("Test ERROR")
    log.critical("Test CRITICAL")
