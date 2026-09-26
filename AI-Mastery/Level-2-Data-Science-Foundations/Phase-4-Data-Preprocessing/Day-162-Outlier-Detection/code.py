import pandas as pd
import numpy as np

def main():
    print("=== Day 162: Outlier Detection Demonstration ===")
    
    df = pd.DataFrame({'Salary': [45000, 50000, 52000, 48000, 51000, 500000]})
    
    q1 = df['Salary'].quantile(0.25)
    q3 = df['Salary'].quantile(0.75)
    iqr = q3 - q1
    ub = q3 + 1.5 * iqr
    
    outliers = df[df['Salary'] > ub]
    print(f"IQR Upper Bound: {ub}")
    print("Detected Outlier Rows:
", outliers)

if __name__ == "__main__":
    main()
