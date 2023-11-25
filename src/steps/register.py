from pathlib import Path
from prefect import flow, get_run_logger
import mlflow
import mlflow.sklearn


@flow
def register_model(cfg):
    logger = get_run_logger()
    logger.info("Registering model")
    lr_model_path = Path(cfg.paths.models.lr)
    mlflow.sklearn.log_model(lr_model_path, "model")
    logger.info(f"Model registered to {lr_model_path}")
    return None
