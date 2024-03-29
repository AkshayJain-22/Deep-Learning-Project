from deepClassifier.config import ConfigurationManager
from deepClassifier.components import PrepareCallback, Training
from deepClassifier import logger

STAGE_NAME = 'Training with callbacks'
def main():
    config = ConfigurationManager()
    prepare_callback_config = config.get_prepare_callback_config()
    prepare_callback = PrepareCallback(config=prepare_callback_config)
    callback_list = prepare_callback.get_tb_ckpt_callbacks()
    training_config = config.get_training_config()
    training = Training(config=training_config)
    training.get_base_model()
    training.train_valid_generator()
    training.train(callbacks_list=callback_list)


if __name__ == '__main__':
    try:
        logger.info(f'>>>>> stage {STAGE_NAME} started <<<<<')
        main()
        logger.info(f'>>>>> stage {STAGE_NAME} completed <<<<<\n\n=================')
    except Exception as e:
        logger.exception(e)
        raise e