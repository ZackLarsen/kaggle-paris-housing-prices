# kaggle-paris-housing-prices

[Kaggle competition](https://www.kaggle.com/competitions/playground-series-s3e6/overview)

## Setting MLflow tracking server

```bash
mlflow server --backend-store-uri sqlite:///mlflow.db --default-artifact-root ./mlruns --host
```

## MLflow UI

```bash
mlflow ui
```

```bash
http://localhost:5000
```

```bash
http://127.0.0.1:8080
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
