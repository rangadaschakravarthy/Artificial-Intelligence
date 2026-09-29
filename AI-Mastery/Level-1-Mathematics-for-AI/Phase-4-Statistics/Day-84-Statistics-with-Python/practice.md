# Practice Problems — Statistics with Python

## Level 1: Basic Concept Checks
1. Why must `sm.add_constant(X)` be called before fitting `sm.OLS(y, X)` in Statsmodels?
2. What does $R^2$ measure in a linear regression model summary?
3. How does Adjusted $R^2$ differ from standard $R^2$?
4. What hypothesis does the model $F$-statistic test?
5. Which SciPy function performs 1-sample t-testing?

## Level 2: Direct Calculations (Python Code)
6. Write Python code using `statsmodels` to fit OLS model $Y$ on $X_1, X_2$.
7. Extract $95\%$ confidence intervals for regression coefficients from fitted `statsmodels` object.
8. Write Python code to calculate Durbin-Watson autocorrelation statistic for model residuals.
9. Perform Shapiro-Wilk test on OLS residuals in Python.
10. Extract model BIC (Bayesian Information Criterion) from fitted `statsmodels` object.

## Level 3: Conceptual & Multi-Step Problems
11. Explain why Durbin-Watson statistic near $2.0$ indicates uncorrelated residuals, while values $< 1.0$ indicate positive autocorrelation.
12. Explain how multicollinearity inflates coefficient standard errors and how Condition Number in Statsmodels summary alerts to collinearity.
13. Show how Adjusted $R^2 = 1 - \frac{(1-R^2)(N-1)}{N-k-1}$ penalizes adding unnecessary features $k$.
14. Explain how Breusch-Pagan test checks for Heteroscedasticity (non-constant variance) in regression residuals.
15. Compare Statsmodels (statistical inference focus) vs Scikit-Learn (predictive accuracy focus) design philosophies.

## Level 4: AI & ML Applications
16. Write Python code to generate synthetic regression dataset, fit Statsmodels OLS, and print key metrics ($R^2$, $F$-stat $p$-value).
17. Write Python code to plot residual Q-Q plot and residual vs fitted values plot for regression diagnostics.
18. Write Python code using `statsmodels.stats.outliers_influence.variance_inflation_factor` to compute VIF for each feature.
19. Explain how VIF $> 10$ identifies severe multicollinearity.
20. Write Python code to fit Logistic Regression using `sm.Logit` and output Odds Ratios $e^{eta_j}$.

## Level 5: Interview Questions
21. Walk through every section of a Statsmodels OLS summary output table (Dep Variable, $R^2$, $F$-stat, Coefs, Std Err, t, P>|t|, Skewness, Kurtosis, Durbin-Watson, Jarque-Bera).
22. How do you handle heteroscedastic residuals in Statsmodels using robust standard errors (`cov_type='HC3'`)?
23. Write Python code using Statsmodels and SciPy to run complete OLS regression, perform full residual diagnostics, and output summary report.
