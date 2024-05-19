import typing as t
import ssl
import queue
from enum import Enum
import logging
import logging.handlers

from ._enums import HandlerObjectsEnum

VALID_HANDLER_CLASSES: list[logging.Handler] = [
    logging.FileHandler,
    logging.NullHandler,
    logging.StreamHandler,
    logging.handlers.RotatingFileHandler,
    logging.handlers.TimedRotatingFileHandler,
    logging.handlers.QueueListener,
    logging.handlers.QueueHandler,
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


def validate_parameters(
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
) -> tuple:  # -> t.Union[
    #     t.Tuple[
    #         str,
    #         str | None,
    #         int | None,
    #         int | None,
    #         str | None,
    #         bool,
    #         str,
    #         str,
    #         str | None,
    #         str,
    #         str | None,
    #         bool,
    #         str | None,
    #         t.Union[str, t.Tuple[str, int]],
    #         int,
    #         int | None,
    #         t.Union[str, t.Tuple[str, int]] | None,
    #         str | None,
    #         t.Union[str, list] | None,
    #         str | None,
    #         tuple | None,
    #         tuple | None,
    #         float | None,
    #         int | None,
    #         str | None,
    #         int | None,
    #         str,
    #         bool,
    #         ssl.SSLContext | None,
    #         str | None,
    #         str | None,
    #         str,
    #         queue.Queue | None,
    #     ],
    #     HandlerType | None,
    # ]:
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
