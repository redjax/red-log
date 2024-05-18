from enum import Enum
import logging
import logging.handlers

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
