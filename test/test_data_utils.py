# tests/test_data_utils.py

import pandas as pd
from src.data_utils import get_shape  # 修正箇所

def test_get_shape():
    data = {
        'column1': [1, 2, 3],
        'column2': [4, 5, 6],
        'column3': [7, 8, 9]
    }
    df = pd.DataFrame(data)
    assert get_shape(df) == (3, 3), "Test Failed: The shape of the DataFrame should be (3, 3)"

if __name__ == "__main__":
    test_get_shape()
    print("All tests passed!")
