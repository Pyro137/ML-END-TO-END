from src.mlProject.config.configuration import ConfigurationManager
from src.mlProject.components.data_validation import Datavalidation
from src.mlProject.logging import logging



class DataValidationPipeline:
    def __init__(self) -> None:
        pass
    
    def main(self):
        config_manager=ConfigurationManager()
        config=config_manager.get_data_validation_config()
        data_validate=Datavalidation(config=config)
        data_validate.validate_all_columns()




if __name__=="__main__":
    try:
        data_validation_pipeline=DataValidationPipeline()
        data_validation_pipeline.main()

    except Exception as e:
        raise e            
        