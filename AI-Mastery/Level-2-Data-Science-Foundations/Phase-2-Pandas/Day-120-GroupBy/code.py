import pandas as pd
import numpy as np

def main():
    print("=== Day 120: GroupBy Demonstration ===")
    
    # 1. Sample Dataset
    df = pd.DataFrame({
        'Department': ['Sales', 'Engineering', 'Sales', 'Engineering', 'Sales', 'HR'],
        'Employee': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank'],
        'Salary': [70000, 95000, 72000, 105000, 68000, 60000],
        'Experience_Yrs': [3, 5, 4, 7, 2, 1]
    })
    print("Raw DataFrame:
", df)
    
    # 2. Basic GroupBy and Group Inspection
    grouped = df.groupby('Department')
    print("
Department Groups Found:", list(grouped.groups.keys()))
    print("
Engineering Group Sub-Table:
", grouped.get_group('Engineering'))
    
    # 3. Single Column Aggregation
    dept_avg_sal = grouped['Salary'].mean()
    print("
Average Salary by Department:
", dept_avg_sal)
    
    # 4. Multi-Column Grouping with as_index=False
    df['Location'] = ['NY', 'NY', 'SF', 'NY', 'SF', 'NY']
    multi_grp = df.groupby(['Department', 'Location'], as_index=False)['Salary'].mean()
    print("
Mean Salary by Dept & Location (as_index=False):
", multi_grp)

if __name__ == "__main__":
    main()
