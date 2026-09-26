import pandas as pd
import numpy as np

def main():
    # 1. NaN Behavior
    print("np.nan == np.nan:", np.nan == np.nan)
    print("pd.isna(np.nan): ", pd.isna(np.nan))
    
    # 2. DataFrame Missing Audit
    df = pd.DataFrame({
        'A': [1.0, 2.0, np.nan, 4.0, 5.0],
        'B': [np.nan, 2.0, np.nan, 4.0, np.nan], # 60% missing
        'C': ['X', 'Y', 'Z', 'W', 'V']
    })
    
    print("
DataFrame:
", df)
    
    missing_summary = pd.DataFrame({
        'Missing_Count': df.isna().sum(),
        'Missing_Percent': df.isna().mean() * 100
    })
    print("
Missing Summary Table:
", missing_summary)
    
    # 3. Filter Rows with Any NaN
    print("
Rows with ANY NaN:
", df[df.isna().any(axis=1)])
    print("
Rows with NO NaN:
", df[df.notna().all(axis=1)])

if __name__ == "__main__":
    main()
