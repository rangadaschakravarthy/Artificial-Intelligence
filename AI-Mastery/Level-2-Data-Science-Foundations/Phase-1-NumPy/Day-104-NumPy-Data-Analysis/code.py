import numpy as np

def main():
    # 1. Percentiles & Five-Number Summary
    data = np.array([10, 15, 20, 25, 30, 40, 50, 100])
    q25, q50, q75 = np.percentile(data, [25, 50, 75])
    iqr = q75 - q25
    
    print("Data:", data)
    print(f"Q1 (25%): {q25}, Q2 (Median): {q50}, Q3 (75%): {q75}")
    print(f"IQR: {iqr}, Upper Bound (Q3 + 1.5*IQR): {q75 + 1.5*iqr}")
    
    # 2. Outlier Filtering
    clean = data[data <= q75 + 1.5 * iqr]
    print("Clean Data (no outliers):", clean)
    
    # 3. Pearson Correlation Matrix
    rng = np.random.default_rng(42)
    x1 = rng.normal(0, 1, 100)
    x2 = x1 * 3.0 + rng.normal(0, 0.2, 100) # Highly correlated
    X = np.column_stack((x1, x2))
    
    corr = np.corrcoef(X, rowvar=False)
    print("
Feature Matrix X shape:", X.shape)
    print("Pearson Correlation Matrix:
", np.round(corr, 3))

if __name__ == "__main__":
    main()
