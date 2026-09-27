# Code — Day 271: Multiple Linear Regression
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.metrics import mean_squared_error, r2_score

def demonstrate_regression():
    print("--- Day 271: Multiple Linear Regression Demo ---")
    
    # Generate Synthetic Dataset
    np.random.seed(42)
    X = np.random.rand(100, 3) * 10
    # True relation: y = 3*x0 - 2*x1 + 0*x2 + 5 + noise
    y = 3 * X[:, 0] - 2 * X[:, 1] + 5 + np.random.randn(100) * 1.5
    
    # 1. Scratch OLS via Normal Equation
    X_b = np.c_[np.ones((len(X), 1)), X]
    beta_scratch = np.linalg.inv(X_b.T.dot(X_b)).dot(X_b.T).dot(y)
    
    # 2. Sklearn Models
    ols = LinearRegression().fit(X, y)
    ridge = Ridge(alpha=10.0).fit(X, y)
    lasso = Lasso(alpha=0.5).fit(X, y)
    
    print("Scratch OLS Betas (b0, b1, b2, b3):", np.round(beta_scratch, 3))
    print("Sklearn OLS Coefficients           :", np.round(ols.coef_, 3), "Intercept:", round(ols.intercept_, 3))
    print("Sklearn Ridge (alpha=10) Coefs     :", np.round(ridge.coef_, 3))
    print("Sklearn Lasso (alpha=0.5) Coefs    :", np.round(lasso.coef_, 3))
    
    # Evaluate OLS
    y_pred = ols.predict(X)
    print(f"\nOLS MSE : {mean_squared_error(y, y_pred):.3f}")
    print(f"OLS R2  : {r2_score(y, y_pred):.3f}")

if __name__ == "__main__":
    demonstrate_regression()
