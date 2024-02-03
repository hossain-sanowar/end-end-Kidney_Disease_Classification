from dataclasses import dataclass
from pathlib import Path

#data Ingestion entity
@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir:Path #these are the access of variable from the other class
    source_URL: str
    local_data_file: Path
    unzip_dir: Path
    
#prepare model based like VGG16
@dataclass(frozen=True)
class PrepareBaseModelConfig:
    root_dir: Path
    base_model_path: Path
    updated_base_model_path: Path
    params_image_size: list
    params_learning_rate: float
    params_include_top: bool
    params_weights: str
    params_classes: int
    
    
#model training

@dataclass(frozen=True)
class TrainingConfig:
    root_dir:Path
    trained_model_path:Path
    updated_base_model_path:Path
    training_data:Path
    params_epochs:int
    params_batch_size:int
    params_is_augmentation:bool
    params_image_size:list
    
    