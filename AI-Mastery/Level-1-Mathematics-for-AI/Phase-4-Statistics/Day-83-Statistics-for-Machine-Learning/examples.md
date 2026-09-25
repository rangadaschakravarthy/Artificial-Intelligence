# Worked Examples — Statistics for Machine Learning

## Example 1: ANOVA F-Test Feature Ranking
**Problem**: Feature 1 has $F = 45.2, p = 0.0001$. Feature 2 has $F = 0.8, p = 0.4500$. Which feature should be selected?
**Solution**:
- Feature 1 has a high $F$-score and $p < 0.05$. Select Feature 1; drop Feature 2.

## Example 2: Bonferroni Adjustment
**Problem**: Evaluating $m = 50$ candidate features at overall family-wise $lpha = 0.05$. What is the adjusted single-feature $p$-value threshold?
**Solution**:
- $lpha_{	ext{adj}} = rac{0.05}{50} = 0.001$.
- Only features with $p \le 0.001$ are selected.

## Example 3: Scikit-Learn SelectKBest ANOVA
**Problem**: Select top 2 features using Scikit-Learn.
**Solution**:
```python
from sklearn.feature_selection import SelectKBest, f_classif

selector = SelectKBest(score_func=f_classif, k=2)
X_selected = selector.fit_transform(X, y)
```

## Example 4: A/B Test Absolute & Relative Lift
**Problem**: Baseline CTR $p_A = 0.05$. Variant B CTR $p_B = 0.06$. Compute absolute and relative lift.
**Solution**:
1. Absolute Lift $= p_B - p_A = 0.06 - 0.05 = +0.01 = +1.0\%$ absolute.
2. Relative Lift $= rac{p_B - p_A}{p_A} = rac{0.01}{0.05} = +0.20 = +20.0\%$ relative lift.

## Example 5: Data Drift Detection via KS-Test
**Problem**: Run 2-sample KS test on production feature values vs training feature values.
**Solution**:
```python
from scipy import stats

ks_stat, p_val = stats.ks_2samp(train_feature, prod_feature)
if p_val < 0.05:
  print("Data Drift Detected! Trigger Model Retraining.")
```
