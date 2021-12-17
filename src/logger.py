# -*- coding: utf-8 -*-

import logging.config
from pathlib import Path

import yaml

from resources.properties import LOGS_FOLDER, LOGS_LEVEL, LOGS_MODE

file_path = Path(__file__).absolute()
root_folder = file_path.parent.parent
path_log_folder = Path(root_folder).joinpath(LOGS_FOLDER)
path_log_config_file = Path(root_folder).joinpath('resources').joinpath('log.yaml')


class InfoFilter(logging.Filter):
    def __init__(self):
        super().__init__()

    def filter(self, record):
        return record.levelno == logging.INFO


class WarningFilter(logging.Filter):
    def __init__(self):
        super().__init__()

    def filter(self, record):
        return record.levelno == logging.WARNING


class ErrorFilter(logging.Filter):
    def __init__(self):
        super().__init__()

    def filter(self, record):
        return record.levelno == logging.ERROR


class CriticalFilter(logging.Filter):
    def __init__(self):
        super().__init__()

    def filter(self, record):
        return record.levelno == logging.CRITICAL


def create_logs_folder() -> bool:
    if not Path(path_log_folder).exists():
        try:
            Path(path_log_folder).mkdir(exist_ok=True)
            return True
        except OSError:
            print(f"Creation of the log directory '{path_log_folder}' failed")
            return False
    else:
        return True


def setup_logging() -> None:
    if create_logs_folder():
        if Path(path_log_config_file).exists():
            if Path(path_log_config_file).is_file():
                with open(path_log_config_file, 'rt') as config_file:
                    config = yaml.safe_load(config_file.read())
                    logging.config.dictConfig(config)
            else:
                print(f"The path to the log configuration file must be a file not a directory: {path_log_config_file}")
        else:
            print(f"The path to the log configuration file do not exist: {path_log_config_file}")
    else:
        print(f"An error occurred while trying to configure the logging system")


logger = logging.getLogger(LOGS_MODE)
logger.setLevel(LOGS_LEVEL)
