# Code — Day 261: Prediction & Inference
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

def demonstrate_day_concept():
    print("--- Day 261: Prediction & Inference Demonstration ---")
    
    # 1. Generate Synthetic Dataset (n=100 samples, d=3 features)
    np.random.seed(42)
    n_samples, n_features = 100, 3
    
    X_raw = np.random.randn(n_samples, n_features) * 10 + 50
    # True relationship: y = 2*x0 - 1.5*x1 + 0.5*x2 + noise
    y_raw = 2 * X_raw[:, 0] - 1.5 * X_raw[:, 1] + 0.5 * X_raw[:, 2] + np.random.randn(n_samples) * 2
    
    # Convert to DataFrame
    df = pd.DataFrame(X_raw, columns=["feature_1", "feature_2", "feature_3"])
    df["target"] = y_raw
    
    print("Dataset Head:")
    print(df.head())
    
    # 2. Train / Test Split
    X = df.drop(columns=["target"]).values
    y = df["target"].values
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # 3. Standardize Features
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    print("\nFeature Matrix X_train shape:", X_train.shape)
    print("Feature Matrix X_test shape :", X_test.shape)
    print("Target Vector y_train shape  :", y_train.shape)
    print("Target Vector y_test shape   :", y_test.shape)
    print("\nScaling Complete! Mean of scaled X_train:", np.round(X_train_scaled.mean(axis=0), 2))

if __name__ == "__main__":
    demonstrate_day_concept()
