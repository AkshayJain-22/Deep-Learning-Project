from dataclasses import dataclass
from pathlib import Path

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