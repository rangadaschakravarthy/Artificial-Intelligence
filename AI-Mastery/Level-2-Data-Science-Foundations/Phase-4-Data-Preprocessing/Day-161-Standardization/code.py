import pandas as pd
from sklearn.preprocessing import StandardScaler

def main():
    print("=== Day 161: Z-Score Standardization Demonstration ===")
    
    df = pd.DataFrame({'Income': [30000, 50000, 70000, 90000, 120000]})
    
    scaler = StandardScaler()
    df['Income_ZScore'] = scaler.fit_transform(df[['Income']])
    
    print("Standardized Dataset:
", df.round(3))

if __name__ == "__main__":
    main()
