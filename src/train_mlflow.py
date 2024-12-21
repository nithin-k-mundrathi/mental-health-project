import mlflow
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score,roc_auc_score
from tqdm import tqdm
from hyperopt import fmin,tpe,STATUS_OK,hp
mlflow.set_tracking_uri(uri="http://localhost:8080")

import pandas as pd
X  = pd.read_pickle('data/processed_data.pkl')

# Load the Iris dataset
y = X['label_c']
X.drop(['label','label_c'],axis=1,inplace=True)

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

def train_model(params):

    with mlflow.start_run(nested=True) as nested_run:
        estimators = params['n_estimators']
        depth = params['max_depth']
        train_auc = []
        test_auc = []
        model_rf = RandomForestClassifier(n_estimators=estimators, max_depth=depth,class_weight="balanced")
        model_rf.fit(X_train, y_train)
        
        y_train_pred = []
        for k in range(0,X_train.shape[0],100):
          y_train_pred.extend(model_rf.predict_proba(X_train[k:k+100])[:,1])
    
        y_test_pred = []
        for k in range(0, X_test.shape[0],100):
          y_test_pred.extend(model_rf.predict_proba(X_test[k:k+100])[:,1])
        
        train_auc = roc_auc_score(y_train,y_train_pred)
        test_auc = roc_auc_score(y_test, y_test_pred)
        mlflow.log_params(
           params = {
              "n_estimators": estimators,
              "max_depth": depth,
              }
        )

        # Calculate metrics
        mlflow.log_metric("test_auc", (test_auc))
        mlflow.log_metric("train_auc", (train_auc))

        # Log the model
        model_info = mlflow.sklearn.log_model(
            sk_model=model_rf,
            artifact_path="depression_model",
            input_example=X_train,
            registered_model_name="tracking-depression-model",
        )


    return {'status' : STATUS_OK,'loss':1-(test_auc)}

# Set our tracking server uri for logging
mlflow.set_tracking_uri(uri="http://127.0.0.1:8080")

# Create a new MLflow Experiment
mlflow.set_experiment("MLflow Depression")

# Define the model hyperparameters
params = {
    "n_estimators": hp.choice('n_estimators',[5, 10, 50,100,250]),
    "max_depth": hp.choice('max_depth',[4,5,10,20,50]),
}

# Start an MLflow run
with mlflow.start_run(run_name = 'depression_mlflow') as run:
    best_params = fmin(
        fn = train_model,
        space = params,
        algo = tpe.suggest,
        max_evals = 8
    )
