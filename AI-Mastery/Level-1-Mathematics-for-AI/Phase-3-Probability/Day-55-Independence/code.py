import numpy as np
from scipy import stats

def main():
    print("--- Day 55: Independence ---")
    
    # 1. Independent vs Dependent Variables Verification
    n_samples = 100000
    # Independent variables
    X_indep = np.random.normal(0, 1, n_samples)
    Y_indep = np.random.normal(0, 1, n_samples)
    
    # Dependent variables (Y = X^2)
    X_dep = np.random.uniform(-1, 1, n_samples)
    Y_dep = X_dep**2
    
    print("
1. Expectation Product Rule E[XY] == E[X]*E[Y]:")
    print("  Independent Pair:")
    print(f"    E[X*Y]:     {np.mean(X_indep * Y_indep):.4f}")
    print(f"    E[X]*E[Y]:  {np.mean(X_indep) * np.mean(Y_indep):.4f}")
    
    print("  Dependent Pair (Y = X^2):")
    print(f"    E[X*Y] (E[X^3]): {np.mean(X_dep * Y_dep):.4f}")
    print(f"    E[X]*E[Y]:       {np.mean(X_dep) * np.mean(Y_dep):.4f}")
    print(f"    Covariance:      {np.cov(X_dep, Y_dep)[0, 1]:.4f} (Zero Covariance despite Dependence!)")
    
    # 2. Chi-Square Independence Test
    # Categorical dataset
    obs = np.array([[10, 10], [20, 20]]) # Perfectly independent proportions
    chi2, p_val, dof, _ = stats.chi2_contingency(obs)
    print(f"
2. Chi-Square Independence Test (Independent Data):")
    print(f"  Chi2 Statistic: {chi2:.4f}, p-value: {p_val:.4f} (p > 0.05 -> Independent)")

if __name__ == "__main__":
    main()
