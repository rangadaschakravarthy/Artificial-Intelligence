import numpy as np

def main():
    print("=== NUMPY MINI-PROJECT: NUMERICAL ANALYSIS ENGINE ===")
    
    # Step 1: Generate Synthetic Dataset with NaNs and Outliers
    rng = np.random.default_rng(42)
    n_samples = 200
    
    f0 = rng.normal(50, 10, n_samples)
    f1 = rng.uniform(100, 200, n_samples)
    
    # Inject NaNs
    f0[rng.choice(n_samples, 10, replace=False)] = np.nan
    f1[rng.choice(n_samples, 10, replace=False)] = np.nan
    
    # Inject Outliers
    f0[0] = 999.0
    f1[1] = -500.0
    
    # True Target: y = 2.5*f0 + 1.5*f1 + 10 + noise
    y = 2.5 * np.nan_to_num(f0, nan=50.0) + 1.5 * np.nan_to_num(f1, nan=150.0) + 10.0 + rng.normal(0, 2, n_samples)
    
    X = np.column_stack((f0, f1))
    print(f"Raw Feature Matrix X Shape: {X.shape}")
    print(f"Total NaNs in X: {np.isnan(X).sum()}")
    
    # Step 2: Impute Missing NaNs with Column Medians
    for col_idx in range(X.shape[1]):
        col_data = X[:, col_idx]
        median_val = np.nanmedian(col_data)
        col_data[np.isnan(col_data)] = median_val
    print(f"Post-Imputation NaNs in X: {np.isnan(X).sum()}")
    
    # Step 3: Outlier Clipping (1.5 * IQR)
    for col_idx in range(X.shape[1]):
        col_data = X[:, col_idx]
        q25, q75 = np.percentile(col_data, [25, 75])
        iqr = q75 - q25
        lower, upper = q25 - 1.5 * iqr, q75 + 1.5 * iqr
        X[:, col_idx] = np.clip(col_data, lower, upper)
    print("Outliers clipped cleanly within IQR bounds.")
    
    # Step 4: Feature Standardization (Z-Score via Broadcasting)
    means = X.mean(axis=0)
    stds = X.std(axis=0)
    X_std = (X - means) / stds
    print(f"Standardized Feature Means: {np.round(X_std.mean(axis=0), 4)}")
    print(f"Standardized Feature Stds:  {np.round(X_std.std(axis=0), 4)}")
    
    # Step 5: OLS Linear Regression Model
    # Add bias column of 1s
    X_design = np.column_stack((np.ones(n_samples), X_std))
    
    # Normal Equation: w = (X^T X)^-1 X^T y
    w = np.linalg.pinv(X_design.T @ X_design) @ X_design.T @ y
    y_pred = X_design @ w
    
    # Evaluation Metrics
    mse = np.mean((y - y_pred) ** 2)
    ss_res = np.sum((y - y_pred) ** 2)
    ss_tot = np.sum((y - np.mean(y)) ** 2)
    r2 = 1.0 - (ss_res / ss_tot)
    
    print("
=== MODEL TRAINING RESULTS ===")
    print(f"Trained Weights [Bias, W1, W2]: {np.round(w, 2)}")
    print(f"Model MSE Loss:                 {mse:.4f}")
    print(f"Model R^2 Score:                {r2:.4f}")
    print("
PHASE 1 — NUMPY COMPLETE!")

if __name__ == "__main__":
    main()
