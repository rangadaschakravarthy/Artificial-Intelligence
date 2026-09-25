# Worked Examples — Statistical Distributions in Statistics

## Example 1: Shapiro-Wilk Normality Test
**Problem**: A sample dataset of 50 model error residuals yields Shapiro-Wilk test statistic $W = 0.985$ with $p$-value $= 0.75$. Interpret result at $lpha = 0.05$.
**Solution**:
1. Null Hypothesis $H_0$: Data is Normally distributed.
2. Since $p$-value $= 0.75 > 0.05$, we fail to reject $H_0$.
3. Data residuals satisfy the Normality assumption; parametric statistical tests are valid.

## Example 2: Distribution Selection for Counts
**Problem**: Select appropriate distribution for modeling the number of customer support tickets received per hour ($x \in \{0, 1, 2, \dots\}$).
**Solution**:
- Count data occurring over fixed time intervals $\implies$ **Poisson Distribution**.

## Example 3: Parametric vs Non-Parametric Selection
**Problem**: User reaction times are heavily right-skewed with extreme outliers. Choose test to compare two groups.
**Solution**:
- Since data is heavily skewed and violates Normality, choose non-parametric **Mann-Whitney U test** rather than two-sample t-test.

## Example 4: Chi-Square Distribution Construction
**Problem**: If $Z_1, Z_2, Z_3 \stackrel{iid}{\sim} \mathcal{N}(0, 1)$, what distribution does $Q = Z_1^2 + Z_2^2 + Z_3^2$ follow?
**Solution**:
- Sum of 3 squared independent standard normal variables follows a **Chi-Square distribution with $df = 3$ degrees of freedom** ($Q \sim \chi^2_3$).

## Example 5: SciPy Normality Testing
**Problem**: Test dataset normality in Python.
**Solution**:
```python
from scipy import stats

data = stats.norm.rvs(size=100)
stat, p_val = stats.shapiro(data)
# p_val > 0.05 confirms normality
```
