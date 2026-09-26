import pandas as pd
import numpy as np

def clean_dataset_pipeline(raw_df):
    # Complete 10-Step Data Cleaning Pipeline
    print("Starting Data Cleaning Pipeline...")
    df = raw_df.copy()
    
    # Step 1: Standardize Column Headers
    df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')
    
    # Step 2: Remove Exact Duplicate Records
    init_rows = len(df)
    df.drop_duplicates(inplace=True)
    print(f"Dropped {init_rows - len(df)} duplicate rows.")
    
    # Step 3: Strip Whitespace from String Columns
    str_cols = df.select_dtypes(include='object').columns
    for col in str_cols:
        df[col] = df[col].astype(str).str.strip()
    
    # Step 4: Parse Numeric Strings
    if 'price' in df.columns:
        df['price'] = (
            df['price']
            .str.replace('$', '', regex=False)
            .str.replace(',', '', regex=False)
            .replace('nan', np.nan)
        )
        df['price'] = pd.to_numeric(df['price'], errors='coerce')
    
    # Step 5: Handle Missing Values
    if 'price' in df.columns:
        median_price = df['price'].median()
        df['price'].fillna(median_price, inplace=True)
    
    if 'category' in df.columns:
        df['category'].replace({'nan': 'Unknown'}, inplace=True)
        df['category'].fillna('Unknown', inplace=True)
    
    # Step 6: Range Validation (e.g. Price > 0)
    df = df[df['price'] > 0]
    
    # Step 7: Validation Assertions
    assert df.isna().sum().sum() == 0, "Validation Failed: Nulls remain!"
    assert df.duplicated().sum() == 0, "Validation Failed: Duplicates remain!"
    print("Pipeline Complete! All quality assertions passed.")
    
    return df

def main():
    print("=== Day 129: Data Cleaning Workflow Demonstration ===")
    
    # Raw Dirty Dataset
    dirty_data = pd.DataFrame({
        ' Product Name ': [' Laptop ', ' Laptop ', ' Mouse ', ' Keyboard ', ' Monitor '],
        ' Category': ['Tech', 'Tech', 'Tech', 'nan', 'Tech'],
        ' Price ': ['$1,200.00', '$1,200.00', '$25.00', 'INVALID', ' $-50.00 ']
    })
    
    print("Raw Dirty Dataset:
", dirty_data)
    print("
Executing Pipeline...
")
    clean_df = clean_dataset_pipeline(dirty_data)
    print("
Final Cleaned Dataset:
", clean_df)

if __name__ == "__main__":
    main()
