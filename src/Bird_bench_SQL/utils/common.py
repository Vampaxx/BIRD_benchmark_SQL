import os
import yaml
import json

from ensure import ensure_annotations

from box.exceptions import BoxValueError
from Bird_bench_SQL import logger,logging
from box import ConfigBox
from pathlib import Path
from typing import Any
import base64



@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e
    


@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"created directory at: {path}")


@ensure_annotations
def save_json(path:str, data: list):
    with open(Path(path), "w") as f:
        json.dump(data, f, indent=4)

    logger.info(f"json file saved at: {path}")




@ensure_annotations
def load_json(file_path):
    with open (Path(file_path),"r") as file:
        text_sql_data = json.load(file)

    logger.info(f"json file loaded succesfully from: {file_path}")
    if isinstance(text_sql_data, list):  # Ensuring the content is a list of dictionaries
        wrapped_content = [ConfigBox(item) for item in text_sql_data]
    return wrapped_content




