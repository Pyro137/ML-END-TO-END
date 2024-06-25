from src.mlProject.components.model_trainer import ModelTrainer
from src.mlProject.config.configuration import ConfigurationManager


class ModelTrainerPipeline:
    def __init__(self) -> None:
        pass

    def main(self):
        config_manager=ConfigurationManager()
        config=config_manager.get_model_trainer_config()
        model_trainer=ModelTrainer(config=config)
        model_trainer.ModelTrain()