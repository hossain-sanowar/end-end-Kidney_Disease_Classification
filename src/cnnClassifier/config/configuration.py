from cnnClassifier.constants import *
from cnnClassifier.utils.common import read_yaml, create_directories
from cnnClassifier.entity.config_entity import DataIngestionConfig

class ConfigurationManager:
    def __init__(self, 
                 config_filepath = CONFIG_FILE_PATH, #data source and destination
                 params_filepath =PARAMS_FILE_PATH): #hyperparameter
        
        self.config=read_yaml(config_filepath) #read data by yaml
        self.params=read_yaml(params_filepath) #read hyperparameter by yaml
    
        create_directories([self.config.artifacts_root]) #create artifacts folder
    
    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config=self.config.data_ingestion #taking input from config file as source data
        
        create_directories([config.root_dir])#??
        
        data_ingestion_config = DataIngestionConfig( #copy data from DataIngestionConfig
            root_dir=config.root_dir,
            source_URL=config.source_URL,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir
        )
        
        return data_ingestion_config