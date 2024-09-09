from pathlib import Path
from typing import Optional
from dataclasses import dataclass


@dataclass(frozen=True)
class DataIngestionConfig:
    SQLite_URL      : str
    SQLite_dir      : Path
    SQLite_file     : Path
    data_URL        : str 
    data_dir        : Path
    data_file_path  : Path


@dataclass(frozen=True)
class DataSplittingConfig:
    data_file_path  : Path
    train_file_path : Path
    test_file_path  : Path 
    db_id_name      : str 
    train_size      : int
    test_size       : int


@dataclass(frozen=True)
class DatabaseAndModelConfig:
    SQLite_database_path    : str
    Model_name              : str 
    temperature             : int 
    api_key                 : Optional[str]
