import numpy as np
from scipy import stats

def main():
    print("--- Day 51: Continuous Random Variables ---")
    
    # 1. Standard Normal Distribution X ~ N(0, 1)
    mu, sigma = 0.0, 1.0
    norm_dist = stats.norm(loc=mu, scale=sigma)
    
    # PDF at x = 0
    pdf_at_0 = norm_dist.pdf(0.0)
    # CDF at x = 1.96 (97.5th percentile)
    cdf_at_196 = norm_dist.cdf(1.96)
    # Interval Probability P(-1 <= X <= 1)
    prob_interval = norm_dist.cdf(1.0) - norm_dist.cdf(-1.0)
    
    print("
1. Standard Normal Distribution Properties:")
    print(f"  PDF f(0):            {pdf_at_0:.4f}")
    print(f"  CDF F(1.96):         {cdf_at_196:.4f}")
    print(f"  P(-1 <= X <= 1):     {prob_interval:.4f} (Empirical 68% Rule)")
    
    # 2. Numerical Integration Verification
    x_samples = np.linspace(-5, 5, 10000)
    dx = x_samples[1] - x_samples[0]
    total_area = np.sum(norm_dist.pdf(x_samples)) * dx
    print(f"
2. Total Area under PDF Integral: {total_area:.6f} (Expected: 1.000000)")

if __name__ == "__main__":
    main()
