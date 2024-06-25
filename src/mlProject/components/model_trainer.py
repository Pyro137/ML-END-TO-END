from src.mlProject.config.configuration import ModelTrainerConfig
from sklearn.linear_model import ElasticNet,Ridge,Lasso
import pandas as pd
import os 
import joblib

class ModelTrainer:
    def __init__(self,config:ModelTrainerConfig):
        self.config=config


    def ModelTrain(self):
       test= pd.read_csv(self.config.test_path)
       train= pd.read_csv(self.config.train_path)

       test_x=test.drop([self.config.target_column],axis=1)
       test_y=test[[self.config.target_column]]
       train_x=train.drop([self.config.target_column],axis=1)
       train_y=train[[self.config.target_column]]

       models = {
            "ElasticNet": ElasticNet(alpha=self.config.alpha),
            "Ridge": Ridge(alpha=self.config.alpha),
            "Lasso": Lasso(alpha=self.config.alpha)
        }
       for model_name, model in models.items():
            
            model.fit(train_x, train_y)
            model_filename = os.path.join(self.config.root_dir, f"{model_name}_{self.config.model_name}")
            joblib.dump(model, model_filename)
           

       

    
