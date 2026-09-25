import numpy as np
import matplotlib.pyplot as plt

def discrete_rv_pmf_cdf():
    # Support: X in {1, 2, 3, 4}
    x_vals = np.array([1, 2, 3, 4])
    pmf = np.array([0.1, 0.4, 0.3, 0.2])
    cdf = np.cumsum(pmf)
    
    return x_vals, pmf, cdf

def main():
    print("--- Day 50: Discrete Random Variables ---")
    
    x_vals, pmf, cdf = discrete_rv_pmf_cdf()
    
    print("
1. Discrete PMF and CDF Table:")
    print("  x  | PMF p(x) | CDF F(x)")
    print("  -----------------------")
    for x, p, f in zip(x_vals, pmf, cdf):
        print(f"  {x:d}  |   {p:.2f}   |   {f:.2f}")
        
    # Expectation and Variance
    mean_X = np.sum(x_vals * pmf)
    var_X = np.sum((x_vals - mean_X)**2 * pmf)
    
    print(f"
2. Summary Statistics:")
    print(f"  Mean E[X]:     {mean_X:.4f}")
    print(f"  Variance Var(X): {var_X:.4f}")

if __name__ == "__main__":
    main()
