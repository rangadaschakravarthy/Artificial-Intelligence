import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

def main():
    print("=== Day 168: Data Leakage Prevention Demonstration ===")
    
    np.random.seed(42)
    X = pd.DataFrame({'Val': np.random.normal(100, 20, 100)})
    y = np.random.choice([0, 1], 100)
    
    # 1. Train/Test Split FIRST
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # 2. Fit Scaler ONLY on Training Data
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    print("Scaler Mean computed strictly from X_train:", scaler.mean_[0].round(3))
    print("Leak-Free Preprocessing Complete!")

if __name__ == "__main__":
    main()
