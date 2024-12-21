# Run the Mlfow command
mlflow server --host 127.0.0.1 --port 8080

# train a Model 
python src/train_mlflow.py

# Predict a Model
streamlit run src/prediction.py

# Mlflow Documentation to refer
https://mlflow.org/docs/latest/getting-started/intro-quickstart/index.html
