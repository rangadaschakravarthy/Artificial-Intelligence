import pandas as pd
import numpy as np

def main():
    print("=== Day 122: Apply and Map Demonstration ===")
    
    # 1. Sample Dataset
    df = pd.DataFrame({
        'Department': ['HR', 'HR', 'IT', 'IT', 'Sales'],
        'Employee': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
        'Salary': [60000, 65000, 95000, 105000, 70000],
        'Rating_Code': ['E', 'M', 'E', 'E', 'M']
    })
    
    # 2. Series.map for Dictionary Substitution
    print("
--- 1. Series.map ---")
    code_map = {'E': 'Exceeds', 'M': 'Meets', 'N': 'Needs Improvement'}
    df['Rating_Text'] = df['Rating_Code'].map(code_map)
    print(df[['Employee', 'Rating_Code', 'Rating_Text']])
    
    # 3. DataFrame.apply across Rows (axis=1)
    print("
--- 2. DataFrame.apply (axis=1) ---")
    df['Bonus'] = df.apply(
        lambda r: r['Salary'] * 0.15 if r['Rating_Code'] == 'E' else r['Salary'] * 0.05,
        axis=1
    )
    print(df[['Employee', 'Salary', 'Rating_Code', 'Bonus']])
    
    # 4. GroupBy.transform
    print("
--- 3. GroupBy.transform ---")
    df['Dept_Avg_Salary'] = df.groupby('Department')['Salary'].transform('mean')
    df['Salary_Ratio'] = df['Salary'] / df['Dept_Avg_Salary']
    print(df[['Employee', 'Department', 'Salary', 'Dept_Avg_Salary', 'Salary_Ratio']])

if __name__ == "__main__":
    main()
