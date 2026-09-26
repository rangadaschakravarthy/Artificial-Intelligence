import pandas as pd
import numpy as np

def main():
    print("=== Day 131: Pandas for Machine Learning Demonstration ===")
    
    # 1. Raw Customer Dataset
    raw_df = pd.DataFrame({
        'Age': [25, 45, 35, 50, 23],
        'Income': [50000, 95000, 70000, 120000, 42000],
        'City': ['NY', 'SF', 'NY', 'LA', 'SF'],
        'Contract_Type': ['Month-to-Month', 'Two-Year', 'One-Year', 'Two-Year', 'Month-to-Month'],
        'Churned': ['No', 'No', 'Yes', 'No', 'Yes']
    })
    
    print("Raw Dataset:
", raw_df)
    
    # 2. Separate Target Vector y
    y = (raw_df['Churned'] == 'Yes').astype(int)
    X_raw = raw_df.drop(columns=['Churned'])
    
    print("
--- 1. Target Vector y ---")
    print(y.values)
    
    # 3. One-Hot Encode Features using pd.get_dummies
    print("
--- 2. One-Hot Encoded Feature Matrix X ---")
    X = pd.get_dummies(X_raw, columns=['City', 'Contract_Type'], drop_first=True, dtype=int)
    print(X)
    
    # 4. Verify ML Readiness
    print("
--- 3. ML Readiness Validation ---")
    print("X Dtypes:
", X.dtypes)
    print("Total Nulls in X:", X.isna().sum().sum())
    print("X Matrix Shape:", X.shape)

if __name__ == "__main__":
    main()
