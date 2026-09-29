# Theory — Introduction to Hypothesis Testing

## 1. Simple Definition
Hypothesis testing is a formal statistical procedure for using sample data to evaluate the validity of a claim or hypothesis about a population parameter.

## 2. The 5-Step Hypothesis Testing Framework
1. **State Hypotheses**: Formulate Null Hypothesis $H_0$ and Alternative Hypothesis $H_a$.
2. **Set Significance Level $lpha$**: Choose risk threshold (typically $lpha = 0.05$ or $5\%$).
3. **Select & Compute Test Statistic**: Calculate $Z$-score, $t$-score, or $\chi^2$ from sample data.
4. **Determine $p$-value or Critical Region**: Compare test statistic against critical values $Z_{crit}, t_{crit}$.
5. **Make Decision & Draw Conclusion**:
   - If $p \le lpha$ (or test stat in critical region) $\implies$ **Reject $H_0$** (Statistically Significant!).
   - If $p > lpha \implies$ **Fail to Reject $H_0$** (Inconclusive / No significant difference).

## 3. One-Tailed vs Two-Tailed Tests
- **Two-Tailed Test** ($H_a: \mu 
\neq \mu_0$): Tests for difference in EITHER direction (increase or decrease). Split $lpha/2$ in both tails.
- **One-Tailed Test Right** ($H_a: \mu > \mu_0$): Tests specifically for an INCREASE. Entire $lpha$ in upper tail.
- **One-Tailed Test Left** ($H_a: \mu < \mu_0$): Tests specifically for a DECREASE. Entire $lpha$ in lower tail.

## 4. Summary
Hypothesis testing structures statistical proof into a 5-step pipeline: state hypotheses, set $lpha$, calculate test statistic, compute $p$-value, and decide.
