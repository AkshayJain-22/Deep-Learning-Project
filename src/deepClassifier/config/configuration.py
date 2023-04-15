from deepClassifier.constants import *
from deepClassifier.utils import read_yaml, create_directories
from deepClassifier.entity import DataIngestionConfig, PrepareBaseModelConfig, PrepareCallbackConfig, TrainingConfig, EvaluationConfig
from pathlib import Path
import os

class ConfigurationManager:
    def __init__(
        self, config_filepath = CONFIG_FILE_PATH,params_filepath = PARAMS_FILE_PATH):
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)
        create_directories([self.config.artifacts_root])

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion
        
        create_directories([config.root_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            source_URL=config.source_URL,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir 
        )

        return data_ingestion_config
    
    def get_prepare_base_model_config(self) -> PrepareBaseModelConfig:
        config = self.config.prepare_base_model
        
        create_directories([config.root_dir])

        prepare_base_model_config = PrepareBaseModelConfig(
            root_dir=Path(config.root_dir),
            base_model_path=Path(config.base_model_path),
            updated_base_model_path=Path(config.updated_base_model_path),
            params_image_size= self.params.IMAGE_SIZE,
            params_include_top= self.params.INCLUDE_TOP,
            params_learning_rate= self.params.LEARNING_RATE,
            params_weights = self.params.WEIGHTS,
            params_classes = self.params.CLASSES
        )

        return prepare_base_model_config
    
    def get_prepare_callback_config(self) -> PrepareCallbackConfig:
        config = self.config.prepare_callback
        model_ckpt_dir= os.path.dirname(config.checkpoint_model_filepath)   #since it has a filename in the end of filepath
        create_directories([Path(model_ckpt_dir),Path(config.tensorboard_log_dir)])

        prepare_callback_config = PrepareCallbackConfig(
            root_dir = Path(config.root_dir),
            tensorboard_log_dir = Path(config.tensorboard_log_dir),
            checkpoint_model_filepath = Path(config.checkpoint_model_filepath))

        return prepare_callback_config

    def get_training_config(self) -> TrainingConfig:
        config_training = self.config.training
        model_config = self.config.prepare_base_model
        training_data = os.path.join(self.config.data_ingestion.unzip_dir,"PetImages")
        params = self.params

        create_directories([Path(config_training.root_dir)])

        training_config = TrainingConfig(
            root_dir = Path(config_training.root_dir),
            trained_model_path= Path(config_training.trained_model_path),
            updated_base_model_path= Path(model_config.updated_base_model_path),
            training_data= Path(training_data),
            params_epochs = params.EPOCHS,
            params_batch_size = params.BATCH_SIZE,
            params_is_augmentation= params.AUGMENTATION,
            params_image_size= params.IMAGE_SIZE)
        return training_config
    
    def get_validation_config(self)-> EvaluationConfig:
        eval_config = EvaluationConfig(
            path_of_model=self.config.training.trained_model_path,
            training_data=self.config.data_ingestion.unzip_dir,
            params_image_size=self.params.IMAGE_SIZE,
            params_batch_size=self.params.BATCH_SIZE,
        )
        return eval_config