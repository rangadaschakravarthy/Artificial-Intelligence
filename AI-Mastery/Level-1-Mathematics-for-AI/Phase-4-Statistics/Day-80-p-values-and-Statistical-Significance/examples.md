# Worked Examples — p-values and Statistical Significance

## Example 1: 2-Tailed Z-Test p-value Calculation
**Problem**: Calculated test statistic $Z = +2.10$. Compute 2-tailed $p$-value.
**Solution**:
1. Single upper tail area: $1 - \Phi(2.10) = 1 - 0.9821 = 0.0179$.
2. For 2-tailed test, double single tail area: $p = 2 	imes 0.0179 = 0.0358$.
3. Since $p = 0.0358 \le 0.05$, Reject $H_0$.

## Example 2: 1-Tailed Right Z-Test p-value
**Problem**: Calculated $Z = +1.80$ for 1-tailed Right test ($H_a: \mu > \mu_0$). Compute $p$-value.
**Solution**:
1. Upper tail area: $p = 1 - \Phi(1.80) = 1 - 0.9641 = 0.0359$.
2. $p = 0.0359 \le 0.05 \implies$ Reject $H_0$.

## Example 3: Large Sample Size p-value Trap
**Problem**: A dataset of $N = 1,000,000$ users shows Model B accuracy $= 85.01\%$ vs Model A $= 85.00\%$. $p$-value is $0.0001$. Evaluate result.
**Solution**:
1. Statistically Significant ($p = 0.0001 < 0.05$).
2. Practically Insignificant (Effect size lift is only $+0.01\%$, which does not justify model deployment costs!).

## Example 4: Cohen's d Effect Size Calculation
**Problem**: Model A mean $= 80\%$, Model B mean $= 85\%$, pooled std dev $s_{pooled} = 10\%$. Compute Cohen's $d$.
**Solution**:
1. $d = \frac{ar{x}_B - ar{x}_A}{s_{pooled}} = \frac{85 - 80}{10} = \frac{5}{10} = 0.50$ (Medium effect size).

## Example 5: SciPy p-value Calculation
**Problem**: Compute $p$-values in Python using SciPy.
**Solution**:
```python
from scipy import stats

z_stat = 2.10
p_val_2tail = 2 * (1 - stats.norm.cdf(abs(z_stat)))  # 0.0357
```
