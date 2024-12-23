import mlflow
import shutil
import warnings
warnings.filterwarnings("ignore")

# get the Id of the Experiment
id_experiment = mlflow.get_experiment_by_name('MLflow Depression').experiment_id

# Search for all the RUns and Get the latest MlFlow Run
runs_all = mlflow.search_runs(
    [id_experiment],
    order_by=['start_time DESC']
)

# Get the ParentRunId of the Latest Run
runs = runs_all[~runs_all['tags.mlflow.parentRunId'].isin(runs_all[runs_all['status']=='RUNNING']['tags.mlflow.parentRunId'])]
latest_parent_run = runs.iloc[0]['tags.mlflow.parentRunId']
latest_nested_runs = runs[runs['tags.mlflow.parentRunId'] == latest_parent_run]

# get the best Nested Run From the Latest Run
best_latest_run = latest_nested_runs.sort_values('metrics.test_auc', ascending=False).iloc[0]

# Copy the Best Run pickle file to Models folder.
shutil.copyfile(
'mlartifacts/439831194545044561/{}/artifacts/depression_model/model.pkl'.format(best_latest_run.run_id),
'models/model.pkl'
)

print('Copied the best model to models')