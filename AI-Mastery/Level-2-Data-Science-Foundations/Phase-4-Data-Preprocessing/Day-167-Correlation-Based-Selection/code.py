import pandas as pd
import numpy as np

def main():
    print("=== Day 167: Correlation-Based Selection Demonstration ===")
    
    np.random.seed(42)
    f1 = np.random.randn(100)
    f2 = f1 * 0.99 # Redundant copy of f1
    f3 = np.random.randn(100)
    
    df = pd.DataFrame({'F1': f1, 'F2': f2, 'F3': f3})
    
    corr = df.corr().abs()
    upper = corr.where(np.triu(np.ones(corr.shape), k=1).astype(bool))
    to_drop = [col for col in upper.columns if any(upper[col] > 0.90)]
    
    print("High Correlation Matrix:
", corr.round(2))
    print("
Dropped Redundant Columns:", to_drop)

if __name__ == "__main__":
    main()
