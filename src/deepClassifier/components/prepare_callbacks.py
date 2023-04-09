from deepClassifier.entity import PrepareCallbackConfig
import os
import tensorflow as tf
import time

class PrepareCallback:
    def __init__(self, config: PrepareCallbackConfig):
        self.config = config

    @property
    def _create_tb_callbacks(self):   #tensorboard callbacks
        timestamp = time.strftime("%Y-%m-%d-%H-%M-%S")  #good practice to create folders with timestamp names as they are unique
        tb_running_log_dir = os.path.join(self.config.tensorboard_log_dir,(f"tb_logs_at_{timestamp}"))
        return tf.keras.callbacks.TensorBoard(log_dir=tb_running_log_dir)

    @property
    def _create_ckpt_callbacks(self):   #checkpoint callbacks    
        return tf.keras.callbacks.ModelCheckpoint(filepath=self.config.checkpoint_model_filepath)


    def get_tb_ckpt_callbacks(self):
        return[
            self._create_tb_callbacks,   #we dont need to call a property as method i.e. with ()
            self._create_ckpt_callbacks
        ]