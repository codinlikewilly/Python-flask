import logging
import os
from logging.handlers import RotatingFileHandler

BASE_DIR = str(pathlib.Path(__file__).parent.parent.resolve())

LOG_DIR = (os.path.join(BASE_DIR, "logs"))
LOG_FORMATTER = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
LOG_HANDLER = RotatingFileHandler(LOG_DIR + '/log.log', maxBytes=10000, backupCount=1)


def get_file_handler():
    log_file_handler = LOG_HANDLER
    log_file_handler.setFormatter(LOG_FORMATTER)
    return log_file_handler


def get_logger(logger_name):
    logger = logging.getLogger(logger_name)
    logger.addHandler(get_file_handler())
    logger.setLevel(logging.DEBUG)
    return logger
