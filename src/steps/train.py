import polars as pl
from prefect import flow, get_run_logger
from sklearn.linear_model import LinearRegression
import mlflow
import mlflow.sklearn
# import sqlite3


@flow
def train(cfg):
    logger = get_run_logger()
    logger.info("Starting train step")

    X_train_path = cfg.paths.data.X_train
    y_train_path = cfg.paths.data.y_train
    X_train = pl.read_parquet(X_train_path).to_pandas()
    y_train = pl.read_parquet(y_train_path).to_pandas()

    # mlflow.set_tracking_uri("sqlite:///mlflow.db")
    mlflow.set_tracking_uri('file:///Users/zacklarsen/Documents/Projects/kaggle/kaggle-paris-housing-prices/mlruns/')
    # mlflow.set_tracking_uri('file:///mlruns')
    mlflow.set_experiment("Kaggle Paris Housing")
    with mlflow.start_run():  # run_name="LR_model"
        mlflow.sklearn.autolog()
        model = LinearRegression()
        logger.info("Fitting model")
        model.fit(X_train, y_train)
        # logger.info("Logging model to mlflow")
        mlflow.sklearn.log_model(model, "model")

    logger.info("Model training finished")

    return None
