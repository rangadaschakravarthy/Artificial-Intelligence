import numpy as np
from scipy import stats

def main():
    print("--- Day 78: Introduction to Hypothesis Testing ---")
    
    # 5-Step Hypothesis Testing Framework Script
    # Claim: New AI Model reduces latency below baseline 50.0 ms
    
    # Step 1: Hypotheses
    # H0: mu >= 50.0 ms (Status Quo)
    # Ha: mu < 50.0 ms (One-Tailed Left Test)
    mu_0 = 50.0
    
    # Step 2: Significance Level
    alpha = 0.05
    
    # Step 3: Sample Data & Test Statistic
    np.random.seed(42)
    sample_latency = np.random.normal(loc=47.5, scale=5.0, size=36) # n = 36
    n = len(sample_latency)
    x_bar = np.mean(sample_latency)
    s = np.std(sample_latency, ddof=1)
    se = s / np.sqrt(n)
    
    t_stat = (x_bar - mu_0) / se
    
    # Step 4: Critical Value & p-value
    t_crit = stats.t.ppf(alpha, df=n-1) # One-Tailed Left
    p_val = stats.t.cdf(t_stat, df=n-1)
    
    # Step 5: Decision
    reject_h0 = p_val < alpha
    
    print(f"1. Hypotheses: H0: mu >= {mu_0} ms vs Ha: mu < {mu_0} ms")
    print(f"2. Alpha: {alpha}")
    print(f"3. Sample (n={n}): Mean x_bar = {x_bar:.2f} ms, s = {s:.2f} ms")
    print(f"   Calculated t-Statistic: {t_stat:.4f}")
    print(f"4. Critical Value t_crit:  {t_crit:.4f} | p-value: {p_val:.4f}")
    print(f"5. Decision:               {'REJECT H0 (Significant Latency Reduction!)' if reject_h0 else 'FAIL TO REJECT H0'}")

if __name__ == "__main__":
    main()
