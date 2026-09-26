import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

def main():
    print("=== Day 169: Train-Test Concept Demonstration ===")
    
    np.random.seed(42)
    X = pd.DataFrame({'Feature': np.random.randn(100)})
    y = pd.Series([0]*80 + [1]*20) # 80:20 imbalanced
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42, stratify=y)
    
    print("Train Shape:", X_train.shape, "Test Shape:", X_test.shape)
    print("Train Class 1 Ratio:", y_train.mean())
    print("Test Class 1 Ratio: ", y_test.mean())

if __name__ == "__main__":
    main()
