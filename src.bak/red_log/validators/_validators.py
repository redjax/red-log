import typing as t
import red_log

VALID_LOGGER_STYLES: list[str] = [
    "%",
    "{",
    "$",
]

VALID_LOG_LEVELS: str = ["NOTSET", "DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]


def validate_log_style(style_str: str = None) -> str:
    """Validate a logging style string."""
    assert style_str, ValueError("style_str cannot be None")
    assert isinstance(style_str, str), TypeError(
        f"style_str must be a string. Got type: ({type(style_str)})"
    )
    assert style_str in VALID_LOGGER_STYLES, ValueError(
        f"Invalid style_str: '{style_str}.' Must be one of: {VALID_LOGGER_STYLES}"
    )

    ## Return input string if all validation pass
    return style_str


def validate_log_levelname(level: str = None) -> str:
    """Validate a logging level name string."""
    assert level, ValueError("level cannot be None")
    assert isinstance(level, str), TypeError(
        f"level must be a string. Got type: ({type(level)})"
    )

    ## Uppercase log level for rest of assertions & return
    level: str = level.upper()

    assert level in VALID_LOGGER_STYLES, ValueError(
        f"Invalid level: '{level}.' Must be one of: {VALID_LOG_LEVELS}"
    )

    ## Return input string if all validation pass
    return level
