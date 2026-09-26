import pandas as pd
import numpy as np

def main():
    print("=== Day 124: Join Demonstration ===")
    
    # 1. Sample DataFrames with Indices
    df_emp = pd.DataFrame({
        'Name': ['Alice', 'Bob', 'Charlie'],
        'Dept': ['HR', 'IT', 'IT']
    }, index=[101, 102, 103])
    
    df_sal = pd.DataFrame({
        'Salary': [70000, 95000, 105000],
        'Bonus': [5000, 10000, 12000]
    }, index=[101, 102, 103])
    
    df_perf = pd.DataFrame({
        'Rating': ['A', 'Exceeds', 'Exceeds']
    }, index=[101, 102, 104])
    
    print("Employees DF:
", df_emp)
    print("
Salaries DF:
", df_sal)
    
    # 2. Basic Index Join
    print("
--- 1. Basic Index Join (Default Left) ---")
    joined_1 = df_emp.join(df_sal)
    print(joined_1)
    
    # 3. Multi-DataFrame Join
    print("
--- 2. Multi-DataFrame Join ---")
    joined_multi = df_emp.join([df_sal, df_perf], how='outer')
    print(joined_multi)

if __name__ == "__main__":
    main()
