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
