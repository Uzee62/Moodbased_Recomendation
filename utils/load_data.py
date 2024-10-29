import pandas as pd

file_path = 'data/mood_items.csv'


def load_data(file_path):
    return pd.read_csv(file_path)
