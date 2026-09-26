import pandas as pd
import numpy as np
from sklearn.preprocessing import PowerTransformer

def main():
    print("=== Day 165: Log & Power Transformations Demonstration ===")
    
    np.random.seed(42)
    skewed_data = np.random.exponential(scale=100, size=100)
    df = pd.DataFrame({'Raw': skewed_data})
    
    df['Log1p'] = np.log1p(df['Raw'])
    pt = PowerTransformer(method='yeo-johnson')
    df['Yeo_Johnson'] = pt.fit_transform(df[['Raw']])
    
    print(f"Raw Skewness:         {df['Raw'].skew():.3f}")
    print(f"Log1p Skewness:       {df['Log1p'].skew():.3f}")
    print(f"Yeo-Johnson Skewness: {df['Yeo_Johnson'].skew():.3f}")

if __name__ == "__main__":
    main()
