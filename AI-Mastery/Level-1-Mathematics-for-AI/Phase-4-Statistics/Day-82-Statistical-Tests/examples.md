# Worked Examples — Statistical Tests

## Example 1: 2-Sample Independent t-Test (Model A vs B)
**Problem**: Model A accuracy folds: mean $= 85\%, s = 3\%, n_1 = 10$. Model B: mean $= 89\%, s = 3\%, n_2 = 10$. Test if Model B is significantly better.
**Solution**:
1. Pooled $SE = \sqrt{rac{9}{10} + rac{9}{10}} = \sqrt{1.8} pprox 1.3416\%$.
2. $t = rac{89 - 85}{1.3416} = rac{4}{1.3416} = 2.9815$.
3. $df = 10 + 10 - 2 = 18$. $t_{crit, 0.05} = 1.734$ (1-tailed).
4. Since $t = 2.9815 > 1.734$, Reject $H_0$. Model B is significantly better!

## Example 2: Paired t-Test (Pre vs Post Optimization)
**Problem**: 5 query latency pairs before/after cache optimization: Differences $d = [10, 12, 8, 15, 5]$ ms. Compute $t$-stat.
**Solution**:
1. Mean difference $ar{d} = rac{10+12+8+15+5}{5} = rac{50}{5} = 10.0$ ms.
2. Sample std dev of differences $s_d = 3.8079$.
3. $SE = rac{3.8079}{\sqrt{5}} = 1.7029$.
4. $t = rac{10.0}{1.7029} = 5.8723$ ($df = 4$). $p = 0.0042 < 0.05 \implies$ Significant latency reduction!

## Example 3: Chi-Square Test of Independence
**Problem**: $2 	imes 2$ table of User Device vs Click: Observed $O = [[40, 60], [60, 40]]$. Compute $\chi^2$.
**Solution**:
1. Row totals: 100, 100. Col totals: 100, 100. Total $N = 200$.
2. Expected counts $E_{ij} = 50$ for all cells.
3. $\chi^2 = \sum rac{(O - 50)^2}{50} = rac{(-10)^2 + 10^2 + 10^2 + (-10)^2}{50} = rac{400}{50} = 8.0$.
4. $df = (2-1)(2-1) = 1$. $\chi^2_{crit} = 3.841$.
5. Since $8.0 > 3.841$, Reject $H_0$ (Device and Click are dependent!).

## Example 4: Choosing Between Independent and Paired t-Test
**Problem**: 1) Comparing test accuracies of 2 models evaluated on identical test images. 2) Comparing test accuracies of 2 models trained and tested on separate random user cohorts.
**Solution**:
1. Paired t-test (`ttest_rel`).
2. 2-Sample Independent t-test (`ttest_ind`).

## Example 5: SciPy Statistical Test Suite Executions
**Problem**: Run statistical tests in Python.
**Solution**:
```python
from scipy import stats

t_ind, p_ind = stats.ttest_ind(group1, group2, equal_var=False)  # Welch's t-test
t_rel, p_rel = stats.ttest_rel(before, after)  # Paired t-test
chi2, p_chi2, dof, _ = stats.chi2_contingency(table)  # Chi-Square
```
