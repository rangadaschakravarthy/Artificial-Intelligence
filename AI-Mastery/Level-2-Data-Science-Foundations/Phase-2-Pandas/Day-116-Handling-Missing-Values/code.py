import pandas as pd
import numpy as np

def main():
    # 1. Sample Dataset with Missing Values
    df = pd.DataFrame({
        'Department': ['IT', 'IT', 'Sales', 'Sales', 'IT'],
        'Salary': [90000.0, np.nan, 50000.0, np.nan, 110000.0],
        'Rating': [4.5, 3.8, np.nan, 4.0, np.nan]
    })
    print("Original DataFrame:
", df)
    
    # 2. Dropna Demonstration
    print("
Drop Rows where Salary is NaN:
", df.dropna(subset=['Salary']))
    
    # 3. Overall Median & Mode Imputation
    df_imp = df.copy()
    df_imp['Salary_Median'] = df_imp['Salary'].fillna(df_imp['Salary'].median())
    print("
Overall Median Imputed Salary:
", df_imp[['Salary', 'Salary_Median']])
    
    # 4. Group-Based Imputation by Department
    df_imp['Salary_Group_Median'] = df_imp.groupby('Department')['Salary'].transform(
        lambda g: g.fillna(g.median())
    )
    print("
Group-Based Median Imputed Salary:
", df_imp[['Department', 'Salary', 'Salary_Group_Median']])
    
    # 5. Forward Fill Demonstration
    time_series = pd.Series([100.0, np.nan, np.nan, 105.0])
    print("
Forward Fill Series:
", time_series.ffill())

if __name__ == "__main__":
    main()
