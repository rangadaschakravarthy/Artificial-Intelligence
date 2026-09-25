import numpy as np

def main():
    print("--- Day 54: Covariance and Correlation ---")
    
    # Generate synthetic correlated data
    np.random.seed(42)
    X1 = np.random.normal(10, 2, 10000)
    X2 = 0.8 * X1 + np.random.normal(0, 1, 10000) # Strongly positively correlated with X1
    X3 = -0.5 * X1 + np.random.normal(0, 1, 10000) # Negatively correlated with X1
    
    data_matrix = np.column_stack([X1, X2, X3])
    
    # 1. Compute Sample Covariance Matrix (3x3)
    cov_matrix = np.cov(data_matrix, rowvar=False)
    
    # 2. Compute Sample Correlation Matrix (3x3)
    corr_matrix = np.corrcoef(data_matrix, rowvar=False)
    
    print("
1. Sample Covariance Matrix (3x3):")
    print(np.round(cov_matrix, 4))
    
    print("
2. Sample Correlation Matrix (3x3):")
    print(np.round(corr_matrix, 4))
    
    print(f"
3. Verified Pearson Correlation r(X1, X2): {corr_matrix[0, 1]:.4f}")
    print(f"   Verified Pearson Correlation r(X1, X3): {corr_matrix[0, 2]:.4f}")

if __name__ == "__main__":
    main()
