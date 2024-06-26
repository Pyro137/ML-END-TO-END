from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path

@dataclass(frozen=True)
class DataValidationConfig:
    root_dir: Path
    STATUS_FILE: str
    all_schema: dict
    unzip_data_dir: Path

@dataclass(frozen=True)
class DataTransformationConfig:
    root_dir: Path
    data_path: Path

@dataclass(frozen=True)
class ModelTrainerConfig:
    root_dir: Path
    train_path: Path
    test_path:Path
    model_name: str
    alpha: float
    l1_ratio:float
    target_column:str

@dataclass(frozen=True)
class ModelEvaluationConfig:
    root_dir: Path
    test_path: Path
    elasticpath: Path
    ridgepath: Path
    lassopath: Path
    target_column: str
    metric_file_name: Path
    