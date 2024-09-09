import os 
import random
from Bird_bench_SQL import logger
from Bird_bench_SQL.entity.config_entity import DataSplittingConfig
from Bird_bench_SQL.utils.common import load_json,save_json


class DataSplitting:

    def __init__(self,config = DataSplittingConfig):
        self.config = config

    def data_splitting(self):

        if not os.path.exists(self.config.train_file_path):
            data_file       = self.config.data_file_path
            logger.info(f"Data processing has started")
            data_file       = load_json(data_file)
            logger.info(f"{data_file} has loaded succesfully completed")
            specific_data   = []
            for data in data_file:
                if data['db_id'] == self.config.db_id_name:
                    specific_data.append(data)
            random.seed(42)
            random.shuffle(specific_data)
            total_size  = len(specific_data) 
            train_size  = int(0.7 * total_size)

            logger.info(f"{data_file} has loaded for data spiting")
            train_data  = specific_data[:train_size]
            test_data   = specific_data[train_size:]
            logger.info(f"{data_file} - data spiting completed")

            save_json(path  = self.config.train_file_path,
                      data  = train_data)
            save_json(path  = self.config.test_file_path,
                      data  = test_data)
            logger.info("data processing completed")
        else:
            logger.info(f"{self.config.data_file_path} file is already present")

