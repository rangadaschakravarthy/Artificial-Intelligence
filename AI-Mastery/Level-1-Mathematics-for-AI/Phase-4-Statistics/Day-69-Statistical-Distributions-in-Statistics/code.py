import numpy as np
from scipy import stats

def main():
    print("--- Day 69: Statistical Distributions in Statistics ---")
    
    np.random.seed(42)
    # Generate Normal vs Skewed Exponential datasets
    normal_data = np.random.normal(loc=10.0, scale=2.0, size=100)
    skewed_data = np.random.exponential(scale=2.0, size=100)
    
    # Shapiro-Wilk Normality Test
    sw_norm_stat, sw_norm_p = stats.shapiro(normal_data)
    sw_skew_stat, sw_skew_p = stats.shapiro(skewed_data)
    
    print("1. Shapiro-Wilk Normality Test Results (alpha = 0.05):")
    print(f"  Normal Data:   Stat={sw_norm_stat:.4f}, p-value={sw_norm_p:.4f} -> {'NORMAL' if sw_norm_p > 0.05 else 'NON-NORMAL'}")
    print(f"  Skewed Data:   Stat={sw_skew_stat:.4f}, p-value={sw_skew_p:.4f} -> {'NORMAL' if sw_skew_p > 0.05 else 'NON-NORMAL'}")
    
    # 2-Sample Kolmogorov-Smirnov Test (Data Drift Check)
    ks_stat, ks_p = stats.ks_2samp(normal_data, skewed_data)
    print(f"
2. 2-Sample KS Test (Data Drift Detection):")
    print(f"  KS Statistic: {ks_stat:.4f}, p-value: {ks_p:.4e}")
    print(f"  Result:       {'SAME Distribution' if ks_p > 0.05 else 'DIFFERENT Distributions (Drift Detected!)'}")

if __name__ == "__main__":
    main()
