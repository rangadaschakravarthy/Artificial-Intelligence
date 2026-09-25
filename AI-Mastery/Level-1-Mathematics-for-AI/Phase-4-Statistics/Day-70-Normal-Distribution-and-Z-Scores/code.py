import numpy as np
from scipy import stats

def main():
    print("--- Day 70: Normal Distribution and Z-Scores ---")
    
    # Generate synthetic feature dataset with an extreme outlier
    np.random.seed(42)
    raw_feature = np.random.normal(loc=50.0, scale=10.0, size=100)
    raw_feature[0] = 95.0 # Add outlier (|Z| > 4.0)
    
    # 1. Compute Z-Scores Manually
    mu = np.mean(raw_feature)
    sigma = np.std(raw_feature, ddof=0)
    z_scores = (raw_feature - mu) / sigma
    
    # 2. Outlier Detection (|Z| > 3.0)
    outlier_mask = np.abs(z_scores) > 3.0
    outliers = raw_feature[outlier_mask]
    cleaned_feature = raw_feature[~outlier_mask]
    
    print("1. StandardScaler Transformation Properties:")
    print(f"  Raw Feature Mean:      {mu:.4f}")
    print(f"  Raw Feature Std Dev:   {sigma:.4f}")
    print(f"  Z-Score Mean:          {np.mean(z_scores):.4f} (Target: 0.0)")
    print(f"  Z-Score Std Dev:       {np.std(z_scores):.4f} (Target: 1.0)")
    
    print(f"
2. Z-Score Outlier Detection (|Z| > 3.0):")
    print(f"  Outliers Flagged:      {outliers}")
    print(f"  Cleaned Dataset Size:  {len(cleaned_feature)} / {len(raw_feature)}")

if __name__ == "__main__":
    main()
