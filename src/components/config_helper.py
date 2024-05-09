import os
import sys
import json

from src.exception import CustomException
from src.logger import logging

import pandas as pd

class Config:
    def __init__(self):
        self.config_filepath = 'data/input'
        self.output_filepath = 'data/output'

    def read_config(self, filename):
        try:
            logging.info(f'Reading JSON file: {filename}')
            file_data = json.load(open(os.path.join(self.config_filepath, filename)))
            return file_data
        except Exception as e:
            raise CustomException(e, sys)
        
    def read_csv(self, filename):
        try:
            logging.info(f'Reading CSV file: {filename}, as dataframe')
            file_data = pd.read_csv(os.path.join(self.config_filepath, filename))
            return file_data
        except Exception as e:
            raise CustomException(e, sys)
        
    def write_json(self, result, filename):
        #TODO write details to json
        try:
            with open(os.path.join(self.output_filepath, filename), "w") as outfile: 
                json.dump(result, outfile)
        except Exception as e:
            raise CustomException(e, sys)
        pass