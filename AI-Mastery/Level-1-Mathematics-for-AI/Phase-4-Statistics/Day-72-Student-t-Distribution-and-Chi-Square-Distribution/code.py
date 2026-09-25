import numpy as np
from scipy import stats

def main():
    print("--- Day 72: Student's t-Distribution and Chi-Square Distribution ---")
    
    # 1. Student's t-Distribution Analysis (N = 16, df = 15)
    N = 16
    df_t = N - 1
    sample_mean, mu_0 = 54.0, 50.0
    sample_s = 8.0
    
    se = sample_s / np.sqrt(N)
    t_stat = (sample_mean - mu_0) / se
    
    p_val_t = 2 * (1 - stats.t.cdf(np.abs(t_stat), df=df_t))
    t_crit = stats.t.ppf(0.975, df=df_t)
    
    print("1. One-Sample t-Test Results (df = 15):")
    print(f"  t-Statistic:    {t_stat:.4f}")
    print(f"  Critical t (95%): +/- {t_crit:.4f}")
    print(f"  p-value:        {p_val_t:.4f}")
    print(f"  Decision:       {'REJECT H0' if p_val_t < 0.05 else 'FAIL TO REJECT H0'}")
    
    # 2. Chi-Square Test for Independence
    # Contingency Table: Device vs Purchase (2x2)
    obs_table = np.array([
        [120, 80],  # Mobile: [Purchase, No Purchase]
        [150, 50]   # Desktop: [Purchase, No Purchase]
    ])
    
    chi2_stat, chi2_p, dof, expected = stats.chi2_contingency(obs_table)
    
    print(f"
2. Chi-Square Test for Independence (2x2 Table, dof = {dof}):")
    print(f"  Chi2 Statistic: {chi2_stat:.4f}")
    print(f"  p-value:        {chi2_p:.4f}")
    print(f"  Decision:       {'DEPENDENT (p < 0.05)' if chi2_p < 0.05 else 'INDEPENDENT'}")

if __name__ == "__main__":
    main()
