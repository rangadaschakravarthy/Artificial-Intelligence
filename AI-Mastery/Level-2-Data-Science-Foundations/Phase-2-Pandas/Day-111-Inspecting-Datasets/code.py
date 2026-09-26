import pandas as pd
import numpy as np

def main():
    # 1. Create Sample Dataset with Anomalies
    df = pd.DataFrame({
        'ID': range(101, 107),
        'Age': [25, 30, np.nan, 45, 50, 35],
        'Income': ['50000', '65000', '70000', 'UNKNOWN', '120000', '85000'],
        'Gender': ['M', 'F', 'F', 'M', 'F', 'M']
    })
    
    print("Raw DataFrame:
", df)
    print("
--- Structural Audit ---")
    print("Shape:", df.shape)
    print("Dtypes:
", df.dtypes)
    
    # 2. Fix String Income Column
    df['Income'] = pd.to_numeric(df['Income'], errors='coerce')
    print("
Post-numeric Conversion Dtypes:
", df.dtypes)
    
    # 3. Missing Value Audit
    missing_table = pd.DataFrame({
        'Count': df.isna().sum(),
        'Percent': df.isna().mean() * 100
    })
    print("
Missing Audit Table:
", missing_table)
    
    # 4. Random Sampling
    print("
Random Sample (n=2):
", df.sample(2, random_state=42))

if __name__ == "__main__":
    main()
