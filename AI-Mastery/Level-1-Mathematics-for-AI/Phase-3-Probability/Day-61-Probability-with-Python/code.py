import numpy as np
from scipy import stats

def main():
    print("--- Day 61: Probability with Python ---")
    
    # 1. Monte Carlo Integration of Intractable Function: integral_0^1 exp(-x^2) dx
    N_sims = 1000000
    x_samples = np.random.uniform(0.0, 1.0, N_sims)
    f_x = np.exp(-x_samples**2)
    mc_integral = np.mean(f_x)
    
    print("
1. Monte Carlo Integration of integral_0^1 exp(-x^2) dx:")
    print(f"  Estimated Integral: {mc_integral:.6f}")
    
    # 2. SciPy Distribution Methods (Normal Distribution)
    dist = stats.norm(loc=100.0, scale=15.0) # IQ Score model
    
    p_gt_130 = 1.0 - dist.cdf(130.0) # Mensa qualification P(IQ > 130)
    iq_99th = dist.ppf(0.99)         # 99th percentile IQ score
    ci_95 = dist.interval(0.95)      # 95% central interval
    
    print("
2. SciPy Normal Distribution Analysis (Mean=100, Std=15):")
    print(f"  P(IQ > 130):       {p_gt_130*100:.2f}%")
    print(f"  99th Percentile:   {iq_99th:.2f}")
    print(f"  95% Central CI:    ({ci_95[0]:.2f}, {ci_95[1]:.2f})")

if __name__ == "__main__":
    main()
