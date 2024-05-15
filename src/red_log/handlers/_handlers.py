from __future__ import annotations

CONSOLE_HANDLER: dict = {
    "console": {
        "class": "logging.StreamHandler",
        "formatter": "default",
        "level": "DEBUG",
        "stream": "ext://sys.stdout",
    }
}

CLI_CONSOLE_HANDLER: dict = {
    "cli": {
        "class": "logging.StreamHandler",
        "formatter": "default",
        "level": "WARNING",
        "stream": "ext://sys.stdout",
    }
}

APP_FILE_HANDLER: dict = {
    "app_file": {
        "formatter": "default",
        "class": "logging.FileHandler",
        "level": "INFO",
        "filename": "app.log",
    }
}

ERR_FILE_HANDLER: dict = {
    "err_file": {
        "formatter": "default",
        "class": "logging.FileHandler",
        "level": "INFO",
        "filename": "app.log",
    }
}

ROTATING_FILE_HANDLER: dict = {
    "rotating_app_file": {
        "class": "logging.handlers.RotatingFileHandler",
        "filename": "app.log",
        ## 2MB
        "maxBytes": 2000000,
        "backupCount": 10,
        "formatter": "default",
        "level": "DEBUG",
    }
}

ROTATING_ERR_FILE_HANDLER: dict = {
    "rotating_erer_file": {
        "class": "logging.handlers.RotatingFileHandler",
        "filename": "err.log",
        ## 2MB
        "maxBytes": 2000000,
        "backupCount": 10,
        "formatter": "default",
        "level": "DEBUG",
    }
}

TIMED_ROTATING_FILE_HANDLER: dict = {
    "class": "logging.handlers.RotatingFileHandler",
    "filename": "app.log",
    "when": "midnight",
    "backupCount": 10,
    "formatter": "std_out",
    "level": "DEBUG",
}
