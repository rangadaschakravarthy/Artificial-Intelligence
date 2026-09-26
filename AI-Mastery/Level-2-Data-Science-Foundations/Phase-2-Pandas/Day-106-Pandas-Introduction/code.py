import pandas as pd
import numpy as np

def main():
    print("Pandas Version:", pd.__version__)
    
    # 1. Basic DataFrame Creation
    data = {
        'Name': ['Alice', 'Bob', 'Charlie', 'David'],
        'Age': [25, 30, 35, 40],
        'Salary': [70000.0, 85000.0, 95000.0, 110000.0],
        'Is_Manager': [False, False, True, True]
    }
    df = pd.DataFrame(data)
    
    print("
Employee DataFrame:
", df)
    print("
DataFrame Shape:", df.shape)
    print("Column Data Types:
", df.dtypes)
    
    # 2. Convert to NumPy Array
    np_matrix = df[['Age', 'Salary']].to_numpy()
    print("
Extracted Age & Salary NumPy Matrix:
", np_matrix)
    print("NumPy Array Shape:", np_matrix.shape)

if __name__ == "__main__":
    main()
