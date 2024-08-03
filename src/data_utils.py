# src/data_utils.py

import pandas as pd

def get_shape(df: pd.DataFrame) -> tuple:
    """
    Returns the number of rows and columns of the DataFrame.
    
    :param df: Input DataFrame
    :return: A tuple containing the number of rows and columns
    """
    return df.shape
