import pandas as pd
from sklearn.preprocessing import MinMaxScaler

def main():
    print("=== Day 160: Min-Max Normalization Demonstration ===")
    
    df = pd.DataFrame({'Age': [20, 30, 40, 50, 60]})
    
    scaler = MinMaxScaler(feature_range=(0, 1))
    df['Age_Normalized'] = scaler.fit_transform(df[['Age']])
    
    print("Min-Max Normalized Dataset:
", df)

if __name__ == "__main__":
    main()
