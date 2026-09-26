import pandas as pd
import numpy as np

def main():
    # 1. Sample Dataset
    df = pd.DataFrame({
        'Department': ['IT', 'HR', 'IT', 'HR', 'IT'],
        'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
        'Salary': [90000, 65000, 110000, 60000, 95000]
    })
    print("Original DataFrame:
", df)
    
    # 2. Single Column Sort
    print("
Sorted by Salary Descending:
", df.sort_values(by='Salary', ascending=False))
    
    # 3. Multi-Column Sort with Mixed Directions
    multi_sorted = df.sort_values(
        by=['Department', 'Salary'],
        ascending=[True, False]
    )
    print("
Multi-Sorted (Dept Asc, Salary Desc):
", multi_sorted)
    
    # 4. nlargest Demo
    print("
Top 2 Salaries (nlargest):
", df.nlargest(2, 'Salary'))

if __name__ == "__main__":
    main()
