# kaggle-paris-housing-prices

[Kaggle competition](https://www.kaggle.com/competitions/playground-series-s3e6/overview)

## Workflow

Run experiments:

- [ ] Define experiment

Compare experiment results:

- [ ] Compare models

## MLflow UI

First, navigate to the mlruns directory below.

```bash
cd /Users/zacklarsen/Documents/Projects/kaggle/kaggle-paris-housing-prices/mlruns/
```

Then, run the following command to start the MLflow UI.

```bash
mlflow ui --backend-store-uri file:///Users/zacklarsen/Documents/Projects/kaggle/kaggle-paris-housing-prices/mlruns/
```

## Setting MLflow tracking URI to local file

```python
import mlflow
mlflow.set_tracking_uri('file:///Users/zacklarsen/Documents/Projects/kaggle/kaggle-paris-housing-prices/mlruns/')
```

## Setting MLflow experiment

```python
mlflow.set_experiment("Kaggle Paris Housing")
```

## Setting MLflow tracking server

```bash
mlflow server --backend-store-uri sqlite:///mlflow.db --default-artifact-root ./mlruns --host
```

## Downloading the data

Navigate to kaggle/data and run the following command. Then, unzip the file and move to the paris_housing_prices directory.

```bash
kaggle competitions download -c playground-series-s3e6
```

## Defining and installing the environment

```bash
mamba env update --file env.yaml --prune
```
