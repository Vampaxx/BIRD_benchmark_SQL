import sqlite3
from Bird_bench_SQL import logger
from langchain_groq import ChatGroq
from sqlalchemy import create_engine
from langchain_community.utilities import SQLDatabase
from Bird_bench_SQL.entity.config_entity import DatabaseAndModelConfig



class DatabaseAndModel:

    def __init__(self,config = DatabaseAndModelConfig):
        self.config = config

    def database_and_model_setup(self):
        logger.info("Model setup initialized")
        llm     = ChatGroq(model        = self.config.Model_name,
                           temperature  = self.config.temperature,
                           api_key      = self.config.api_key,)
        
        logger.info(f"model----{(self.config.Model_name).split('/')[-1]}----created")
        conn    = sqlite3.connect(self.config.SQLite_database_path) 
        logger.info(f"connection----{(self.config.SQLite_database_path).split('/')[-1]}----created")

        engine  = create_engine(f"sqlite:///{self.config.SQLite_database_path}")
        logger.info(f"engine----{(self.config.SQLite_database_path).split('/')[-1]}----created")

        db      = SQLDatabase(engine) 
        logger.info(f"database----created")
        return llm,conn,db 
