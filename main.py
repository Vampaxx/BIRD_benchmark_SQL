from Bird_bench_SQL import logger
from Bird_bench_SQL.pipeline.stage_1_data_ingestion import DataIngestionPipeline
from Bird_bench_SQL.pipeline.stage_02_data_splitting import DataSplittingPipeline
from Bird_bench_SQL.pipeline.stage_03_database_and_model import DatabaseAndModelPipeline



STAGE_NAME = "Data ingestion stage"

try:
    logger.info(f"<<<____stage____{STAGE_NAME}____started >>>")
    obj = DataIngestionPipeline()
    obj.main()
    logger.info(f"<<<____stage____{STAGE_NAME}____starcompleted \n\n===========================================>>>")

except Exception as e:
    raise e


STAGE_NAME = "Data splitting stage"
try:
    logger.info(f"<<<____stage____{STAGE_NAME}____started >>>")
    obj = DataSplittingPipeline()
    obj.main()
    logger.info(f"<<<____stage____{STAGE_NAME}____starcompleted \n\n===========================================>>>")

except Exception as e:
    raise e


STAGE_NAME = "Database and model setup stage"      

try:
    logger.info(f"<<<____stage____{STAGE_NAME}____started >>>")
    obj = DatabaseAndModelPipeline()
    llm,conn,engine = obj.main()
    logger.info(f"<<<____stage____{STAGE_NAME}____completed \n\n===========================================>>>")

except Exception as e:
    raise e