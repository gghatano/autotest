import pandas as pd

def evaluate_function(data1_path, data2_path):
    df1 = pd.read_csv(data1_path)
    df2 = pd.read_csv(data2_path)
    
    # 仮の評価ロジック
    # 例: 各データフレームの最初の列の和を計算して返す
    value1 = df1.iloc[:, 0].sum()
    value2 = df2.iloc[:, 0].sum()
    
    return value1 + value2

