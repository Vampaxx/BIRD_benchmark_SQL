from Bird_bench_SQL import logger
from Bird_bench_SQL.config.configuration import ConfigurationManager
from Bird_bench_SQL.components.data_splitting import DataSplitting




STAGE_NAME = "Data splitting stage"


class DataSplittingPipeline:
    def __init__(self):
        pass 
    def main(self):
        try:
            config                  = ConfigurationManager()
            data_splitting_config  = config.get_data_splitting_config()
            data_splitting          = DataSplitting(config=data_splitting_config)
            data_splitting.data_splitting()

        except Exception as e:
            raise e
        

if __name__ == "__main__":
    try:
        logger.info(f"<<<    stage   {STAGE_NAME}    started >>>")
        obj = DataSplittingPipeline()
        obj.main()
        logger.info(f"<<<    stage   {STAGE_NAME}    starcompleted \n\n===========================================>>>")

    except Exception as e:
        raise e
        


