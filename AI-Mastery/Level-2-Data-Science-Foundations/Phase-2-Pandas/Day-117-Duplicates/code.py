import pandas as pd
import numpy as np

def main():
    # 1. Create DataFrame with Duplicates
    df = pd.DataFrame({
        'User_ID': [101, 102, 101, 103, 101],
        'Action': ['Login', 'Purchase', 'Login', 'Login', 'Logout'],
        'Amount': [0, 50, 0, 0, 0]
    })
    
    print("Original DataFrame:
", df)
    print("
Duplicate Rows Count:", df.duplicated().sum())
    
    # 2. Exact Duplicate Drop (keeps first)
    print("
Drop Exact Duplicates:
", df.drop_duplicates())
    
    # 3. Subset Deduplication (User_ID)
    print("
Keep FIRST per User_ID:
", df.drop_duplicates(subset=['User_ID'], keep='first'))
    print("
Keep LAST per User_ID:
", df.drop_duplicates(subset=['User_ID'], keep='last'))
    print("
Keep NONE (keep=False):
", df.drop_duplicates(subset=['User_ID'], keep=False))

if __name__ == "__main__":
    main()
