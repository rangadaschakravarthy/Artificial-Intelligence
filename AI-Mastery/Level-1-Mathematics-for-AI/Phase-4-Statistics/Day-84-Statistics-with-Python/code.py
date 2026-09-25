import numpy as np
import statsmodels.api as sm
from scipy import stats

def main():
    print("--- Day 84: Statistics with Python (Statsmodels OLS) ---")
    
    # Generate Synthetic Regression Dataset
    np.random.seed(42)
    n = 100
    X1 = np.random.normal(0, 1, n)
    X2 = np.random.normal(0, 1, n)
    # Target Y = 2.5 + 3.0*X1 - 1.5*X2 + noise
    y = 2.5 + 3.0 * X1 - 1.5 * X2 + np.random.normal(0, 0.5, n)
    
    X = np.column_stack([X1, X2])
    X_const = sm.add_constant(X)
    
    # Fit Statsmodels OLS
    model = sm.OLS(y, X_const).fit()
    
    # Extract Key Metrics Programmatically
    r2 = model.rsquared
    adj_r2 = model.rsquared_adj
    f_pvalue = model.f_pvalue
    params = model.params
    pvalues = model.pvalues
    
    # Residual Normality Diagnostic
    residuals = model.resid
    sw_stat, sw_p = stats.shapiro(residuals)
    
    print("1. OLS Regression Results:")
    print(f"  R-Squared:             {r2:.4f} (99%+ Variance Explained)")
    print(f"  Adjusted R-Squared:    {adj_r2:.4f}")
    print(f"  Overall F-Stat p-val:  {f_pvalue:.4e} (Model is Highly Significant!)")
    
    print("
2. Parameter Coefficients & p-values:")
    print(f"  Intercept (beta_0):   Coef = {params[0]:.4f} | p-value = {pvalues[0]:.4e}")
    print(f"  Feature 1 (beta_1):   Coef = {params[1]:.4f} | p-value = {pvalues[1]:.4e}")
    print(f"  Feature 2 (beta_2):   Coef = {params[2]:.4f} | p-value = {pvalues[2]:.4e}")
    
    print(f"
3. Residual Diagnostics:")
    print(f"  Shapiro-Wilk Normality p-val: {sw_p:.4f} -> {'RESIDUALS NORMAL' if sw_p > 0.05 else 'NON-NORMAL'}")

if __name__ == "__main__":
    main()
