from src.mlProject.config.configuration import ConfigurationManager
from src.mlProject.components.data_transformation import DataTransformation

from pathlib import Path

STAGE_NAME="DATA TRANSFORMATİON STAGE"

class DataTransformationPipeline:
    def __init__(self):
        pass
    def main(self):
        try:
            with open(Path("artifacts/data_validation/status.txt")) as file:
                status=file.read().split(" ")[-1]

            if status=="True":
                config=ConfigurationManager()
                data_transformation_config=config.get_data_transformation_config()
                data_transformation=DataTransformation(data_transformation_config)
                data_transformation.train_test_split()
            else:
                raise Exception("Data transformation occured error")



        except Exception as e:     
            raise e