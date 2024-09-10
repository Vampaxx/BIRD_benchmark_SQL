from Bird_bench_SQL import logger
from Bird_bench_SQL.config.configuration import ConfigurationManager
from Bird_bench_SQL.components.database_and_model import DatabaseAndModel




STAGE_NAME = "Database and model setup stage"


class DatabaseAndModelPipeline:
    def __init__(self):
        pass 
    def main(self):
        try:
            manager             = ConfigurationManager()
            config              = manager.get_database_and_model_config()
            datamodel_and_model = DatabaseAndModel(config=config)
            llm,conn,engine     = datamodel_and_model.database_and_model_setup()
            return llm,conn,engine
        except Exception as e:
            raise e
        

if __name__ == "__main__":
    try:
        logger.info(f"<<<    stage   {STAGE_NAME}    started >>>")
        obj = DatabaseAndModelPipeline()
        llm,conn,engine = obj.main()
        logger.info(f"<<<    stage   {STAGE_NAME}    completed \n\n===========================================>>>")

    except Exception as e:
        raise e
        


