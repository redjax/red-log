import typing as t
from pathlib import Path

import logging
import logging.handlers


class HandlerFactory:
    @staticmethod
    def create_stream_handler(
        level: t.Union[int, str] = logging.DEBUG,  # Set default level to DEBUG
        formatter: logging.Formatter | None = None,
    ) -> logging.StreamHandler:
        level = HandlerFactory._get_log_level(level)
        handler = logging.StreamHandler()
        handler.setLevel(level)
        if formatter:
            handler.setFormatter(formatter)
        return handler

    @staticmethod
    def create_file_handler(
        filename: str,
        level: t.Union[int, str] = logging.DEBUG,  # Set default level to DEBUG
        formatter: logging.Formatter | None = None,
    ) -> logging.FileHandler:

        if not Path(f"{filename}").parent.exists():
            try:
                Path(f"{filename}").parent.mkdir(exist_ok=True, parents=True)
            except Exception as exc:
                msg = Exception(
                    f"Unhandled exception creating logging parent directory '{Path(f'{filename}').parent}. Details: {exc}"
                )
                # log.error(msg)

                raise exc

        level = HandlerFactory._get_log_level(level)
        handler = logging.FileHandler(filename)
        handler.setLevel(level)
        if formatter:
            handler.setFormatter(formatter)
        return handler

    @staticmethod
    def _get_log_level(level: t.Union[int, str]) -> int:
        if isinstance(level, str):
            level = level.upper()
            return logging._nameToLevel.get(level, logging.INFO)
        return level
