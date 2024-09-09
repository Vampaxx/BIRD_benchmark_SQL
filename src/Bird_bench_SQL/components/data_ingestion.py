import os
import urllib.request as request
from Bird_bench_SQL import logger
from Bird_bench_SQL.entity.config_entity import DataIngestionConfig


class DataIngestion:

    def __init__(self,config = DataIngestionConfig):
        self.config = config
        
    def download_file(self):

        if not os.path.exists(self.config.SQLite_file):
            logger.info(f"Downloading SQLite file from {self.config.SQLite_URL} to {self.config.SQLite_dir}")
            filename, header = request.urlretrieve(url      = self.config.SQLite_URL, 
                                                   filename = self.config.SQLite_file)
            logger.info(f"{filename} downloaded with the following info: \n{header}")
        else:
            logger.info(f"{self.config.SQLite_file} already exists, skipping download.")

        # Download data file if it doesn't exist
        if not os.path.exists(self.config.data_file_path):
            logger.info(f"Downloading data file from {self.config.data_URL} to {self.config.data_dir}")
            filename, header = request.urlretrieve(url      = self.config.data_URL,
                                                   filename = self.config.data_file_path)
            logger.info(f"{filename} downloaded with the following info: \n{header}")
        else:
            logger.info(f"{self.config.data_dir} already exists, skipping download.")




