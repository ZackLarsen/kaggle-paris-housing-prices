import sys
from pathlib import Path

import hydra
from hydra import compose, initialize
from omegaconf import DictConfig
from prefect import flow, get_run_logger

sys.path.append(str(Path.cwd().parent))  # Have to append string - see here: https://github.com/takluyver/entrypoints/issues/43

from steps.ingest import ingest_raw_data
from steps.clean import clean_data
from steps.split import split
from steps.save import save_splits, save_model
# from steps.transform import transform
from steps.train import train
from steps.register import register_model
# from steps.evaluate import evaluate
# from steps.tune import tune


@flow
@hydra.main(config_path="config", config_name="main", version_base="1.3.2")
def run_flow(cfg: DictConfig) -> None:
    logger = get_run_logger()
    logger.info("Running flow")

    # raw_data = ingest_raw_data(cfg)
    # cleaned_data = clean_data(raw_data)
    # splits = split(cfg, cleaned_data)
    # save_splits(cfg, splits)

    # transform()

    train(cfg)

    # evaluate()
    # tune()
    # register_model()


if __name__ == "__main__":
    with initialize(version_base="1.3.2",
                    config_path="config",
                    job_name="run_flow"):
        cfg = compose(config_name="main")
        run_flow(cfg)
