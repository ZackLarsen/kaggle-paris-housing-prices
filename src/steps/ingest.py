from prefect import flow, get_run_logger
import polars as pl


@flow
def ingest_raw_data(cfg):
    """Ingest raw data from the data source."""
    logger = get_run_logger()
    train_raw_path = cfg.paths.data.train_raw
    logger.info(f"Ingesting raw data from {train_raw_path}")
    raw_data = pl.read_csv(train_raw_path)
    return raw_data
