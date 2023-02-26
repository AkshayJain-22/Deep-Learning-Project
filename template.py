import os
from pathlib import Path    # to convert he filapath in correct format
import logging

logging.basicConfig(level = logging.INFO, format = '[%(asctime)s]: %(message)s: ')

package_name = "deepClassifier"

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{package_name}/__init__.py",
    f"src/{package_name}/components/__init__.py",
    f"src/{package_name}/utils/__init__.py",
    f"src/{package_name}/config/__init__.py",
    f"src/{package_name}/pipeline/__init__.py",
    f"src/{package_name}/entity/__init__.py",
    f"src/{package_name}/artifacts/__init__.py",
    "configs/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "init_setup.sh",
    "requirements.txt",
    "requirements_dev.txt",
    "setup.py",
    "setup.cfg",
    "pyproject.toml",
    "tox.ini",
    "research/trials.ipynb"
]

for filepath in list_of_files:
    filepath = Path(filepath)   # it converts the filepaths to correct format based on your OS
    filedir, filename = os.path.split(filepath)   # it gives the name of the directory and the name of the file.
    if filedir!='':     # for only filenames it givrs empty directory which will create error
        os.makedirs(filedir, exist_ok = True)
        logging.info(f'Creating directory: {filedir} for file: {filename}')
    
    if (not os.path.exists(filename)) or (os.path.getsize(filepath) == 0):
        with open(filepath,'w') as f:
            pass # just create an empty file
            logging.info(f'Creating empty file: {filepath}')
    else:
        logging.info(f'File exists: {filepath}')