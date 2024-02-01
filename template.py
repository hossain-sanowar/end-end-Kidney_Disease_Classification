#create the file amd folder for the project
import os
from pathlib import Path
import logging


#logging strings
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]:%(message)s:%(levelname)s:')

project_name='cnnClassifier'

#just follow the Keras structure. here we are using "src" instead of "Keras"
list_of_files = [
    ".github/workflows/.gitkeep", #if folder is empty then github won't update because of .gitkeep
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    "templates/index.html",
    'test.py'

]

for filepath in list_of_files:
    filepath = Path(filepath) # path is used for any kind of operating system like Windows, mac and linux
    filedir, filename = os.path.split(filepath)#separate folder and file


    if filedir !="": #folder is already present, it won't be created
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory; {filedir} for the file: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0): #not exist filepath or file size is zero
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating empty file: {filepath}")


    else:
        logging.info(f"{filename} is already exists")
