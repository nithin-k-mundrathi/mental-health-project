# Install all the packages
pip install -r requirements.txt

# Run the Mlfow command
mlflow server --host 127.0.0.1 --port 8080

# train a Model - run this in a New Terminal
python src/train_mlflow.py

# Save the Best model
python src/best_model.py

# Predict a Model
streamlit run src/prediction.py
streamlit run src/prediction-original.py

# Mlflow Documentation to refer
https://mlflow.org/docs/latest/getting-started/intro-quickstart/index.html
