from src.mlProject.config.configuration import ConfigurationManager
from src.mlProject.components.data_validation import Datavalidation




class DataValidationPipeline:
    def __init__(self) -> None:
        pass
    
    def main(self):
        config_manager=ConfigurationManager()
        config=config_manager.get_data_validation_config()
        data_validate=Datavalidation(config=config)
        data_validate.validate_all_columns()



