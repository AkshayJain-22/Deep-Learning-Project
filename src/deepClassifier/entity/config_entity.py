from dataclasses import dataclass
from pathlib import Path
import time
import tensorflow as tf

@dataclass(frozen=True) 
class DataIngestionConfig:      #this will also work as a named tuple but is a better way to implement the same concept
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path

@dataclass(frozen=True) 
class PrepareBaseModelConfig:      #this will also work as a named tuple but is a better way to implement the same concept
    root_dir: Path
    base_model_path: Path
    updated_base_model_path: Path
    params_image_size: list
    params_include_top: bool
    params_learning_rate: float
    params_weights: str
    params_classes:int

@dataclass(frozen=True) 
class PrepareCallbackConfig:      #this will also work as a named tuple but is a better way to implement the same concept
    root_dir: Path
    tensorboard_log_dir: Path
    checkpoint_model_filepath: Path

    
@dataclass(frozen=True) 
class TrainingConfig:      #this will also work as a named tuple but is a better way to implement the same concept
    root_dir: Path
    trained_model_path: Path
    updated_base_model_path: Path
    training_data: Path
    params_epochs: int
    params_batch_size: int
    params_is_augmentation: bool
    params_image_size: list