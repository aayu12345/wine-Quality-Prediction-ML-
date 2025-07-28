import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO , format='[%(asctime)s]: %(message)s')
project_name="ml_project"

LIST_OF_FILES=[
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/componenets/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/entity/config_entity.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "schema.yaml",
    "main.py",
    "app.py",
    "requirements.txt",
    "setup.py",
    "research/trial.ipynb",
    "templates/index.html",
]

for filepath in LIST_OF_FILES:
    filepath=Path(filepath)
    file_dir, file_name=os.path.split(filepath)
    if file_dir !="":
        os.makedirs(file_dir, exist_ok=True)
        logging.info(f"Creating directory: {file_dir} for the file: {file_name}")

    if (not os.path.exists(filepath)) or((os.path.getsize(filepath) == 0)):
        with open(filepath, 'w') as f:
            pass
        logging.info(f"Creating empty file: {file_name} at {file_dir}")

    else:
        logging.info(f"File already exists: {file_name}")        