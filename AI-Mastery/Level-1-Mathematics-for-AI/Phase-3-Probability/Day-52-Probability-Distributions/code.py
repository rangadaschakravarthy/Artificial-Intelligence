import numpy as np
from scipy import stats

def main():
    print("--- Day 52: Probability Distributions ---")
    
    # 1. Binomial Distribution
    n, p = 10, 0.5
    binom_dist = stats.binom(n, p)
    print(f"
1. Binomial(n={n}, p={p}):")
    print(f"  P(X = 5):     {binom_dist.pmf(5):.4f}")
    print(f"  Mean E[X]:    {binom_dist.mean():.4f}")
    print(f"  Var Var(X):   {binom_dist.var():.4f}")
    
    # 2. Poisson Distribution
    lam = 3.0
    poisson_dist = stats.poisson(lam)
    print(f"
2. Poisson(lambda={lam}):")
    print(f"  P(X = 0):     {poisson_dist.pmf(0):.4f}")
    print(f"  P(X <= 2):    {poisson_dist.cdf(2):.4f}")
    
    # 3. Gaussian Distribution
    mu, sigma = 0.0, 1.0
    norm_dist = stats.norm(loc=mu, scale=sigma)
    samples = norm_dist.rvs(size=100000)
    print(f"
3. Standard Normal N(0, 1) Simulation (100,000 samples):")
    print(f"  Sample Mean:  {np.mean(samples):.4f} (Expected: 0.0)")
    print(f"  Sample Var:   {np.var(samples):.4f} (Expected: 1.0)")

if __name__ == "__main__":
    main()
