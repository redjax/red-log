from enum import Enum
import logging
from logging.config import dictConfig

import red_log
from test_mod import test_log_levels


formatter = red_log.formatters.get_formatter(name="default", as_dict=True)
# print(f"Formatter ({type(formatter)}): {formatter}")


# log_level: int = red_log.LogLevelIntsEnum["INFO"].value
# print(f"Log level: {log_level}")
# # log.debug(f"Log level: {log_level}")

# print(f"Base logger config dict: {red_log.configs.CONFIG_DICT_BASE}")

stream_handler = red_log.handlers.get_handler(log_level="info")
print(f"Stream handler ({type(stream_handler)}): {stream_handler}")

stream_handler_dict = red_log.handlers.get_handler(log_level="info", as_dict=True)
print(f"Stream handler dict ({type(stream_handler_dict)}): {stream_handler_dict}")

file_handler = red_log.handlers.get_handler(
    name="app_file", handler_class="file", log_level="debug"
)
print(f"File handler ({type(file_handler)}): {file_handler}")

file_handler_dict = red_log.handlers.get_handler(
    name="app_log_file", handler_class="file", log_level="debug", as_dict=True
)
print(f"File handler dict ({type(file_handler_dict)}): {file_handler_dict}")

rotating_file_handler = red_log.handlers.get_handler(
    name=None, handler_class="rotatingfile", log_level="debug", filename="app.log"
)
print(f"Rotating file handler ({type(rotating_file_handler)}): {rotating_file_handler}")


rotating_file_handler_dict = red_log.handlers.get_handler(
    name=None, handler_class="rotatingfile", log_level="debug", filename="app.log"
)
print(
    f"Rotating file handler dict ({type(rotating_file_handler_dict)}): {rotating_file_handler_dict}"
)
