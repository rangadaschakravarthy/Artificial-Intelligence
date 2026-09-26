import pandas as pd
import numpy as np

def main():
    print("=== Day 163: Outlier Handling Demonstration ===")
    
    df = pd.DataFrame({'Val': [10, 12, 11, 13, 14, 250]})
    
    q05 = df['Val'].quantile(0.05)
    q95 = df['Val'].quantile(0.95)
    
    df['Val_Capped'] = df['Val'].clip(lower=q05, upper=q95)
    print("Capped Dataset:
", df)

if __name__ == "__main__":
    main()
