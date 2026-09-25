# Theory — p-values and Statistical Significance

## 1. Simple Definition
A **$p$-value** is the probability of obtaining a test statistic as extreme as, or more extreme than, the one observed in sample data, **assuming the Null Hypothesis ($H_0$) is true**.

## 2. Intuition
Imagine flipping a coin 10 times to test if it's fair ($H_0: p = 0.5$). You get 10 Heads in a row.
If the coin WAS fair ($H_0$ true), the chance of getting 10 Heads by luck is $P = (0.5)^{10} = 0.000976$ ($p$-value $= 0.000976$).
Because this $p$-value is extremely small ($< 0.05$), you conclude the coin is biased ($H_a$).

## 3. Decision Rule
- If **$p \le lpha$**: Reject $H_0$ $\implies$ Result is **Statistically Significant**.
- If **$p > lpha$**: Fail to Reject $H_0$ $\implies$ Result is **Not Statistically Significant**.

## 4. CRITICAL $p$-value Misconceptions

| Misconception | Correction |
| :--- | :--- |
| "$p$-value is the probability that $H_0$ is true." | **FALSE!** $p$-value is $P(	ext{Data} \mid H_0)$, NOT $P(H_0 \mid 	ext{Data})$. |
| "$p = 0.01$ means the treatment has a large effect." | **FALSE!** $p$-value measures statistical certainty, NOT effect magnitude. With large $n$, tiny useless effects yield tiny $p$-values. |
| "$p > 0.05$ proves $H_0$ is true." | **FALSE!** It only means the sample size was insufficient to detect a difference. |

## 5. Statistical Significance vs Practical Significance (Effect Size)
- **Statistical Significance ($p$-value)**: Tells you IF an effect exists.
- **Practical Significance (Effect Size, e.g. Cohen's $d$)**: Tells you HOW LARGE and meaningful the effect is in the real world.

## 6. Summary
$p$-values measure data compatibility with $H_0$; $p \le lpha$ rejects $H_0$. Always pair $p$-values with Effect Size.
