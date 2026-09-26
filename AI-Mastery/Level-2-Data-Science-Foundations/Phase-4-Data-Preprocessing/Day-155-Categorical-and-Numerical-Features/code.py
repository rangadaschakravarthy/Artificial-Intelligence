import pandas as pd
import numpy as np

def main():
    print("=== Day 155: Categorical and Numerical Features Demonstration ===")
    
    df = pd.DataFrame({
        'Customer_Age': [22, 45, 31, 55],
        'Account_Balance': [1500.50, 45000.00, 8900.25, 120000.00],
        'State_Code': ['CA', 'NY', 'CA', 'TX'],
        'Zip_Code': [90210, 10001, 90210, 75001] # Integer categorical
    })
    
    # Recast Zip_Code as string categorical
    df['Zip_Code'] = df['Zip_Code'].astype(str)
    
    num_cols = df.select_dtypes(include=np.number).columns.tolist()
    cat_cols = df.select_dtypes(include=['object', 'category']).columns.tolist()
    
    print("Numeric Features:    ", num_cols)
    print("Categorical Features:", cat_cols)

if __name__ == "__main__":
    main()
