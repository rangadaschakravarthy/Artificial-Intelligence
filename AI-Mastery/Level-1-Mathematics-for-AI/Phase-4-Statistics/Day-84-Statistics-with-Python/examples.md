# Worked Examples — Statistics with Python

## Example 1: Fitting OLS Model in Statsmodels
**Problem**: Fit linear model $Y = eta_0 + eta_1 X + \epsilon$ using `statsmodels`.
**Solution**:
```python
import statsmodels.api as sm

X_with_const = sm.add_constant(X)  # Add intercept column
model = sm.OLS(y, X_with_const).fit()
print(model.summary())
```

## Example 2: Extracting R-squared and p-values
**Problem**: Extract $R^2$ and coefficient $p$-values programmatically.
**Solution**:
```python
r2 = model.rsquared
p_vals = model.pvalues
# r2 gives float, p_vals gives Pandas Series
```

## Example 3: One-Way ANOVA in Statsmodels
**Problem**: Perform 1-Way ANOVA across 3 groups using formula interface.
**Solution**:
```python
import statsmodels.api as sm
from statsmodels.formula.api import ols

model = ols('score ~ C(group)', data=df).fit()
anova_table = sm.stats.anova_lm(model, typ=2)
print(anova_table)
```

## Example 4: Residual Normality Diagnostic
**Problem**: Check if OLS residuals are Normally distributed.
**Solution**:
```python
residuals = model.resid
sw_stat, sw_p = stats.shapiro(residuals)
# sw_p > 0.05 confirms Gaussian residual assumption
```

## Example 5: Statsmodels GLM (Logistic Regression)
**Problem**: Fit binary logistic regression in `statsmodels`.
**Solution**:
```python
import statsmodels.api as sm

logit_model = sm.Logit(y, sm.add_constant(X)).fit()
print(logit_model.summary())
```
