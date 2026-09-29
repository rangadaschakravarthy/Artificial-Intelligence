# Worked Examples — Introduction to Hypothesis Testing

## Example 1: Formulating Hypotheses for Model Accuracy Lift
**Problem**: An engineer tests a new model architecture hoping to improve baseline accuracy beyond $85\%$. Formulate $H_0$ and $H_a$.
**Solution**:
- Null Hypothesis $H_0: \mu \le 0.85$ (No improvement over baseline status quo).
- Alternative Hypothesis $H_a: \mu > 0.85$ (New model improves accuracy).
- Type of test: One-Tailed Right test.

## Example 2: Formulating Hypotheses for Latency Shift
**Problem**: Test whether a code refactor changed latency from baseline 50 ms. Formulate $H_0$ and $H_a$.
**Solution**:
- $H_0: \mu = 50$ ms.
- $H_a: \mu 
\neq 50$ ms.
- Type of test: Two-Tailed test.

## Example 3: Two-Tailed Z Critical Values
**Problem**: For $lpha = 0.05$ in a 2-tailed Z-test, find critical region boundaries.
**Solution**:
1. Tail probability $lpha / 2 = 0.025$.
2. $Z_{crit} = \pm 1.960$.
3. Rejection region: $Z < -1.960$ or $Z > +1.960$.

## Example 4: One-Tailed Z Critical Value
**Problem**: For $lpha = 0.05$ in a 1-tailed Right Z-test ($H_a: \mu > \mu_0$), find critical value.
**Solution**:
1. Upper tail area $= 0.05$.
2. $Z_{crit} = +1.645$.
3. Rejection region: $Z > +1.645$.

## Example 5: Decision Rule Application
**Problem**: Computed test statistic $Z = +2.15$. Test is 2-tailed at $lpha = 0.05$ ($Z_{crit} = \pm 1.96$). Make decision.
**Solution**:
1. Since $Z = 2.15 > 1.96$, $Z$ falls inside the rejection region.
2. Decision: Reject $H_0$. Conclusion: Result is statistically significant.
