import pandas as pd
import numpy as np

def main():
    # 1. Sample Dataset
    df = pd.DataFrame({
        'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
        'Age': [25, 45, 35, 52, 29],
        'Department': ['HR', 'IT', 'IT', 'Sales', 'HR'],
        'Salary': [70000, 120000, 85000, 95000, 62000]
    })
    print("Full DataFrame:
", df)
    
    # 2. Multi-Condition Filtering (AND &)
    it_high_salary = df[(df['Department'] == 'IT') & (df['Salary'] > 80000)]
    print("
IT Department & Salary > 80k:
", it_high_salary)
    
    # 3. Category Membership (isin)
    target_deps = df[df['Department'].isin(['HR', 'Sales'])]
    print("
HR or Sales Departments:
", target_deps)
    
    # 4. Range Filtering (between)
    age_range = df[df['Age'].between(30, 50)]
    print("
Age between 30 and 50:
", age_range)
    
    # 5. df.query()
    min_sal = 80000
    query_res = df.query("Salary >= @min_sal and Age < 40")
    print("
Query (Salary >= 80k & Age < 40):
", query_res)

if __name__ == "__main__":
    main()
