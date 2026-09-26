import pandas as pd
import numpy as np

def main():
    print("=== Day 127: Time Series Demonstration ===")
    
    # 1. Parsing Raw Date Strings
    raw_data = {
        'Date_Str': ['2023-01-15 08:30', '2023-01-16 10:15', '2023-02-01 14:00', '2023-02-15 09:00'],
        'Revenue': [1200, 1500, 2200, 1800]
    }
    df = pd.DataFrame(raw_data)
    
    # 2. Convert to DatetimeIndex
    df['Timestamp'] = pd.to_datetime(df['Date_Str'])
    df.set_index('Timestamp', inplace=True)
    df.sort_index(inplace=True)
    
    print("Parsed Time Series DataFrame:
", df)
    print("Index Dtype:", df.index.dtype)
    
    # 3. Partial String Slicing
    print("
--- 1. Partial String Slicing (January 2023) ---")
    jan_data = df.loc['2023-01']
    print(jan_data)
    
    # 4. Generating Date Ranges
    print("
--- 2. Date Range Generation (pd.date_range) ---")
    bday_range = pd.date_range(start='2023-01-01', periods=5, freq='B')
    print("5 Business Days:", bday_range)

if __name__ == "__main__":
    main()
