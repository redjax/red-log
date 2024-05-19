import logging


class LoggerFactory:
    """Factory for retrieving initialized logging.Logger objects.

    Params:
        name (str): The name of the logger. Re-using a name will retrieve the logger's existing config.
        level (str | int): Set logging level (i.e. `logging.DEBUG`, or "DEBUG")
    """

    def __init__(self, name: str, level: str | int = logging.INFO) -> None:
        if isinstance(level, str):
            level = level.upper()
        self.logger: logging.Logger = logging.getLogger(name=name)
        self.logger.setLevel(level=level)

    def add_handler(self, handler: logging.Handler) -> None:
        self.logger.addHandler(hdlr=handler)

    def get_logger(self) -> logging.Logger:
        return self.logger
