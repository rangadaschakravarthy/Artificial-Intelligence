import pandas as pd
import numpy as np

def main():
    print("=== Day 132: Real-World Dataset Cleaning and Analysis Mini Project ===")
    
    # STAGE 1: RAW DATA INGESTION
    print("
--- STAGE 1: Raw Data Ingestion ---")
    dirty_data = pd.DataFrame({
        ' Transaction_ID ': [1001, 1002, 1002, 1003, 1004, 1005, 1006],
        ' Cust_Name ': [' Alice ', ' Bob ', ' Bob ', ' Charlie ', ' David ', ' Eve ', ' Frank '],
        ' Category ': ['Electronics', 'Electronics', 'Electronics', 'Clothing', 'Furniture', 'Clothing', 'Electronics'],
        ' Amount ': ['$1,200.50', '$45.00', '$45.00', 'INVALID', '$350.00', '$89.99', '$899.00'],
        ' Tx_Date ': ['2023-01-15', '2023-01-16', '2023-01-16', '2023-02-01', '2023-02-15', '2023-03-01', '2023-03-10'],
        ' Churned ': ['No', 'No', 'No', 'Yes', 'No', 'Yes', 'No']
    })
    print("Raw Data Ingested. Shape:", dirty_data.shape)
    
    # STAGE 2: DATA CLEANING
    print("
--- STAGE 2: Data Cleaning Pipeline ---")
    df = dirty_data.copy()
    
    # Standardize Headers
    df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')
    
    # Deduplicate
    init_rows = len(df)
    df.drop_duplicates(subset=['transaction_id'], inplace=True)
    print(f"Deduplicated {init_rows - len(df)} duplicate records.")
    
    # Clean String Text
    for col in ['cust_name', 'category', 'churned']:
        df[col] = df[col].astype(str).str.strip()
    
    # Parse Numeric Amount
    df['amount'] = (
        df['amount']
        .str.replace('$', '', regex=False)
        .str.replace(',', '', regex=False)
        .replace('INVALID', np.nan)
    )
    df['amount'] = pd.to_numeric(df['amount'], errors='coerce')
    df['amount'].fillna(df['amount'].median(), inplace=True)
    
    # Parse Timestamps
    df['tx_date'] = pd.to_datetime(df['tx_date'])
    print("Cleaned Dataset Head:
", df.head())
    
    # STAGE 3: EXPLORATORY DATA ANALYSIS (EDA)
    print("
--- STAGE 3: Exploratory Data Analysis ---")
    print("Transaction Amount Summary:
", df['amount'].describe().round(2))
    print("Category Frequency:
", df['category'].value_counts(normalize=True).round(3))
    
    # STAGE 4: BUSINESS REPORTING & AGGREGATION
    print("
--- STAGE 4: Business Reporting (Pivot Table & Time Series) ---")
    df['month'] = df['tx_date'].dt.to_period('M')
    piv_report = df.pivot_table(index='month', columns='category', values='amount', aggfunc='sum', fill_value=0)
    print("Monthly Category Revenue Pivot Table:
", piv_report)
    
    # STAGE 5: ML PREPROCESSING
    print("
--- STAGE 5: Machine Learning Dataset Preparation ---")
    y = (df['churned'] == 'Yes').astype(int)
    X_raw = df.drop(columns=['churned', 'transaction_id', 'cust_name', 'tx_date', 'month'])
    X = pd.get_dummies(X_raw, columns=['category'], drop_first=True, dtype=int)
    
    print("Prepared Feature Matrix X:
", X)
    print("Target Vector y:
", y.values)
    
    # STAGE 6: VALIDATION ASSERTIONS & EXPORT
    print("
--- STAGE 6: Validation Assertions & Export ---")
    assert X.isna().sum().sum() == 0, "Validation Error: Nulls remain in X!"
    assert X.select_dtypes(include='object').shape[1] == 0, "Validation Error: Un-encoded string objects remain!"
    assert len(X) == len(y), "Validation Error: X and y length mismatch!"
    
    print("All Pipeline Assertions Passed Successfully!")
    print("=== Mini Project Completed Successfully ===")

if __name__ == "__main__":
    main()
