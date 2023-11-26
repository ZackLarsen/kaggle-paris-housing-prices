# kaggle-paris-housing-prices

[Kaggle competition](https://www.kaggle.com/competitions/playground-series-s3e6/overview)

## Workflow

Run experiments:

- Define configuration with model type and parameters
- Run run_flow.py to run the experiment

Compare experiment results:

- Using a Jupyter notebook:
  - Go to "Experiments" tab in MLflow UI
  - Click on the experiment you want to compare
  - Click on the "Chart view"
- Using the MLflow UI:

Registering models:

- Using CLI:
  - Start an MLflow server using SQLite as the backend store
- Using the MLflow Registry UI:
  - Navigate to the MLflow UI (usually at http://127.0.0.1:5000 if running locally).
  - Go to the "Experiments" tab, find your run, and click on the logged model in the "Artifacts" section.
  - Use the "Register Model" button to register the model.

## MLflow UI

First, navigate to the mlruns directory below and activate the conda/mamba environment.

```bash
cd /Users/zacklarsen/Documents/Projects/kaggle/kaggle-paris-housing-prices/mlruns/
mamba activate kaggle_paris
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
