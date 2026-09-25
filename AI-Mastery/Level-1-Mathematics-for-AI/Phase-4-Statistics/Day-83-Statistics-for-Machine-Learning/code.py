import numpy as np
from scipy import stats
from sklearn.feature_selection import SelectKBest, f_classif

def main():
    print("--- Day 83: Statistics for Machine Learning ---")
    
    # 1. Statistical Feature Selection via ANOVA F-Test
    np.random.seed(42)
    n_samples, n_features = 200, 10
    X = np.random.randn(n_samples, n_features)
    # Make feature 0 and feature 2 strongly predictive of y
    y = np.random.choice([0, 1], size=n_samples)
    X[y == 1, 0] += 1.5 # Feature 0 signal
    X[y == 1, 2] += 2.0 # Feature 2 signal
    
    selector = SelectKBest(score_func=f_classif, k=2)
    selector.fit(X, y)
    
    scores = selector.scores_
    pvalues = selector.pvalues_
    selected_indices = selector.get_support(indices=True)
    
    print("1. ANOVA F-Test Feature Ranking:")
    for idx in range(n_features):
        print(f"  Feature {idx}: F-Score = {scores[idx]:6.2f} | p-value = {pvalues[idx]:.4e} {'[SELECTED]' if idx in selected_indices else ''}")
        
    # 2. Multiple Testing Bonferroni Adjustment
    alpha = 0.05
    bonf_alpha = alpha / n_features
    sig_features = np.where(pvalues < bonf_alpha)[0]
    
    print(f"
2. Bonferroni Multiple Testing Adjustment (alpha = {alpha}, n_features = {n_features}):")
    print(f"  Adjusted Threshold alpha_bonf: {bonf_alpha:.4f}")
    print(f"  Surviving Features (p < alpha_bonf): {sig_features}")

if __name__ == "__main__":
    main()
