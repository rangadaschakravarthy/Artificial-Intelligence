# Practice Questions — Day 270

## Basic Questions
1. Define the mathematical model for Simple Linear Regression.
2. What is a residual error $e_i = y_i - \hat{y}_i$?
3. Explain the difference between MAE and MSE.

## Conceptual Questions
4. Why do we square errors in Ordinary Least Squares (OLS)?
5. Explain $R^2$ (Coefficient of Determination) and how to interpret $R^2 = 0.85$.
6. Why is feature scaling mandatory before fitting Ridge or Lasso regression?

## Calculation Questions
7. Given $y = [3, 5, 7]$ and $\hat{y} = [2, 6, 7]$, compute MAE, MSE, and RMSE.
8. Calculate the slope $\beta_1$ for data points $(1, 2), (2, 4), (3, 5)$.

## Implementation Questions
9. Write a NumPy function solving the Normal Equation $\boldsymbol{\beta} = (\mathbf{X}^T\mathbf{X})^{-1}\mathbf{X}^T\mathbf{y}$.
10. Implement `sklearn.linear_model.Ridge` and evaluate test $R^2$ score.

## ML Reasoning Questions
11. You have 100 features and suspect 90 of them are uninformative noise. Should you use Ridge or Lasso? Explain.
12. Your regression model gets $R^2 = 0.99$ on training data but $R^2 = 0.20$ on test data. Diagnose and prescribe a fix.

## Dataset Questions
13. Identify features, target, and units in a given sales dataset table.

## Interview Questions
14. Derive the OLS Normal Equation $\boldsymbol{\beta} = (\mathbf{X}^T\mathbf{X})^{-1}\mathbf{X}^T\mathbf{y}$.
15. What happens to $(\mathbf{X}^T\mathbf{X})^{-1}$ when features are perfectly collinear? How does Ridge regression fix this?
