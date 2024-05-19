"""Logging formatters.

Default formatteer configDict:

```python title="Default logging cofigDict" linenums="1"
{
    "name": {
        "format": None,
        "datefmt": None,
    }
}
```
"""

from __future__ import annotations

import typing as t
import logging

from red_log.constants import DEFAULT_DATE_FMT, DEFAULT_FMT, DEFAULT_LOGGER_STYLE
from red_log.validators import validate_log_style
from .validators import validate_str_input


DEFAULT_LOG_FORMATTER: dict = {
    "default": {
        "format": DEFAULT_FMT,
        "datefmt": DEFAULT_DATE_FMT,
    }
}

## Only timestamp and message
TS_MSG: dict = {"ts_msg": {"format": "[%(asctime)s]: %(message)s"}}

## Only level and message
LEVEL_MSG: dict = {"level_msg": {"format": "[%(levelname)s]"}}


def _formatter_dict(name: str = None, fmt: str = None, datefmt: str = None) -> dict:
    """Return a formatter config dict.

    Logging formatters define the message and timestamp format for log messages
    that declare this formatter. Formatters must have a name; when using dictConfig(),
    it is possible to append multiple formatter dicts, like:

    ```python title="Append multiple formatters" linenums="1"
    default_formatter = get_formatter_dict()
    second_formatter = get_formatter_dict(name="second", format="%(levelname)s: %(message)s"

    logger_config_dict = {
        ...
        "formatters": [default_formatter, second_formatter.]
    }
    ```

    When added to a logger config dict, these formatters are accessible to handlers.

    Params:
        name (str): The name for the formatter.
        fmt: (str): The format for log messages.
            Help: https://docs.python.org/3/library/logging.html#logrecord-attributes
        datefmt (str): The format for log timestamps.
            Help: https://docs.python.org/3/library/time.html#time.strftime

    Returns:
        (dict): A dictionary defining a logging formatter.
    """
    name = validate_str_input(_str=name)
    fmt = validate_str_input(_str=fmt)
    datefmt = validate_str_input(_str=datefmt)

    try:
        formatter_dict: dict = {name: {"format": fmt, "datefmt": datefmt}}

        return formatter_dict
    except Exception as exc:
        msg = Exception(
            f"Unhandled exception initializing formatter config dict. Details: {exc}"
        )
        # log.error(msg)

        raise exc


def __formatter_obj(
    fmt: str = None,
    datefmt: str = None,
    style: str = None,
    validate: bool = None,
    defaults: dict[str, t.Any] | None = None,
) -> logging.Formatter:
    """Return a logging.Formatter object.

    Params:
        name (str): The name for the formatter.
        fmt: (str): The format for log messages.
            Help: https://docs.python.org/3/library/logging.html#logrecord-attributes
        datefmt (str): The format for log timestamps.
            Help: https://docs.python.org/3/library/time.html#time.strftime
        style (str): Can be one of '%', '{' or '$' and determines how the format string will be merged with its data.
            - `%`  = printf-style
            - `'{'` = string format
            - `'$'` = string.Template
        validate (str): If `True` (the default), incorrect or mismatched fmt and style will raise a `ValueError`.
        defaults (str): A dictionary with default values to use in custom fields.
            For example, `logging.Formatter('%(ip)s %(message)s', defaults={"ip": None})`.

    """
    fmt = validate_str_input(_str=fmt)
    style = validate_log_style(style_str=validate_str_input(_str=style))
    datefmt = validate_str_input(_str=datefmt)

    try:
        _formatter: logging.Formatter = logging.Formatter(
            fmt=fmt, datefmt=datefmt, style=style, validate=validate, defaults=defaults
        )

        return _formatter
    except Exception as exc:
        msg = Exception(
            f"Unhandled exception initializing logging.Formatter. Details: {exc}"
        )
        # log.error(msg)

        raise exc


def get_formatter(
    name: str | None = "default",
    fmt: str = DEFAULT_FMT,
    datefmt: str = DEFAULT_DATE_FMT,
    style: str | None = DEFAULT_LOGGER_STYLE,
    validate: bool | None = True,
    defaults: dict[str, t.Any] | None = None,
    as_dict: bool = False,
) -> dict | logging.Formatter:
    """Get a formatter definition.

    params:
        name (str): The name for the formatter.
        fmt: (str): The format for log messages.
            Help: https://docs.python.org/3/library/logging.html#logrecord-attributes
        datefmt (str): The format for log timestamps.
            Help: https://docs.python.org/3/library/time.html#time.strftime
        style (str): Can be one of '%', '{' or '$' and determines how the format string will be merged with its data.
            - `%`  = printf-style
            - `'{'` = string format
            - `'$'` = string.Template
        validate (str): If `True` (the default), incorrect or mismatched fmt and style will raise a `ValueError`.
        defaults (str): A dictionary with default values to use in custom fields.
            For example, `logging.Formatter('%(ip)s %(message)s', defaults={"ip": None})`.

    Returns:
        (dict): If `as_dict=True`, returns a logging formatter definition as a configDict.
        (logging.Formatter): If `as_dict=False` (default), returns a `logging.Formatter` instance.
    """
    fmt = validate_str_input(_str=fmt)
    datefmt = validate_str_input(_str=datefmt)
    style = validate_log_style(style_str=validate_str_input(_str=style))
    if defaults:
        assert isinstance(defaults, dict), TypeError(
            f"defaults must be a dict. Got type: ({type(defaults)})"
        )

    if as_dict:
        assert name, ValueError(
            "as_dict is True, but missing a name for the formatter."
        )
        name = validate_str_input(_str=name)

        try:
            _formatter: dict = _formatter_dict(name=name, fmt=fmt, datefmt=datefmt)

            return _formatter
        except Exception as exc:
            msg = Exception(
                f"Unhandled exception getting formatter dict config. Details: {exc}"
            )
            # log.error(msg)

            raise exc

    else:
        try:
            _formatter: logging.Formatter = __formatter_obj(
                fmt=fmt,
                datefmt=datefmt,
                style=style,
                validate=validate,
                defaults=defaults,
            )

            return _formatter
        except Exception as exc:
            msg = Exception(
                f"Unhandled exception initializing logging.Formatter object. Details: {exc}"
            )
            # log.error(msg)

            raise exc
