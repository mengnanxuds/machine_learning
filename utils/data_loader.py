import pandas as pd
from sklearn.model_selection import train_test_split

def load_data(file_path, target_column):
    """importing data from file and split training and test set"""
    df = pd.read_csv(file_path)
    X = df.drop(columns=[target_column])
    y = df[target_column]
    return train_test_split(X, y, test_size=0.2, random_state=42)