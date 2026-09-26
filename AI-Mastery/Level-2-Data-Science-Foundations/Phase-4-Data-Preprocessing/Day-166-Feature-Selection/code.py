import pandas as pd
from sklearn.feature_selection import VarianceThreshold

def main():
    print("=== Day 166: Feature Selection (VarianceThreshold) Demonstration ===")
    
    df = pd.DataFrame({
        'Const': [5, 5, 5, 5],
        'LowVar': [0, 0, 0, 1],
        'HighVar': [10, 50, 30, 90]
    })
    
    vt = VarianceThreshold(threshold=0.1)
    vt.fit(df)
    
    retained = df.columns[vt.get_support()]
    print("Retained Features:", list(retained))

if __name__ == "__main__":
    main()
