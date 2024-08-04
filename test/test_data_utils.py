# tests/test_data_utils.py

import pandas as pd
from src.data_utils import get_shape
import os

def test_get_shape():
    # テストデータのパスを取得
    csv_path = os.path.join(os.path.dirname(__file__), 'data', 'sample_data.csv')
    
    # CSVデータを読み込む
    df = pd.read_csv(csv_path)
    
    # 関数のテストを実行
    assert get_shape(df) == (3, 3), "Test Failed: The shape of the DataFrame should be (3, 3)"

if __name__ == "__main__":
    test_get_shape()
    print("All tests passed!")
