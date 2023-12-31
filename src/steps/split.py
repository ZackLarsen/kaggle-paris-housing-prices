from prefect import flow, get_run_logger
import polars as pl
from sklearn.model_selection import train_test_split


@flow
def split(cfg, data):
    logger = get_run_logger()
    logger.info("Splitting data into train and test sets")

    target_var = cfg.target_var
    random_state = cfg.train_test_split.random_state
    train_ratio = cfg.train_test_split.train_ratio
    validation_ratio = cfg.train_test_split.validation_ratio
    test_ratio = cfg.train_test_split.test_ratio

    assert train_ratio + validation_ratio + test_ratio == 1, \
        """train_ratio, validation_ratio, and test_ratio must sum to 1"""

    X = data.drop(target_var)
    y = data.select(pl.col(target_var))

    logger.info("Splitting data into train, validation, and test sets")
    logger.info(f"train_ratio: {train_ratio}")
    logger.info(f"validation_ratio: {validation_ratio}")
    logger.info(f"test_ratio: {test_ratio}")

    X_train, X_test, y_train, y_test = \
        train_test_split(
            X,
            y,
            test_size=1 - train_ratio,
            random_state=random_state)

    X_validation, X_test, y_validation, y_test = \
        train_test_split(
            X_test,
            y_test,
            test_size=test_ratio/(test_ratio + validation_ratio),
            random_state=random_state)

    logger.info(f"Size of data: {data.shape}")
    logger.info(f"Size of X_train: {X_train.shape}")
    logger.info(f"Size of X_validation: {X_validation.shape}")
    logger.info(f"Size of X_test: {X_test.shape}")

    splits = {
        'X_train': X_train,
        'X_validation': X_validation,
        'X_test': X_test,
        'y_train': y_train,
        'y_validation': y_validation,
        'y_test': y_test
    }

    return splits
