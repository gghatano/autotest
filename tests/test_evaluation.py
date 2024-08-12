import pandas as pd
import os
import csv
from src.evaluation import evaluate_function

def run_test_case(data1_path, data2_path, function_name, expected_value):
    # 動的に関数を取得
    func = globals()[function_name]
    result = func(data1_path, data2_path)
    assert result == expected_value, (
        f"Test failed for function '{function_name}' with data1_path='{data1_path}' and "
        f"data2_path='{data2_path}': {result} != {expected_value}"
    )

def test_evaluation():
    # テストケースの読み込み
    test_cases_path = os.path.join(os.path.dirname(__file__), 'test_cases.csv')
    
    with open(test_cases_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data1_path = row['data1_path']
            data2_path = row['data2_path']
            function_name = row['function_name']
            expected_value = int(row['expected_value'])
            
            try:
                run_test_case(data1_path, data2_path, function_name, expected_value)
                print(f"Test passed for {function_name} with {data1_path} and {data2_path}")
            except AssertionError as e:
                print(e)
                raise

if __name__ == "__main__":
    test_evaluation()
    print("All tests passed!")

