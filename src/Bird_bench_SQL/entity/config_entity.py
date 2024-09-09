from dataclasses import dataclass
from pathlib import Path


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
