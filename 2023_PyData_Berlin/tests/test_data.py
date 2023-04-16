import pandas as pd
from pathlib import Path

def test_csv_values():
    data_path = Path(__file__).parent.parent.joinpath("data/data.csv")
    data = pd.read_csv(data_path)
    assert abs(data["sin"]).all() <= 1
