import numpy as np
from scipy import stats
from statsmodels.stats.proportion import proportion_confint, proportions_ztest

def main():
    print("--- Day 71: Bernoulli and Binomial Statistical Foundations ---")
    
    # A/B Test Conversion Data
    n_A, n_B = 1000, 1000
    success_A, success_B = 100, 130  # 10% vs 13% conversion
    
    p_hat_A = success_A / n_A
    p_hat_B = success_B / n_B
    se_A = np.sqrt(p_hat_A * (1 - p_hat_A) / n_A)
    
    # 95% Confidence Interval for Variant A
    ci_low_A, ci_high_A = proportion_confint(success_A, n_A, alpha=0.05, method='normal')
    
    # 2-Sample Z-Test for Proportions
    z_stat, p_val = proportions_ztest([success_B, success_A], [n_B, n_A], alternative='two-sided')
    
    print("1. Variant A Conversion Proportion Analysis:")
    print(f"  Sample Accuracy p_hat_A: {p_hat_A:.4f} ({p_hat_A*100:.1f}%)")
    print(f"  Standard Error SE:       {se_A:.4f}")
    print(f"  95% Normal CI:           [{ci_low_A:.4f}, {ci_high_A:.4f}]")
    
    print("
2. A/B Test 2-Sample Z-Test Result (Variant B vs Variant A):")
    print(f"  Variant B p_hat_B:       {p_hat_B:.4f} ({p_hat_B*100:.1f}%)")
    print(f"  Z-Statistic:             {z_stat:.4f}")
    print(f"  p-value:                 {p_val:.4f}")
    print(f"  Conclusion:              {'STATISTICALLY SIGNIFICANT LIFT (p < 0.05)' if p_val < 0.05 else 'NOT SIGNIFICANT'}")

if __name__ == "__main__":
    main()
