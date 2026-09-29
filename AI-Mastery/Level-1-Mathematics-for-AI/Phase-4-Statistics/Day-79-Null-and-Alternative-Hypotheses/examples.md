# Worked Examples — Null and Alternative Hypotheses

## Example 1: Fraud Detection False Positive Reduction
**Problem**: Security team wants to prove new model reduces False Positive Rate ($FPR$) below baseline $5\%$.
**Solution**:
- $H_0: FPR \ge 0.05$
- $H_a: FPR < 0.05$ (1-Tailed Left)

## Example 2: Non-Inferiority Testing
**Problem**: Test if compressed mobile AI model is no worse than cloud model accuracy ($88\%$) by more than margin $\delta = 2\%$.
**Solution**:
- $H_0: 	ext{Acc}_{mobile} \le 0.86$
- $H_a: 	ext{Acc}_{mobile} > 0.86$

## Example 3: ANOVA Multi-Model Comparison
**Problem**: Compare means of 4 hyperparameter configurations ($M_1, M_2, M_3, M_4$).
**Solution**:
- $H_0: \mu_1 = \mu_2 = \mu_3 = \mu_4$
- $H_a$: At least one model mean $\mu_i$ differs.

## Example 4: Regression Slope Significance
**Problem**: Test if feature weight $eta_1$ in $Y = eta_0 + eta_1 X$ is statistically significant.
**Solution**:
- $H_0: eta_1 = 0$
- $H_a: eta_1 
\neq 0$

## Example 5: Python Hypothesis Formulation Function
**Problem**: Write Python function to format hypotheses strings.
**Solution**:
```python
def format_hypotheses(metric_name, baseline_val, test_type='greater'):
  if test_type == 'greater':
    return f'H0: {metric_name} <= {baseline_val}', f'Ha: {metric_name} > {baseline_val}'
  elif test_type == 'less':
    return f'H0: {metric_name} >= {baseline_val}', f'Ha: {metric_name} < {baseline_val}'
  else:
    return f'H0: {metric_name} = {baseline_val}', f'Ha: {metric_name} != {baseline_val}'
```
