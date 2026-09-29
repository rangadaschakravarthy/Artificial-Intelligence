# Theory — Null and Alternative Hypotheses

## 1. Simple Definition
- **Null Hypothesis ($H_0$)**: The default claim that there is no effect, no difference, or no improvement. Always contains an equality operator ($=, \le, \ge$).
- **Alternative Hypothesis ($H_a$)**: The research claim that there is a real effect, difference, or improvement. Contains strict inequality operators ($
\neq, >, <$).

## 2. Operator Rules Table

| Test Type | Null Hypothesis $H_0$ | Alternative Hypothesis $H_a$ | Tail Type |
| :--- | :--- | :--- | :--- |
| **Two-Tailed** | $H_0: \mu = \mu_0$ | $H_a: \mu 
\neq \mu_0$ | Two-Tailed |
| **One-Tailed Right** | $H_0: \mu \le \mu_0$ | $H_a: \mu > \mu_0$ | Upper Tail |
| **One-Tailed Left** | $H_0: \mu \ge \mu_0$ | $H_a: \mu < \mu_0$ | Lower Tail |

## 3. Real-World AI Scenarios
1. **A/B Testing Conversion Lift**:
   - $H_0: p_B - p_A \le 0$ (Variant B does not increase conversions).
   - $H_a: p_B - p_A > 0$ (Variant B increases conversions).
2. **Model Accuracy Comparison**:
   - $H_0: 	ext{Acc}_B - 	ext{Acc}_A = 0$ (No difference in accuracy).
   - $H_a: 	ext{Acc}_B - 	ext{Acc}_A 
\neq 0$ (Accuracies differ).
3. **Feature Selection Correlation**:
   - $H_0: 
ho_{X,Y} = 0$ (Feature $X$ has no linear relationship with target $Y$).
   - $H_a: 
ho_{X,Y} 
\neq 0$ (Feature $X$ is correlated with target $Y$).

## 4. Summary
$H_0$ is the status quo containing equality; $H_a$ is the research claim containing inequality.
