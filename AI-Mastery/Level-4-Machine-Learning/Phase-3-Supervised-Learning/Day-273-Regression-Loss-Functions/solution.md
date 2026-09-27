# Practice Solutions — Day 273

## Basic Solutions
1. Regression Loss Functions & Metrics models $y = \mathbf{X}\boldsymbol{\beta} + \boldsymbol{\epsilon}$.
2. A residual $e_i = y_i - \hat{y}_i$ is the vertical difference between actual target $y_i$ and model prediction $\hat{y}_i$.
3. MAE measures average absolute magnitude of errors; MSE squares errors, penalizing larger outliers more heavily.

## Conceptual Solutions
4. Squaring ensures positive and negative errors don't cancel out, produces a continuous differentiable loss function, and penalizes large errors exponentially.
5. $R^2 = 1 - \frac{\text{SS}_{\text{res}}}{\text{SS}_{\text{tot}}}$. $R^2 = 0.85$ means 85% of target variance is explained by feature inputs.
6. Penalties $\sum |\beta_j|$ or $\sum \beta_j^2$ treat all features equally; unscaled features with large numerical ranges would dominate penalties unfairly.

## Calculation Solutions
7. $e = [1, -1, 0]$. $|e| = [1, 1, 0] \implies \text{MAE} = 2/3 = 0.67$. $e^2 = [1, 1, 0] \implies \text{MSE} = 2/3 = 0.67$. $\text{RMSE} = \sqrt{0.67} = 0.82$.
8. $\bar{x} = 2, \bar{y} = 3.67$. $\sum (x_i - \bar{x})(y_i - \bar{y}) = (-1)(-1.67) + 0 + (1)(1.33) = 3.0$. $\sum (x_i - \bar{x})^2 = 1 + 0 + 1 = 2$. Slope $\beta_1 = 3/2 = 1.5$.

## Implementation Solutions
```python
import numpy as np
from sklearn.linear_model import Ridge

# 9. Normal Equation
def normal_equation(X, y):
    # Add intercept column of ones
    X_b = np.c_[np.ones((len(X), 1)), X]
    return np.linalg.inv(X_b.T.dot(X_b)).dot(X_b.T).dot(y)

# 10. Sklearn Ridge
X = np.array([[1], [2], [3], [4]])
y = np.array([2.1, 3.9, 6.2, 8.1])
model = Ridge(alpha=1.0).fit(X, y)
print("Ridge Slope:", model.coef_[0], "R2:", model.score(X, y))
```

## ML Reasoning Solutions
11. Use Lasso ($L_1$). Lasso performs feature selection by shrinking coefficients of uninformative features exactly to zero.
12. Severe overfitting (high variance). Apply $L_2$ regularization (Ridge), reduce feature complexity, or acquire more training samples.

## Dataset Questions
13. Input features: marketing spend, customer count; Target: quarterly revenue in USD.

## Interview Solutions
14. Derivation: Set $\frac{\partial}{\partial \boldsymbol{\beta}} \|\mathbf{y} - \mathbf{X}\boldsymbol{\beta}\|^2 = -2\mathbf{X}^T(\mathbf{y} - \mathbf{X}\boldsymbol{\beta}) = 0 \implies \mathbf{X}^T\mathbf{X}\boldsymbol{\beta} = \mathbf{X}^T\mathbf{y} \implies \boldsymbol{\beta} = (\mathbf{X}^T\mathbf{X})^{-1}\mathbf{X}^T\mathbf{y}$.
15. Perfect collinearity makes $\mathbf{X}^T\mathbf{X}$ non-invertible ($\det = 0$). Ridge adds $\alpha \mathbf{I}$ to make $(\mathbf{X}^T\mathbf{X} + \alpha \mathbf{I})$ strictly positive-definite and invertible!
