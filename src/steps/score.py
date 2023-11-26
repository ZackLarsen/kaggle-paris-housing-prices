import mlflow
import pandas as pd

logged_model = 'runs:/68db303a03904c3b9b51ad673728d0c9/LR_model'

# Load model as a PyFuncModel.
loaded_model = mlflow.pyfunc.load_model(logged_model)

loaded_model.predict(pd.DataFrame(data))
