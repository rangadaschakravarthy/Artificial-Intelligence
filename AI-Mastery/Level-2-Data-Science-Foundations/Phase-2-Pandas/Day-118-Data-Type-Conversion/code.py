import pandas as pd
import numpy as np

def main():
    # 1. Dirty Dataset Simulation
    df = pd.DataFrame({
        'Age': ['25', '30', 'INVALID', '40'],
        'Date': ['2026-01-01', '2026-01-02', '2026-01-03', '2026-01-04'],
        'Region': ['North', 'South', 'North', 'South']
    })
    
    print("Original DataFrame Dtypes:
", df.dtypes)
    
    # 2. Robust Numeric Conversion (errors='coerce')
    df['Age'] = pd.to_numeric(df['Age'], errors='coerce')
    
    # 3. Datetime Conversion
    df['Date'] = pd.to_datetime(df['Date'])
    
    # 4. Categorical Conversion
    mem_before = df['Region'].memory_usage(deep=True)
    df['Region'] = df['Region'].astype('category')
    mem_after = df['Region'].memory_usage(deep=True)
    
    print("
Converted DataFrame:
", df)
    print("
Converted Data Types:
", df.dtypes)
    print(f"
Region Memory Before: {mem_before} bytes | After: {mem_after} bytes")

if __name__ == "__main__":
    main()
