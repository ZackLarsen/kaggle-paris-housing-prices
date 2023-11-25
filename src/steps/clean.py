from datetime import datetime

from prefect import flow, get_run_logger
import polars as pl
import polars.selectors as cs
import numpy as np
from scipy import stats


def calculate_age(data):
    current_year = datetime.now().year
    return (
        data
        .with_columns(age=current_year - pl.col("made"))
        .filter(pl.col("made") <= current_year)
        .drop("made")
    )


def remove_outliers(data):
    outliers_removed = (
        data
        .with_columns(
            pl.col(["basement", "squareMeters", "floors", "attic", "garage"])
            .map_batches(lambda x: np.abs(stats.zscore(x)))
            .name.suffix("_z_score_abs")
        )
        .filter(
            pl.fold(
                acc=pl.lit(True),
                function=lambda acc, x: acc & x,
                exprs=cs.contains("_z_score") < 3,
            )
        )
    )

    outliers_removed_cols = outliers_removed.columns
    outliers_removed_cols.sort()

    return outliers_removed.select(outliers_removed_cols)


@flow
def clean_data(raw_data):
    """Clean the raw data."""
    logger = get_run_logger()
    logger.info("Cleaning data")
    logger.info(f"Shape of raw data: {raw_data.shape}")

    clean_data = (
        raw_data
        .lazy()
        .drop("id")
        .pipe(calculate_age)
        .pipe(remove_outliers)
    ).collect()

    logger.info(f"Shape of clean data: {clean_data.shape}")

    return clean_data
