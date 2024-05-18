from __future__ import annotations

import typing as t

import logging
import logging.handlers
from enum import Enum
import queue
import ssl
import datetime
from .validators import VALID_HANDLER_CLASSES
from ._types import HandlerType


class HandlerObjectsEnum(Enum):
    """Return a logging.Handler class matching an input string.

    Note that enum keys are uppercase versions of the logging.Handler, without the "Handler" at the end. For example,
    FILE = logging.FileHandler

    Usage:
        ```python title="HandlerObjectsEnum usage" linenums="1"
        ## Note that you do not retrieve the enum value with `.value`. Instead, return the handler directly.
        stream_handler = HandlerObjectsEnum["STREAM"]
        ```
    """

    FILE = logging.FileHandler
    ROTATINGFILE = logging.handlers.RotatingFileHandler
    TIMEBASEDROTATINGFILE = logging.handlers.TimedRotatingFileHandler
    QUEUE = logging.handlers.QueueHandler
    QUEUELISTENER = logging.handlers.QueueListener
    NULL = logging.NullHandler
    STREAM = logging.StreamHandler
    SYSLOG = logging.handlers.SysLogHandler
    SMTP = logging.handlers.SMTPHandler
    BUFFERING = logging.handlers.BufferingHandler
    DATAGRAM = logging.handlers.DatagramHandler
    HTTP = logging.handlers.HTTPHandler
    MEMORY = logging.handlers.MemoryHandler
    NTEVENTLOG = logging.handlers.NTEventLogHandler
    SOCKET = logging.handlers.SocketHandler
    WATCHEDFILE = logging.handlers.WatchedFileHandler


# def __validate_parameters(
#     handler_class: str,
#     filename: str | None,
#     max_bytes: int | None,
#     backup_count: int | None,
#     name: str | None,
#     as_dict: bool,
# ) -> tuple[str, str | None, int | None, int | None, str | None, bool]:
#     handler_class = handler_class.upper().replace("HANDLER", "")
#     try:
#         handler_enum: HandlerObjectsEnum = HandlerObjectsEnum[handler_class]
#     except KeyError:
#         raise ValueError(f"Invalid handler_class: {handler_class}")

#     handler_cls: t.Union[
#         logging.FileHandler,
#         logging.handlers.RotatingFileHandler,
#         logging.handlers.TimedRotatingFileHandler,
#         logging.handlers.QueueHandler,
#         logging.handlers.QueueListener,
#         logging.NullHandler,
#         logging.StreamHandler,
#         logging.handlers.SysLogHandler,
#         logging.handlers.SMTPHandler,
#         logging.handlers.BufferingHandler,
#         logging.handlers.DatagramHandler,
#         logging.handlers.HTTPHandler,
#         logging.handlers.MemoryHandler,
#         logging.handlers.NTEventLogHandler,
#         logging.handlers.SocketHandler,
#         logging.handlers.WatchedFileHandler,
#     ] = handler_enum.value

#     if as_dict and not name:
#         raise ValueError("When as_dict=True, a handler name must be given.")

#     if (
#         handler_cls
#         in (
#             logging.FileHandler,
#             logging.handlers.RotatingFileHandler,
#             logging.handlers.TimedRotatingFileHandler,
#             logging.handlers.WatchedFileHandler,
#         )
#         and not filename
#     ):
#         raise ValueError("When requesting a file handler, a filename must be given.")

#     if handler_cls == logging.handlers.RotatingFileHandler:
#         if not (filename and max_bytes is not None and backup_count is not None):
#             raise ValueError(
#                 "When requesting a rotating file handler, a filename, max_bytes, and backup_count must be given."
#             )

#     ## Return validated parameters
#     return handler_class, filename, max_bytes, backup_count, name, as_dict


def __validate_parameters(
    handler_class: str,
    filename: str | None = None,
    max_bytes: int | None = None,
    backup_count: int | None = None,
    name: str | None = None,
    as_dict: bool = False,
    log_level: str = "NOTSET",
    formatter_name: str = "default",
    stream: str | None = "ext://sys.stdout",
    mode: str = "a",
    encoding: str | None = "utf-8",
    delay: bool = False,
    errors: str | None = None,
    address: t.Union[str, t.Tuple[str, int]] = ("localhost", 514),
    facility: int = logging.handlers.SysLogHandler.LOG_USER,
    socktype: int | None = None,
    mailhost: t.Union[str, t.Tuple[str, int]] | None = None,
    fromaddr: str | None = None,
    toaddrs: str | list | None = None,
    subject: str | None = None,
    credentials: tuple | None = None,
    secure: tuple | None = None,
    timeout: float | None = 1.0,
    capacity: int | None = None,
    host: str | None = None,
    port: int | None = None,
    method: str = "GET",
    secure_http: bool = False,
    context: ssl.SSLContext | None = None,
    appname: str | None = None,
    dllname: str | None = None,
    logtype: str = "Application",
    queue: queue.Queue | None = None,
    *handlers: logging.Handler,
) -> t.Union[
    t.Tuple[
        str,
        str | None,
        int | None,
        int | None,
        str | None,
        bool,
        str,
        str,
        str | None,
        str,
        str | None,
        bool,
        str | None,
        t.Union[str, t.Tuple[str, int]],
        int,
        int | None,
        t.Union[str, t.Tuple[str, int]] | None,
        str | None,
        t.Union[str, list] | None,
        str | None,
        tuple | None,
        tuple | None,
        float | None,
        int | None,
        str | None,
        int | None,
        str,
        bool,
        ssl.SSLContext | None,
        str | None,
        str | None,
        str,
        queue.Queue | None,
    ],
    HandlerType | None,
]:
    handler_class = handler_class.upper().replace("HANDLER", "")
    try:
        handler_enum: HandlerObjectsEnum = HandlerObjectsEnum[handler_class]
    except KeyError:
        raise ValueError(f"Invalid handler_class: {handler_class}")

    handler_cls: t.Union[
        logging.FileHandler,
        logging.handlers.RotatingFileHandler,
        logging.handlers.TimedRotatingFileHandler,
        logging.handlers.QueueHandler,
        logging.handlers.QueueListener,
        logging.NullHandler,
        logging.StreamHandler,
        logging.handlers.SysLogHandler,
        logging.handlers.SMTPHandler,
        logging.handlers.BufferingHandler,
        logging.handlers.DatagramHandler,
        logging.handlers.HTTPHandler,
        logging.handlers.MemoryHandler,
        logging.handlers.NTEventLogHandler,
        logging.handlers.SocketHandler,
        logging.handlers.WatchedFileHandler,
    ] = handler_enum.value

    if as_dict and not name:
        raise ValueError("When as_dict=True, a handler name must be given.")

    if (
        handler_cls
        in (
            logging.FileHandler,
            logging.handlers.RotatingFileHandler,
            logging.handlers.TimedRotatingFileHandler,
            logging.handlers.WatchedFileHandler,
        )
        and not filename
    ):
        raise ValueError("When requesting a file handler, a filename must be given.")

    if handler_cls == logging.handlers.RotatingFileHandler:
        if not (filename and max_bytes is not None and backup_count is not None):
            raise ValueError(
                "When requesting a rotating file handler, a filename, max_bytes, and backup_count must be given."
            )

    ## Return validated parameters
    return (
        handler_class,
        filename,
        max_bytes,
        backup_count,
        name,
        as_dict,
        log_level,
        formatter_name,
        stream,
        mode,
        encoding,
        delay,
        errors,
        address,
        facility,
        socktype,
        mailhost,
        fromaddr,
        toaddrs,
        subject,
        credentials,
        secure,
        timeout,
        capacity,
        host,
        port,
        method,
        secure_http,
        context,
        appname,
        dllname,
        logtype,
        queue,
        *handlers,
    )


def __get_file_handler(
    filename: str, mode: str = "a", encoding: str | None = None, delay: bool = False
) -> logging.FileHandler:
    return logging.FileHandler(
        filename=filename, mode=mode, encoding=encoding, delay=delay
    )


def __get_rotating_file_handler(
    filename: str,
    max_bytes: int,
    backup_count: int,
    encoding: str | None = "utf-8",
    delay: bool = False,
    errors: str | None = None,
) -> logging.handlers.RotatingFileHandler:
    return logging.handlers.RotatingFileHandler(
        filename=filename,
        maxBytes=max_bytes,
        backupCount=backup_count,
        encoding=encoding,
        delay=delay,
        errors=errors,
    )


def __get_stream_handler(stream: str | None) -> logging.StreamHandler:
    return logging.StreamHandler(stream=stream)


def __get_timed_rotating_file_handler(
    filename: str,
    when: str = "h",
    interval: int = 1,
    backup_count: int = 0,
    encoding: str | None = "utf-8",
    delay: bool = False,
    utc: bool = False,
    at_time: datetime.time | None = None,
) -> logging.handlers.TimedRotatingFileHandler:
    return logging.handlers.TimedRotatingFileHandler(
        filename=filename,
        when=when,
        interval=interval,
        backupCount=backup_count,
        encoding=encoding,
        delay=delay,
        utc=utc,
        atTime=at_time,
    )


def __get_queue_handler(queue: queue.Queue) -> logging.handlers.QueueHandler:
    return logging.handlers.QueueHandler(queue=queue)


def __get_queue_listener(
    queue: queue.Queue, *handlers: logging.Handler
) -> logging.handlers.QueueListener:
    return logging.handlers.QueueListener(queue=queue, *handlers)


def __get_null_handler() -> logging.NullHandler:
    return logging.NullHandler()


def __get_syslog_handler(
    address: str | tuple = ("localhost", 514),
    facility: int = logging.handlers.SysLogHandler.LOG_USER,
    socktype: int | None = None,
) -> logging.handlers.SysLogHandler:
    return logging.handlers.SysLogHandler(
        address=address, facility=facility, socktype=socktype
    )


def __get_smtp_handler(
    mailhost: str | tuple,
    fromaddr: str,
    toaddrs: str | list,
    subject: str,
    credentials: tuple | None = None,
    secure: tuple | None = None,
    timeout: float | None = 1.0,
) -> logging.handlers.SMTPHandler:
    return logging.handlers.SMTPHandler(
        mailhost=mailhost,
        fromaddr=fromaddr,
        toaddrs=toaddrs,
        subject=subject,
        credentials=credentials,
        secure=secure,
        timeout=timeout,
    )


def __get_buffering_handler(capacity: int) -> logging.handlers.BufferingHandler:
    return logging.handlers.BufferingHandler(capacity=capacity)


def __get_datagram_handler(host: str, port: int) -> logging.handlers.DatagramHandler:
    return logging.handlers.DatagramHandler(host=host, port=port)


def __get_http_handler(
    host: str,
    url: str,
    method: str = "GET",
    secure: bool = False,
    credentials: tuple | None = None,
    context: ssl.SSLContext | None = None,
) -> logging.handlers.HTTPHandler:
    return logging.handlers.HTTPHandler(
        host=host,
        url=url,
        method=method,
        secure=secure,
        credentials=credentials,
        context=context,
    )


def __get_memory_handler(
    capacity: int,
    flush_level: int = logging.ERROR,
    target: logging.Handler | None = None,
) -> logging.handlers.MemoryHandler:
    return logging.handlers.MemoryHandler(
        capacity=capacity, flushLevel=flush_level, target=target
    )


def __get_nteventlog_handler(
    appname: str, dllname: str | None = None, logtype: str = "Application"
) -> logging.handlers.NTEventLogHandler:
    return logging.handlers.NTEventLogHandler(
        appname=appname, dllname=dllname, logtype=logtype
    )


def __get_socket_handler(host: str, port: int) -> logging.handlers.SocketHandler:
    return logging.handlers.SocketHandler(host=host, port=port)


def __get_watched_file_handler(
    filename: str, mode: str = "a", encoding: str | None = None, delay: bool = False
) -> logging.handlers.WatchedFileHandler:
    return logging.handlers.WatchedFileHandler(
        filename=filename, mode=mode, encoding=encoding, delay=delay
    )


def __get_handler_config(
    name: str,
    handler_cls: type[logging.Handler],
    log_level: str,
    formatter_name: str,
    filename: str | None = None,
    max_bytes: int | None = None,
    backup_count: int | None = None,
    stream: str | None = None,
) -> dict:
    handler_config: dict[str, dict[str, str]] = {
        name: {
            "class": f"{handler_cls.__module__}.{handler_cls.__name__}",
            "level": log_level,
            "formatter": formatter_name,
        }
    }
    if filename:
        handler_config[name]["filename"] = filename
    if max_bytes is not None:
        handler_config[name]["maxBytes"] = max_bytes
    if backup_count is not None:
        handler_config[name]["backupCount"] = backup_count
    if stream:
        handler_config[name]["stream"] = stream

    return handler_config


def get_handler(
    handler_class: str | None = "stream",
    log_level: str = "NOTSET",
    formatter_name: str = "default",
    stream: str | None = "ext://sys.stdout",
    filename: str | None = "app.log",
    max_bytes: int | None = 2000000,
    backup_count: int | None = 3,
    as_dict: bool = False,
    name: str | None = None,
    mode: str = "a",
    encoding: str | None = "utf-8",
    delay: bool = False,
    errors: str | None = None,
    address: str | tuple = ("localhost", 514),
    facility: int = logging.handlers.SysLogHandler.LOG_USER,
    socktype: int | None = None,
    mailhost: str | tuple | None = None,
    fromaddr: str | None = None,
    toaddrs: str | list | None = None,
    subject: str | None = None,
    credentials: tuple | None = None,
    secure: tuple | None = None,
    timeout: float | None = 1.0,
    capacity: int | None = None,
    host: str | None = None,
    port: int | None = None,
    method: str = "GET",
    secure_http: bool = False,
    context: ssl.SSLContext | None = None,
    appname: str | None = None,
    dllname: str | None = None,
    logtype: str = "Application",
    queue: queue.Queue | None = None,
    *handlers: logging.Handler,
    **kwargs,
) -> (
    dict
    | t.Union[
        logging.FileHandler,
        logging.handlers.RotatingFileHandler,
        logging.handlers.TimedRotatingFileHandler,
        logging.handlers.QueueHandler,
        logging.handlers.QueueListener,
        logging.NullHandler,
        logging.StreamHandler,
        logging.handlers.SysLogHandler,
        logging.handlers.SMTPHandler,
        logging.handlers.BufferingHandler,
        logging.handlers.DatagramHandler,
        logging.handlers.HTTPHandler,
        logging.handlers.MemoryHandler,
        logging.handlers.NTEventLogHandler,
        logging.handlers.SocketHandler,
        logging.handlers.WatchedFileHandler,
    ]
):
    """Build & return a logging.Handler object from inputs.

    This method is an entrypoint to get a handler class from the handlers module code. This method accepts all
    parameters that any Handler could use, and chooses which methods to pass to the Handler builder function based
    on the "handler_class" value passed.

    Note that "handler_class" should be the name of a logging.Handler, without the word "Handler." For example, to
    retrieve a FileHandler, pass "handler_class='file'."

    Params:
        handler_class (str | None): The name of the logging handler class without the word "Handler". Defaults to "stream".
        log_level (str): The logging level. Defaults to "NOTSET".
        formatter_name (str): The name of the formatter. Defaults to "default".
        stream (str | None): The output stream. Defaults to "ext://sys.stdout".
        filename (str | None): The name of the log file. Defaults to "app.log".
        max_bytes (int | None): The maximum size of the log file. Defaults to 2000000 bytes.
        backup_count (int | None): The number of backup log files to retain. Defaults to 3.
        as_dict (bool): Flag indicating whether to return the handler as a dictionary configuration. Defaults to False.
        name (str | None): The name of the handler. Required when as_dict is True.
        mode (str): The file mode when opening the log file. Defaults to "a".
        encoding (str | None): The file encoding. Defaults to "utf-8".
        delay (bool): Flag indicating whether to delay file opening. Defaults to False.
        errors (str | None): The error handling strategy. Defaults to None.
        address (str | tuple): The address for SysLogHandler. Defaults to ("localhost", 514).
        facility (int): The SysLogHandler facility. Defaults to logging.handlers.SysLogHandler.LOG_USER.
        socktype (int | None): The socket type for SysLogHandler. Defaults to None.
        mailhost (str | tuple | None): The SMTP server address. Defaults to None.
        fromaddr (str | None): The sender's email address for SMTPHandler. Defaults to None.
        toaddrs (str | list | None): The recipient's email address(es) for SMTPHandler. Defaults to None.
        subject (str | None): The email subject for SMTPHandler. Defaults to None.
        credentials (tuple | None): The credentials for SMTPHandler. Defaults to None.
        secure (tuple | None): The security settings for SMTPHandler. Defaults to None.
        timeout (float | None): The timeout duration for SMTPHandler. Defaults to 1.0.
        capacity (int | None): The capacity of the BufferingHandler. Defaults to None.
        host (str | None): The host address for DatagramHandler or SocketHandler. Defaults to None.
        port (int | None): The port for DatagramHandler or SocketHandler. Defaults to None.
        method (str): The HTTP method for HTTPHandler. Defaults to "GET".
        secure_http (bool): Flag indicating whether to use secure HTTP for HTTPHandler. Defaults to False.
        context (ssl.SSLContext | None): The SSL context for secure connections. Defaults to None.
        appname (str | None): The name of the application for NTEventLogHandler. Defaults to None.
        dllname (str | None): The name of the DLL for NTEventLogHandler. Defaults to None.
        logtype (str): The type of log for NTEventLogHandler. Defaults to "Application".
        queue (queue.Queue | None): The queue for QueueHandler or QueueListener. Defaults to None.
        *handlers (logging.Handler): Additional handlers to attach to QueueListener.

    Raises:
        TODO

    Returns:
        (dict): When `as_dict=True`, a handler dictionary config object is returned.
        (logging.Handler): A logging Handler class, defined in "class_name."
    """

    ## Validate input parameters
    # Merge explicit parameters with **kwargs
    all_parameters = {
        "handler_class": handler_class,
        "filename": filename,
        "max_bytes": max_bytes,
        "backup_count": backup_count,
        "name": name,
        "as_dict": as_dict,
        "log_level": log_level,
        "formatter_name": formatter_name,
        "stream": stream,
        "mode": mode,
        "encoding": encoding,
        "delay": delay,
        "errors": errors,
        "address": address,
        "facility": facility,
        "socktype": socktype,
        "mailhost": mailhost,
        "fromaddr": fromaddr,
        "toaddrs": toaddrs,
        "subject": subject,
        "credentials": credentials,
        "secure": secure,
        "timeout": timeout,
        "capacity": capacity,
        "host": host,
        "port": port,
        "method": method,
        "secure_http": secure_http,
        "context": context,
        "appname": appname,
        "dllname": dllname,
        "logtype": logtype,
        "queue": queue,
        **kwargs,  # Include any additional parameters
    }

    # Call the validation function
    validated_params = __validate_parameters(**all_parameters)

    # Check if validation succeeded
    if validated_params is None:
        # Handle invalid parameters
        return None

    # Unpack the validated parameters
    (
        handler_class,
        filename,
        max_bytes,
        backup_count,
        name,
        as_dict,
        log_level,
        formatter_name,
        stream,
        mode,
        encoding,
        delay,
        errors,
        address,
        facility,
        socktype,
        mailhost,
        fromaddr,
        toaddrs,
        subject,
        credentials,
        secure,
        timeout,
        capacity,
        host,
        port,
        method,
        secure_http,
        context,
        appname,
        dllname,
        logtype,
        queue,
        *handlers,
    ) = validated_params

    ## Get enum
    handler_enum: HandlerObjectsEnum = HandlerObjectsEnum[handler_class]
    ## extract logging handler class
    handler_cls: t.Union[
        logging.FileHandler,
        logging.handlers.RotatingFileHandler,
        logging.handlers.TimedRotatingFileHandler,
        logging.handlers.QueueHandler,
        logging.handlers.QueueListener,
        logging.NullHandler,
        logging.StreamHandler,
        logging.handlers.SysLogHandler,
        logging.handlers.SMTPHandler,
        logging.handlers.BufferingHandler,
        logging.handlers.DatagramHandler,
        logging.handlers.HTTPHandler,
        logging.handlers.MemoryHandler,
        logging.handlers.NTEventLogHandler,
        logging.handlers.SocketHandler,
        logging.handlers.WatchedFileHandler,
    ] = handler_enum.value

    if as_dict:
        return __get_handler_config(
            name=name,
            handler_cls=handler_cls,
            log_level=log_level,
            formatter_name=formatter_name,
            filename=filename,
            max_bytes=max_bytes,
            backup_count=backup_count,
            stream=stream,
        )

    else:
        match handler_cls:
            case logging.FileHandler:
                handler: logging.FileHandler = __get_file_handler(
                    filename=filename, mode=mode, encoding=encoding, delay=delay
                )
            case logging.handlers.RotatingFileHandler:
                handler: logging.handlers.RotatingFileHandler = (
                    __get_rotating_file_handler(
                        filename=filename,
                        max_bytes=max_bytes,
                        backup_count=backup_count,
                        encoding=encoding,
                        delay=delay,
                        errors=errors,
                    )
                )
            case logging.StreamHandler:
                handler = __get_stream_handler(stream=stream)
            case logging.handlers.TimedRotatingFileHandler:
                handler = __get_timed_rotating_file_handler(filename=filename)
            case logging.handlers.QueueHandler:
                handler = __get_queue_handler(queue=queue)
            case logging.handlers.QueueListener:
                handler = __get_queue_listener(queue=queue, *handlers)
            case logging.NullHandler:
                handler = __get_null_handler()
            case logging.handlers.SysLogHandler:
                handler = __get_syslog_handler(
                    address=address, facility=facility, socktype=socktype
                )
            case logging.handlers.SMTPHandler:
                handler = __get_smtp_handler(
                    mailhost=mailhost,
                    fromaddr=fromaddr,
                    toaddrs=toaddrs,
                    subject=subject,
                    credentials=credentials,
                    secure=secure,
                    timeout=timeout,
                )
            case logging.handlers.BufferingHandler:
                handler = __get_buffering_handler(capacity=capacity)
            case logging.handlers.DatagramHandler:
                handler = __get_datagram_handler(host=host, port=port)
            case logging.handlers.HTTPHandler:
                handler = __get_http_handler(
                    host=host,
                    url=filename,
                    method=method,
                    secure=secure_http,
                    credentials=credentials,
                    context=context,
                )
            case logging.handlers.MemoryHandler:
                handler = __get_memory_handler(capacity=capacity)
            case logging.handlers.NTEventLogHandler:
                handler = __get_nteventlog_handler(
                    appname=appname, dllname=dllname, logtype=logtype
                )
            case logging.handlers.SocketHandler:
                handler = __get_socket_handler(host=host, port=port)
            case logging.handlers.WatchedFileHandler:
                handler = __get_watched_file_handler(
                    filename=filename, mode=mode, encoding=encoding, delay=delay
                )
            case _:
                handler = handler_cls()

        handler.setLevel(log_level.upper())
        return handler
