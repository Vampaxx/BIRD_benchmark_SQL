from Bird_bench_SQL import logger
from Bird_bench_SQL.config.configuration import ConfigurationManager
from Bird_bench_SQL.components.data_ingestion import DataIngestion



STAGE_NAME = "Data ingestion stage"


class DataIngestionPipeline:
    def __init__(self):
        pass 
    def main(self):
        try:
            config                  = ConfigurationManager()
            data_ingestion_config   = config.get_data_ingestion_config()
            data_ingestion          = DataIngestion(config=data_ingestion_config)
            data_ingestion.download_file()

        except Exception as e:
            raise e
        

if __name__ == "__main__"    :
    try:
        logger.info("<<<    stage   {STAGE_NAME}    started >>>")
        obj = DataIngestionPipeline()
        obj.main()
        logger.info("<<<    stage   {STAGE_NAME}    starcompleted \n\n===========================================>>>")

    except Exception as e:
        raise e
        
