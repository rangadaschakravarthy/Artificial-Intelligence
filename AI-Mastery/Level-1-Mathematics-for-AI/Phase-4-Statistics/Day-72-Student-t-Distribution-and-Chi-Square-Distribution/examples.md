# Worked Examples — Student's t-Distribution and Chi-Square Distribution

## Example 1: t-Statistic Calculation
**Problem**: Sample size $N = 16$ ($df = 15$), sample mean $ar{x} = 54$, sample $s = 8$. Test $H_0: \mu = 50$. Compute $t$-score.
**Solution**:
1. Standard Error $SE = rac{s}{\sqrt{N}} = rac{8}{\sqrt{16}} = rac{8}{4} = 2.0$.
2. $t = rac{ar{x} - \mu_0}{SE} = rac{54 - 50}{2.0} = rac{4}{2.0} = +2.0$.
3. $t$-score is $+2.0$ with $df = 15$.

## Example 2: t Critical Value Lookup
**Problem**: Find 2-tailed critical $t$-value for $df = 15$ at significance level $lpha = 0.05$.
**Solution**:
1. Tail probability $lpha/2 = 0.025$ in upper tail.
2. Using SciPy `stats.t.ppf(0.975, df=15)` $pprox 2.1315$.
3. Critical region is $|t| > 2.1315$.
4. (From Example 1, $t = 2.0 < 2.1315$, so fail to reject $H_0$).

## Example 3: Chi-Square Goodness-of-Fit Statistic
**Problem**: Observed dice roll counts for 60 rolls: $O = [15, 7, 12, 8, 11, 7]$. Expected counts for fair die: $E_i = 10$. Compute $\chi^2$ statistic.
**Solution**:
1. $\chi^2 = \sum rac{(O_i - E_i)^2}{E_i}$.
2. $= rac{(15-10)^2}{10} + rac{(7-10)^2}{10} + rac{(12-10)^2}{10} + rac{(8-10)^2}{10} + rac{(11-10)^2}{10} + rac{(7-10)^2}{10}$.
3. $= rac{25 + 9 + 4 + 4 + 1 + 9}{10} = rac{52}{10} = 5.20$.
4. $df = 6 - 1 = 5$.

## Example 4: Chi-Square Critical Value Lookup
**Problem**: Find critical value for $\chi^2$ test with $df = 5$ at $lpha = 0.05$.
**Solution**:
1. Using SciPy `stats.chi2.ppf(0.95, df=5)` $pprox 11.0705$.
2. Since observed $\chi^2 = 5.20 < 11.0705$, fail to reject $H_0$ (die is fair).

## Example 5: SciPy t and Chi-Square Probability Evaluation
**Problem**: Evaluate $p$-values in Python.
**Solution**:
```python
from scipy import stats

p_val_t = 2 * (1 - stats.t.cdf(2.0, df=15))  # p = 0.0639
p_val_chi2 = 1 - stats.chi2.cdf(5.20, df=5)  # p = 0.3920
```
