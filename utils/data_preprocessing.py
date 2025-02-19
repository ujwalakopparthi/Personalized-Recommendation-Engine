# utils/data_preprocessing.py
import pandas as pd

def preprocess_data(file_path):
    df = pd.read_csv(file_path)
    # Process data (e.g., handle missing values, normalize data)
    df = df.dropna()
    # Other preprocessing steps as needed
    return df
