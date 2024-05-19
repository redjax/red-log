DEFAULT_FMT: str = (
    "[%(asctime)s] [%(levelname)s] > [%(filename)s:%(lineno)d] [%(funcName)s]: %(message)s"
)
DEFAULT_SIMPLE_FMT: str = (
    "[%(asctime)s] [%(levelname)s] > [%(filename)s:%(lineno)d]: %(message)s"
)
DEFAULT_DETAIL_FMT: str = (
    "[%(astime)s] [Logger:%(name)s] [pid:%(process)d] [procname:%(processName)s] [%(levelname)s] [module:%(module)s] > [%(filename)s.%(funcname)s:%(lineno)d]: %(message)s"
)

DEFAULT_DATE_FMT: str = "%Y-%m-%d %H:%M:%S"

DEFAULT_LOGGER_STYLE: str = "%"
