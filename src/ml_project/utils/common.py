import os
from box.exceptions import BoxValueError
import yaml
from ml_project import logger 
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any


@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """
    Reads a YAML file and return a Configbox object

    Args:
        path_to_yaml (str): Path like input

    Raises:
         ValueError: if yaml file is empty
         e:empty file

    Returns:
        ConfigBox: ConfigBox object containing the YAML data          

    """

    try:
        with open(path_to_yaml) as yaml_file:
            content=yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
        
    except BoxValueError:
        raise ValueError(f"Yaml file: {path_to_yaml} is empty")
    except Exception as e:
        raise e

@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """
    Create list of directories
    Args:
        path_to_directories (list): List of directories
        ignore_log (bool,optional): ignore if multiple directories is to be created 
        
    """  
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"created directory at: {path}")


@ensure_annotations
def save_json(path: Path, data: dict):
    """
    Save json data
    Args:
        path (Path): Path to json file
        data (dict): data to be saved in a json file
    """
    with open(path, "w") as f:
        json.dump(data, f,indent=4)

    logger.info(f"json file saved at: {path}")


@ensure_annotations
def load_json(path: Path) -> ConfigBox:

    """
    Args:
        path (Path): Path to json file
        
    Returns:
        ConfigBox: data as class attributes instead of dict
    """

    with open(path) as f:
        content=json.load(f)

    logger.info(f"json file loaded successfully from: {path}")
    return ConfigBox(content)

@ensure_annotations
def save_bin(data:Any, path:Path):
    """
    Save data in binary format using joblib
    
    Args:
        data (Any) : Data to be saved a s binary
        path(Path): path to save the binary file
        
    """

    joblib.dump(value=data, filename=path)
    logger.info(f"binary file saved at: {path}")

@ensure_annotations
def load_bin(path:Path) -> Any:
    """
    load binary data
    Args:
        path (Path): Path to binary file

    Returns:
        Any: object stored in the file

    """ 
    data=joblib.load(path)
    logger.info(f"binary file loaded from: {path}")
    return data

@ensure_annotations
def get_size(path:Path) -> str:
    """
    Get size in KB
    Args:
        path (Path): Path to file or directory
        
    Returns:
        str:Size in KB
    """
    size_in_kb=round(os.path.getsize(path)/1024)
    return f"~ {size_in_kb} KB"
                                 
