from src.mlProject.config.configuration import ConfigurationManager
from src.mlProject.components.model_evaluation import ModelEvaluation



class ModelEvaluationPipeline:
    def __init__(self) -> None:
        pass

    def main(self):
        config_manager=ConfigurationManager()
        config=config_manager.get_model_evaluation_config()
        model_evaluate=ModelEvaluation(config=config)
        model_evaluate.save_results()