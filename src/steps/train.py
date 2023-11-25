import polars as pl
from prefect import flow, get_run_logger
from sklearn.linear_model import LinearRegression
import mlflow
import mlflow.sklearn
# import sqlite3


@flow
def train(cfg):
    logger = get_run_logger()
    logger.info("Training model")

    X_train_path = cfg.paths.data.X_train
    y_train_path = cfg.paths.data.y_train
    X_train = pl.read_parquet(X_train_path)
    y_train = pl.read_parquet(y_train_path)

    mlflow.set_tracking_uri("sqlite:///mlflow.db")
    with mlflow.start_run(run_name="LR_model"):
        mlflow.sklearn.autolog()
        model = LinearRegression()
        model.fit(X_train, y_train)
        mlflow.sklearn.log_model(model, "LR_model")

    logger.info("Model training finished")

    return model
