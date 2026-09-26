import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

def main():
    print("=== LEVEL 2 FINAL DATA SCIENCE PROJECT CAPSTONE ===")
    # 1. Ingest
    np.random.seed(42)
    df = pd.DataFrame({
        'Age': [25, 30, 45, 50, 35, 28, 40, 55],
        'Income': [50000, 65000, 95000, 120000, 75000, 58000, 88000, 140000],
        'Churn': [0, 0, 1, 0, 0, 1, 0, 1]
    })
    
    # 2. Split
    X = df.drop(columns=['Churn'])
    y = df['Churn']
    X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.25, random_state=42)
    
    # 3. Preprocess
    scaler = StandardScaler()
    X_tr_s = scaler.fit_transform(X_tr)
    X_te_s = scaler.transform(X_te)
    
    print("Final Capstone Preprocessed Array Shapes:")
    print("X_train_scaled:", X_tr_s.shape)
    print("X_test_scaled: ", X_te_s.shape)

if __name__ == '__main__':
    main()
