import red_log
import logging


class FormatterFactory:
    """Formatter class for returning initialized logging.Formatter objects."""

    @staticmethod
    def create_formatter(
        fmt: str = red_log.constants.DEFAULT_FMT,
        date_fmt: str = red_log.constants.DEFAULT_DATE_FMT,
        style: str = red_log.constants.DEFAULT_LOGGER_STYLE,
        validate: bool = True,
    ) -> logging.Formatter:
        return logging.Formatter(
            fmt=fmt, datefmt=date_fmt, style=style, validate=validate
        )
