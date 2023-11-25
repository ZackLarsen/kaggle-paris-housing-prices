from prefect import flow, get_run_logger
from sklearn import metrics
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import mlflow
import mlflow.sklearn


@flow
def evaluate():
    logger = get_run_logger()
    logger.info("Evaluating model performance")
    value1 = 4  # TODO: Replace with actual value
    mlflow.log_metric("metric1", value1)
    metrics = "Evaluation Metrics"
    return metrics
