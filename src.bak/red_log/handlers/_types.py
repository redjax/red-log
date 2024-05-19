import typing as t
import logging
import logging.handlers

HandlerType = t.Union[
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
