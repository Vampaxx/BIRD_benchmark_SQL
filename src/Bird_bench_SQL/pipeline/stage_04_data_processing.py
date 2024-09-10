from Bird_bench_SQL import logger
from Bird_bench_SQL.config.configuration import ConfigurationManager
from Bird_bench_SQL.components.data_processing import DataProcessing




STAGE_NAME = "Data processing stage"


class DataProcessingPipeline:
    def __init__(self):
        pass 
    def main(self):
        try:
            manager                 = ConfigurationManager()
            model_config            = manager.get_database_and_model_config()
            data_processing_config  = manager.get_data_processing_config()
            data_processing         = DataProcessing(processing_config  = data_processing_config,
                                                        model_config       = model_config)
            data_processing.data_processing()
            example_selector        = data_processing.sematic_similarity_example_selector()
            return example_selector
        except Exception as e:
            raise e
        

if __name__ == "__main__":
    try:
        logger.info(f"<<<    stage   {STAGE_NAME}    started >>>")
        obj = DataProcessingPipeline()
        example_selector = obj.main()
        print(len(example_selector.select_examples({'question': "What are the genres of Sky Captain ",})))
        logger.info(f"<<<    stage   {STAGE_NAME}    completed \n\n===========================================>>>")

    except Exception as e:
        raise e
        


