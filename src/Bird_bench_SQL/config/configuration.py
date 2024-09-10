import os
from dotenv import load_dotenv
from Bird_bench_SQL import logger
from Bird_bench_SQL.constants import *
from Bird_bench_SQL.utils.common import read_yaml, create_directories
from Bird_bench_SQL.entity.config_entity import (DataIngestionConfig,
                                                 DataSplittingConfig,
                                                 DatabaseAndModelConfig,
                                                 DataProcessingConfig)
                                                #PrepareBaseModelConfig,
                                                #PrepareCallbacksConfig,
                                                #TrainingConfig,
                                                #EvaluationConfig)




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
    

    def get_data_splitting_config(self) -> DataSplittingConfig:

        config =  self.config.data_splitting
        params = self.params 
        logger.info('Data splitting initialized')
        data_procesing_config = DataSplittingConfig(data_file_path     = config.data_file_path,
                                                     train_file_path    = config.train_file_path,
                                                     test_file_path     = config.test_file_path,
                                                     db_id_name         = params.db_id,
                                                     train_size         = params.TRAIN_SIZE,
                                                     test_size          = params.TEST_SIZE) 
        return data_procesing_config
    

    def get_database_and_model_config(self) -> DatabaseAndModelConfig:
        config = self.config.database_and_model
        params = self.params 
        
        logger.info('Database and model config initialized')
        load_dotenv()
        data_procesing_config = DatabaseAndModelConfig(SQLite_database_path = config.database_path,
                                                       Model_name           = params.MODEL_NAME,
                                                       temperature          = params.TEMPERATURE,
                                                       api_key              = os.getenv("GROQ_API_KEY")) 
        logger.info("database and model config finished") 
        return data_procesing_config   
    

    def get_data_processing_config(self) -> DataProcessingConfig:
        config =  self.config.data_processing
        params = self.params 
        logger.info('Data preprocessing config initialized')
        data_procesing_config = DataProcessingConfig(data_file_path     = config.data_file_path,
                                                     train_file_path    = config.train_file_path,
                                                     test_file_path     = config.test_file_path,
                                                     few_shot_file_path = config.few_shots_path,
                                                     few_shot_file_size = params.FEW_SHOTS_SIZE,
                                                     db_id_name         = params.db_id,
                                                     k                  = params.K,
                                                     embedding_model    = params.EMBEDDING_MDOEL
                                                     )
        logger.info('Data preprocessing config finished')
        return data_procesing_config        
             
    


    
if __name__ == "__main__":
    try:
        config                      = ConfigurationManager()
        data_processing_config      = config.get_data_splitting_config()
        processing_config           = config.get_data_processing_config()
        model_config                = config.get_database_and_model_config()

        train_path          = processing_config.train_file_path
        test_path           = processing_config.test_file_path

    except Exception as e:
        raise e