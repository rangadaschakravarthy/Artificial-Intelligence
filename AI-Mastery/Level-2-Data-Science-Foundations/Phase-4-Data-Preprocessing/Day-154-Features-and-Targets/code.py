import pandas as pd
import numpy as np

def main():
    print("=== Day 154: Features and Targets Demonstration ===")
    
    df = pd.DataFrame({
        'SquareFt': [1200, 1800, 2400],
        'Bedrooms': [2, 3, 4],
        'Condition': ['Fair', 'Good', 'Excellent'],
        'ZipCode': ['90210', '10001', '90210'],
        'Price': [350000, 520000, 750000]
    })
    
    target_col = 'Price'
    X = df.drop(columns=[target_col])
    y = df[target_col]
    
    print("Feature Matrix X:
", X)
    print("
Target Vector y:
", y.values)

if __name__ == "__main__":
    main()
