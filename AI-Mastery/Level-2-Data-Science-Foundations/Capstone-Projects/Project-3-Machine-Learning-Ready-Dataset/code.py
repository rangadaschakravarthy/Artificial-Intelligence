import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

def main():
    print("=== Capstone Project 3: Machine Learning Ready Dataset ===")
    X = pd.DataFrame({'F1': [1, 2, 3, 4, 5]})
    y = np.array([0, 1, 0, 1, 0])
    X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.2, random_state=42)
    scaler = StandardScaler()
    X_tr_s = scaler.fit_transform(X_tr)
    print("ML Ready Train Array Shape:", X_tr_s.shape)

if __name__ == '__main__':
    main()
