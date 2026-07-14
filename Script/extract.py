import pandas as pd
from pathlib import Path


def extract_data():

    data_path = Path("../data/raw")

    datasets = {}

    for file in data_path.glob("*.csv"):
        datasets[file.stem] = pd.read_csv(file)

    print("Datasets extracted successfully.")

    return datasets