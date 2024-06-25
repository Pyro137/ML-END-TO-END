from sklearn.model_selection import train_test_split
import pandas as pd
import os
from src.mlProject.config.configuration import DataTransformationConfig
from sklearn.preprocessing import StandardScaler



class DataTransformation:
    def __init__(self,config: DataTransformationConfig):
        self.config=config

    def train_test_split(self):
        data=pd.read_csv(self.config.data_path)

        train,test=train_test_split(data)    
          # Scaler nesnesi oluştur
        scaler = StandardScaler()

        # Eğitim verisini ölçeklendir
        train_scaled = scaler.fit_transform(train)
        test_scaled = scaler.transform(test)

        # Ölçeklenmiş verileri CSV olarak kaydet
        pd.DataFrame(train_scaled, columns=train.columns).to_csv(os.path.join(self.config.root_dir, "train_scaled.csv"))
        pd.DataFrame(test_scaled, columns=test.columns).to_csv(os.path.join(self.config.root_dir, "test_scaled.csv"))

        
