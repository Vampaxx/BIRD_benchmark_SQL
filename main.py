from Bird_bench_SQL import logger
from Bird_bench_SQL.pipeline.stage_1_data_ingestion import DataIngestionPipeline


STAGE_NAME = "Data ingestion stage"
try:
    logger.info("<<<____stage____{STAGE_NAME}____started >>>")
    obj = DataIngestionPipeline()
    obj.main()
    logger.info("<<<____stage____{STAGE_NAME}____starcompleted \n\n===========================================>>>")

except Exception as e:
    raise e

