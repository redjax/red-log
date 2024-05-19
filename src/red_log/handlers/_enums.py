import logging
import logging.handlers
from enum import Enum


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
