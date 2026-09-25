import numpy as np
from scipy import stats

def main():
    print("--- Day 57: Joint Probability Distributions ---")
    
    # 1. 2D Bivariate Normal Distribution Evaluation
    mean = np.array([0.0, 0.0])
    cov = np.array([[2.0, 1.0], 
                    [1.0, 2.0]])
    
    bivariate_norm = stats.multivariate_normal(mean=mean, cov=cov)
    
    # Evaluate Joint Density PDF at point (1, 2)
    pt = np.array([1.0, 2.0])
    pdf_val = bivariate_norm.pdf(pt)
    
    print("
1. Bivariate Normal PDF:")
    print(f"  Mean Vector:       {mean}")
    print(f"  Covariance Matrix:
{cov}")
    print(f"  Joint PDF at (1,2): {pdf_val:.4f}")
    
    # 2. 2D Sample Simulation & Numerical Covariance
    samples = bivariate_norm.rvs(size=100000)
    sample_cov = np.cov(samples, rowvar=False)
    
    print("
2. Simulated 100,000 Points Covariance Matrix:")
    print(np.round(sample_cov, 4))

if __name__ == "__main__":
    main()
