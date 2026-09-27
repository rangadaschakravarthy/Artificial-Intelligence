# Examples — Day 275: Regularization (Ridge, Lasso & ElasticNet)

## Example 1 — Extremely Simple
Fitting a line to two points $(0, 1)$ and $(2, 5) \implies y = 2x + 1$.

## Example 2 — Basic Numerical Calculation
Computing MSE, MAE, and $R^2$ for $y = [10, 20, 30]$ and $\hat{y} = [12, 18, 33]$.
- $\text{MAE} = (2 + 2 + 3)/3 = 2.33$.
- $\text{MSE} = (4 + 4 + 9)/3 = 5.67$.
- $\text{RMSE} = \sqrt{5.67} = 2.38$.

## Example 3 — Real Dataset Example (Boston Housing / California Housing)
Predicting median house value from median income, house age, and room counts.

## Example 4 — Machine Learning Pipeline Example
Applying `StandardScaler` + `Ridge(alpha=1.0)` to prevent multicollinearity issues.

## Example 5 — Real-World Scenario (Salary Prediction)
Predicting software engineer salary based on years of experience, education level, and location.

## Example 6 — Interview-Style Example
Explaining why Lasso ($L_1$) creates sparse weights (drives coefficients exactly to zero) whereas Ridge ($L_2$) shrinks them continuously.
