# Worked Examples — Statistics AI Mini-Project

## Example 1: Automated Test Selection (Normal Data, Equal Variance)
- Group A: Normal, $s_A^2 = 4.0$. Group B: Normal, $s_B^2 = 4.2$. Levene $p = 0.82 > 0.05$.
- Selected Test: **Student's Independent 2-Sample t-Test**.

## Example 2: Automated Test Selection (Normal Data, Unequal Variance)
- Group A: Normal, $s_A^2 = 4.0$. Group B: Normal, $s_B^2 = 25.0$. Levene $p = 0.001 < 0.05$.
- Selected Test: **Welch's 2-Sample t-Test**.

## Example 3: Automated Test Selection (Non-Normal Skewed Data)
- Group A: Exponentially distributed ($p_{shapiro} = 0.001$). Group B: Normal.
- Selected Test: **Mann-Whitney U Test** (Non-parametric).

## Example 4: Executive Report Generation
- Metric: Conversion Rate. Variant A $= 10.0\%$, Variant B $= 12.5\%$.
- $p$-value $= 0.012 < 0.05$. Cohen's $d = 0.35$.
- Result: **STATISTICALLY SIGNIFICANT LIFT APPROVED FOR DEPLOYMENT**.
