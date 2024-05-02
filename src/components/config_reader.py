import os
import sys
import json

from src.exception import CustomException
from src.logger import logging

class ConfigReader:
    def __init__(self) -> None:
        self.config_filename = 'config.json'
        self.config_filepath = 'data/input'

    def read_config(self):
        try:
            logging.info('Readinfg config file')
            config = json.load(open(os.path.join(f'{self.config_filepath}',f'{self.config_filename}')))
            return config
        except Exception as e:
            raise CustomException(e, sys)