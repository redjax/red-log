from __future__ import annotations

DEFAULT_ROOT_LOGGER: dict = {
    "": {
        "handlers": ["console"],
        ## Hide all but warning/errors on root logger
        "level": "NOTSET",
    }
}

SILENT_LOGGER: dict = {"silent": {"level:" "NOTSET"}}
