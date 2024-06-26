from src.mlProject.config.configuration import ConfigurationManager
from src.mlProject.components.model_trainer import ModelTrainer



class ModelTrainerPipeline:
    def __init__(self):
        pass
    
    def main(self):
        config_manager=ConfigurationManager()
        config_trainer=config_manager.get_model_trainer_config()
        model_trainer=ModelTrainer(config=config_trainer)
        model_trainer.train()
