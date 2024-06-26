from src.mlProject.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from src.mlProject.pipeline.stage_02_data_validation import DataValidationPipeline
from src.mlProject.pipeline.stage_03_data_transformation import DataTransformationPipeline
from src.mlProject.pipeline.stage_04_model_trainer import ModelTrainerPipeline
from src.mlProject.pipeline.stage_05_model_evaluation import ModelEvaluationPipeline

try:
    data_ingestion_pipeline=DataIngestionTrainingPipeline()
    data_ingestion_pipeline.main()
    datavalidationpipeline=DataValidationPipeline()
    datavalidationpipeline.main()
    data_transformation=DataTransformationPipeline()
    data_transformation.main()
    model_trainer=ModelTrainerPipeline()
    model_trainer.main()
    model_evaluate=ModelEvaluationPipeline()
    model_evaluate.main()
except Exception as e: 
    raise e