import logging


logger = logging.getLogger("root")
DEBUG = logging.DEBUG
INFO = logging.INFO


def setup_log_level(level=INFO):
    logging.basicConfig(level=level)
