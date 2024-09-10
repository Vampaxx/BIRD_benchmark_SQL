import os 
import random
from Bird_bench_SQL.utils.common import load_json,save_json
from Bird_bench_SQL import logger
from Bird_bench_SQL.components.database_and_model import DatabaseAndModel
from Bird_bench_SQL.config.configuration import ConfigurationManager
from Bird_bench_SQL.entity.config_entity import (DatabaseAndModelConfig,
                                                 DataProcessingConfig)


#from langchain.vectorstores import Chroma
from langchain_community.vectorstores import Chroma
#from sentence_transformers import SentenceTransformer
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.prompts import SemanticSimilarityExampleSelector



class DataProcessing(DatabaseAndModel):

    def __init__(self,processing_config : DataProcessingConfig, model_config:DatabaseAndModelConfig):
        super().__init__(model_config)
        self.processing_config          = processing_config
        self.llm, self.conn, self.db    = self.database_and_model_setup()

    def data_processing(self): 
        """if  os.path.exists(self.processing_config.few_shot_file_path):
            os.remove(self.processing_config.few_shot_file_path)
            logger.info(f"{self.processing_config.few_shot_file_path} has been deleted.")
        else:
            pass""" 

        if not os.path.exists(self.processing_config.few_shot_file_path):
            
            logger.info(f"Data processing has started")
            #data_path   = self.processing_config.data_file_path
            train_path  = self.processing_config.train_file_path
            data_file   = load_json(train_path)
            logger.info(f"{data_file} has loaded succesfully completed")

            conn = self.conn 
            cursor  = conn.cursor() 
            logger.info("----added cursor----")
            #datas = load_json(train_path)

            for data in data_file: # datas
                results         = cursor.execute(data.SQL)
                data['Answer']  = ",".join([str(ans[0]) for ans in results])
            conn.close()
            logger.info("----database closeed----")
            logger.info("----Data alternation started----")
            
            random.shuffle(data_file) # datas
            few_shots       = random.sample(data_file,self.processing_config.few_shot_file_size) # datas
            logger.info(f"----Pick {self.processing_config.few_shot_file_size} Random samples from dataset----")

            logger.info(f"----Data alternation of few shots started----")
            few_shots_data  = []
            for item in few_shots:
                new_item = {
                    "Question"  : f"{item['question']} ==>> {item['evidence']}",
                    "SQLQuery"  : item['SQL'],
                    "SQLResult" : "Result of the SQL query",  # Placeholder for the actual SQL result if needed
                    "Answer"    : item['Answer']
                }
                few_shots_data.append(new_item)
            logger.info(f"----Data alternation of few shots completed----")
            save_json(path  = self.processing_config.few_shot_file_path,
                      data  = few_shots_data)
            
        else:
            logger.info(f"{self.processing_config.few_shot_file_path} file is already present")


    def sematic_similarity_example_selector(self):
        logger.info(f"Sematic similarity example selector begin") 
        embeddings    = HuggingFaceEmbeddings(model_name=self.processing_config.embedding_model)
        logger.info(f"----Embedding model----{self.processing_config.embedding_model}----setup successfully completed") 
        to_vectorize  = [' '.join(sent.values()) for sent in load_json(self.processing_config.few_shot_file_path)]
        logger.info(f"----loaded few_shot-data from----{self.processing_config.few_shot_file_path}----") 
        vectorstore   = Chroma.from_texts(to_vectorize,embeddings,metadatas=load_json(self.processing_config.few_shot_file_path))
        logger.info("----successfully completed vectorstore----")

        example_selector = SemanticSimilarityExampleSelector(vectorstore  = vectorstore,k= self.processing_config.k,)
        return example_selector
  

try:
    manager                 = ConfigurationManager()
    model_config            = manager.get_database_and_model_config()
    data_processing_config  = manager.get_data_processing_config()
    data_processing         = DataProcessing(processing_config  = data_processing_config,
                                                model_config       = model_config)
    data_processing.data_processing()
    example_selector        = data_processing.sematic_similarity_example_selector()

except Exception as e:
    raise e