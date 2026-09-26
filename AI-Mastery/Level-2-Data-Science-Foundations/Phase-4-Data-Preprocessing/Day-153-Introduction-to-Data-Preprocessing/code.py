import pandas as pd
import numpy as np

def main():
    print("=== Day 153: Introduction to Data Preprocessing Demonstration ===")
    
    df = pd.DataFrame({
        'Age': [22, 35, 45, 29, 52],
        'Income': [45000, 78000, 110000, 62000, 135000],
        'Tier': ['Basic', 'Premium', 'Enterprise', 'Basic', 'Enterprise']
    })
    print("Raw DataFrame:
", df)
    
    # Preprocessing
    X = pd.get_dummies(df, columns=['Tier'], drop_first=True, dtype=float)
    num_cols = ['Age', 'Income']
    X[num_cols] = (X[num_cols] - X[num_cols].mean()) / X[num_cols].std()
    
    print("
Preprocessed ML-Ready Feature Matrix X:
", X.round(3))

if __name__ == "__main__":
    main()
