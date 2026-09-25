import numpy as np

def main():
    print("--- Day 53: Expectation and Variance ---")
    
    # 1. Empirical Verification of Variance Rules
    n_samples = 100000
    X = np.random.normal(loc=10.0, scale=2.0, size=n_samples) # Mean 10, Var 4
    
    a, b = 3.0, 5.0
    Y = a * X + b
    
    print("
1. Linear Transformation Variance Scaling:")
    print(f"  Theoretical Var(X):       4.0000")
    print(f"  Empirical Var(X):         {np.var(X):.4f}")
    print(f"  Theoretical Var(3X + 5):  {3**2 * 4:.4f} (9 * 4 = 36)")
    print(f"  Empirical Var(3X + 5):    {np.var(Y):.4f}")
    
    # 2. Ensemble Variance Reduction Simulation
    # Generate M independent model prediction errors
    M = 10
    model_errors = np.random.normal(loc=0.0, scale=3.0, size=(n_samples, M)) # Var = 9
    ensemble_errors = np.mean(model_errors, axis=1) # Average across M models
    
    print(f"
2. Ensemble Model Variance Reduction (M = {M} models):")
    print(f"  Single Model Error Var:   {np.var(model_errors[:, 0]):.4f} (Expected: 9.0)")
    print(f"  Ensemble Avg Error Var:   {np.var(ensemble_errors):.4f} (Expected: 9/10 = 0.9)")

if __name__ == "__main__":
    main()
