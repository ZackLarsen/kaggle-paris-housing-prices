import polars as pl
from prefect import flow, get_run_logger
import mlflow
import mlflow.sklearn
from sklearn.linear_model import LinearRegression, Ridge, Lasso, ElasticNet
from sklearn.ensemble import RandomForestRegressor, AdaBoostRegressor, GradientBoostingRegressor
from sklearn.tree import DecisionTreeRegressor, ExtraTreeRegressor
from sklearn.svm import SVR
from xgboost import XGBRegressor
from lightgbm import LGBMRegressor
from flaml import AutoML


mlflow.set_tracking_uri('file:///Users/zacklarsen/Documents/Projects/kaggle/kaggle-paris-housing-prices/mlruns/')
mlflow.set_experiment("Kaggle Paris Housing")


@flow
def train(cfg):
    logger = get_run_logger()
    logger.info("Starting train step")

    X_train_path = cfg.paths.data.X_train
    y_train_path = cfg.paths.data.y_train
    X_train = pl.read_parquet(X_train_path).to_pandas()
    y_train = pl.read_parquet(y_train_path).to_pandas().values.ravel()

    model_type = eval(cfg.model.type)
    parameters = cfg.model.get('parameters', {})
    model = model_type(**parameters)

    with mlflow.start_run(run_name=cfg.model.type):
        mlflow.sklearn.autolog()
        logger.info("Fitting model")
        model.fit(X_train, y_train)
        logger.info("Logging model to mlflow")
        mlflow.sklearn.log_model(model, "model")

    logger.info("Model training finished")

    return None
