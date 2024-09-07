
import os
from pathlib import Path
from Bird_bench_SQL.constants import *
from Bird_bench_SQL.utils.common import read_yaml, create_directories
from Bird_bench_SQL.entity.config_entity import (DataIngestionConfig,)
                                                #PrepareBaseModelConfig,
                                                #PrepareCallbacksConfig,
                                                #TrainingConfig,
                                                #EvaluationConfig)
from Bird_bench_SQL.components.data_ingestion import DataIngestion



class ConfigurationManager:
    def __init__(self,
                 config_filepath    = CONFIG_FILE_PATH,
                 params_filepath    = PARAMS_FILE_PATH):
        
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)
        create_directories([self.config.artifacts_root])

    def get_data_ingestion_config(self)->DataIngestionConfig:

        config      = self.config.data_ingestion
        create_directories([config.SQLite_dir,config.data_dir])

        data_ingestion_config= DataIngestionConfig(SQLite_URL       = config.SQLite_URL,
                                                   SQLite_dir       = config.SQLite_dir,
                                                   SQLite_file      = config.SQLite_file,
                                                   data_URL         = config.data_URL,
                                                   data_dir         = config.data_dir,
                                                   data_file_path   = config.data_file_path)
        return data_ingestion_config
    


    
if __name__ == "__main__":
    try:
        config                  = ConfigurationManager()
        data_ingestion_config   = config.get_data_ingestion_config()
        data_ingestion          = DataIngestion(config=data_ingestion_config)
        data_ingestion.download_file()

    except Exception as e:
        raise e