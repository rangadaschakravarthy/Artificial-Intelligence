import numpy as np

def binary_cross_entropy(y_true, y_pred):
    eps = 1e-15 # Numerical stability clip
    y_pred = np.clip(y_pred, eps, 1 - eps)
    return -np.mean(y_true * np.log(y_pred) + (1 - y_true) * np.log(1 - y_pred))

def main():
    print("--- Day 59: Probability for Machine Learning ---")
    
    # 1. Empirical Coin Flip MLE vs MAP
    np.random.seed(42)
    flips = np.random.binomial(1, p=0.70, size=10) # 10 flips
    k = np.sum(flips)
    N = len(flips)
    
    # MLE
    p_mle = k / N
    # MAP with Beta(2, 2) prior
    alpha, beta = 2.0, 2.0
    p_map = (k + alpha - 1) / (N + alpha + beta - 2)
    
    print("
1. Coin Flip Parameter Estimation (N = 10 trials):")
    print(f"  Observed Heads:    {k} / {N}")
    print(f"  True Probability:  0.7000")
    print(f"  MLE Estimate:      {p_mle:.4f}")
    print(f"  MAP Estimate:      {p_map:.4f} (Pulled toward 0.5 prior)")
    
    # 2. Binary Cross-Entropy Loss Calculation
    y_true = np.array([1, 1, 0, 0])
    y_pred_good = np.array([0.9, 0.8, 0.1, 0.2])
    y_pred_bad  = np.array([0.2, 0.3, 0.7, 0.8])
    
    print("
2. Binary Cross-Entropy Loss (NLL):")
    print(f"  Good Model Loss: {binary_cross_entropy(y_true, y_pred_good):.4f}")
    print(f"  Bad Model Loss:  {binary_cross_entropy(y_true, y_pred_bad):.4f}")

if __name__ == "__main__":
    main()
