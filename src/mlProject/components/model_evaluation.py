import os
import pandas as pd
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from src.mlProject.utils.common import save_json
import joblib
from src.mlProject.config.configuration import ModelEvaluationConfig
from pathlib import Path

class ModelEvaluation:
    def __init__(self, config: ModelEvaluationConfig):
        self.config = config

    def eval_metrics(self, actual, pred):
        mse = mean_squared_error(actual, pred)
        mae = mean_absolute_error(actual, pred)
        r2 = r2_score(actual, pred)
        return mse, mae, r2

    def save_results(self):
        test_data = pd.read_csv(self.config.test_path)
        test_x = test_data.drop([self.config.target_column], axis=1)
        test_y = test_data[[self.config.target_column]]

        # Model dosyalarını yüklüyoruz
        elastic_model = joblib.load(self.config.elasticpath)
        ridge_model = joblib.load(self.config.ridgepath)
        lasso_model = joblib.load(self.config.lassopath)

        # Tahminler yapılıyor
        elastic_pred = elastic_model.predict(test_x)
        ridge_pred = ridge_model.predict(test_x)
        lasso_pred = lasso_model.predict(test_x)

        a, b, c = self.eval_metrics(test_y, elastic_pred)
        d, e, f = self.eval_metrics(test_y, ridge_pred)
        x, y, z = self.eval_metrics(test_y, lasso_pred)

        results = {"ElasticNet": {"mse": a, "mae": b, "r2": c},
                   "Ridge": {"mse": d, "mae": e, "r2": f},
                   "Lasso": {"mse": x, "mae": y, "r2": z}}

        save_json(path=Path(self.config.metric_file_name), data=results)