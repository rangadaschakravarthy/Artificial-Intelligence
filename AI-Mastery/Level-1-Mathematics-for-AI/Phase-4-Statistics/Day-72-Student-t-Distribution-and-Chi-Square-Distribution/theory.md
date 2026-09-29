# Theory — Student's t-Distribution and Chi-Square Distribution

## 1. Simple Definition
- **Student's $t$-Distribution**: A symmetric bell-shaped continuous distribution with heavier tails than the Normal distribution, used for statistical inference on means when sample size $N$ is small and population variance $\sigma^2$ is unknown.
- **Chi-Square Distribution ($\chi^2_k$)**: A right-skewed continuous distribution representing the sum of $k$ squared independent standard normal variables, used for testing variances and categorical independence.

## 2. Intuition
- When population variance $\sigma$ is known, we use $Z$-scores.
- When population variance is unknown, we estimate it using sample variance $s$. Using $s$ introduces extra sampling uncertainty, widening the distribution tails. The $t$-distribution accounts for this extra uncertainty!

## 3. Mathematical Formulas
- **$t$-Statistic**:
  

$$
t = \frac{ar{X} - \mu}{s / \sqrt{N}} \sim t_{N-1}
$$

- **Student's $t$ PDF**:
  $$f(t; 
u) = \frac{\Gamma\left(\frac{
u+1}{2}
ight)}{\sqrt{
u \pi} \Gamma\left(\frac{
u}{2}
ight)} \left( 1 + \frac{t^2}{
u} 
ight)^{-\frac{
u+1}{2}}$$
  *(where $
u = df = N - 1$ degrees of freedom)*

- **Chi-Square Statistic**:
  

$$
\chi^2 = \sum_{i=1}^k \frac{(O_i - E_i)^2}{E_i} \sim \chi^2_{df}
$$

## 4. Degrees of Freedom ($df$)
Degrees of freedom represent the number of independent pieces of information available to estimate a parameter.
- For 1-Sample $t$-test: $df = N - 1$.
- For 2-Sample Independent $t$-test: $df = N_1 + N_2 - 2$.
- For Chi-Square Independence Test ($r 	imes c$ table): $df = (r - 1)(c - 1)$.

## 5. Summary
Use $Z$ when $\sigma$ is known or $N \ge 30$; use $t$ when $\sigma$ is unknown and $N < 30$. Use $\chi^2$ for independence testing and variance analysis.
