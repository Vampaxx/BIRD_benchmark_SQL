from Bird_bench_SQL import logger
from Bird_bench_SQL.pipeline.stage_1_data_ingestion import DataIngestionPipeline
from Bird_bench_SQL.pipeline.stage_02_data_splitting import DataSplittingPipeline



STAGE_NAME = "Data ingestion stage"
try:
    logger.info("<<<____stage____{STAGE_NAME}____started >>>")
    obj = DataIngestionPipeline()
    obj.main()
    logger.info("<<<____stage____{STAGE_NAME}____starcompleted \n\n===========================================>>>")

except Exception as e:
    raise e

STAGE_NAME = "Data splitting stage"
try:
    logger.info(f"<<<    stage   {STAGE_NAME}    started >>>")
    obj = DataSplittingPipeline()
    obj.main()
    logger.info(f"<<<    stage   {STAGE_NAME}    starcompleted \n\n===========================================>>>")

except Exception as e:
    raise e
        