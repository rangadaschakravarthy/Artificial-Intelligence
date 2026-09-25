# Worked Examples — Type I and Type II Errors

## Example 1: Real-World Medical Diagnosis Errors
**Problem**: $H_0$: Patient is healthy. Identify Type I and Type II errors.
**Solution**:
- **Type I Error ($lpha$)**: Test says Patient has Disease, but patient is actually healthy (False Positive).
- **Type II Error ($eta$)**: Test says Patient is healthy, but patient actually has Disease (False Negative / Dangerous Miss!).

## Example 2: Spam Filter Errors
**Problem**: $H_0$: Email is Ham (legitimate). Identify Type I and Type II errors.
**Solution**:
- **Type I Error**: Flagging legitimate email as Spam (moves important email to Spam folder!).
- **Type II Error**: Letting Spam email into Inbox.

## Example 3: Computing Power from $eta$
**Problem**: An A/B test setup has Type II error rate $eta = 0.15$. Calculate Statistical Power.
**Solution**:
- $	ext{Power} = 1 - eta = 1 - 0.15 = 0.85 = 85\%$.

## Example 4: Sample Size for 80% Power
**Problem**: Calculate sample size needed in Python for $d=0.5, lpha=0.05, 	ext{power}=0.80$.
**Solution**:
```python
from statsmodels.stats.power import TTestIndPower

analysis = TTestIndPower()
n_per_group = analysis.solve_power(
    effect_size=0.5, alpha=0.05, power=0.80, ratio=1.0
)
# n_per_group approx 64 samples per group
```

## Example 5: $lpha$ vs $eta$ Trade-off
**Problem**: If you decrease $lpha$ from $0.05$ to $0.01$, what happens to Type II error $eta$ and Power $1-eta$?
**Solution**:
1. Decreasing $lpha$ moves critical value further out ($1.96 	o 2.58$), making $H_0$ harder to reject.
2. This increases Type II error $eta$ (more false negatives).
3. Statistical Power $1-eta$ DECREASES.
