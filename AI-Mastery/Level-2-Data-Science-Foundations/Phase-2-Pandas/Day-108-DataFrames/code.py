import pandas as pd
import numpy as np

def main():
    # 1. Create DataFrame
    data = {
        'CustomerID': [101, 102, 103, 104],
        'Age': [25, 45, 35, 50],
        'Income': [55000.0, 95000.0, 72000.0, 120000.0],
        'Status': ['Single', 'Married', 'Single', 'Married']
    }
    df = pd.DataFrame(data)
    
    print("DataFrame:
", df)
    print("
Shape:", df.shape)
    
    # 2. Schema Inspection
    print("
--- Summary Info ---")
    df.info()
    
    print("
--- Numerical Describe ---")
    print(df.describe())
    
    # 3. Rename and Drop
    df_mod = df.rename(columns={'Income': 'Annual_Income'})
    df_mod.drop(columns=['Status'], inplace=True)
    print("
Modified DataFrame (Renamed & Dropped):
", df_mod)

if __name__ == "__main__":
    main()
