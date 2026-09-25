# Theory — Type I and Type II Errors

## 1. Simple Definition
- **Type I Error ($lpha$)**: Rejecting Null Hypothesis $H_0$ when $H_0$ is actually TRUE (False Positive / False Alarm).
- **Type II Error ($eta$)**: Failing to reject Null Hypothesis $H_0$ when $H_0$ is actually FALSE (False Negative / Missed Discovery).
- **Statistical Power ($1 - eta$)**: Probability of correctly rejecting $H_0$ when a true effect exists.

## 2. Hypothesis Testing Decision Matrix

| Reality \ Decision | Fail to Reject $H_0$ | Reject $H_0$ |
| :--- | :--- | :--- |
| **$H_0$ is True** | Correct Decision ($1 - lpha$) | **Type I Error ($lpha$)** (False Positive) |
| **$H_0$ is False** | **Type II Error ($eta$)** (False Negative) | Correct Decision (**Power $1 - eta$**) |

## 3. Four Factors Affecting Statistical Power ($1 - eta$)
1. **Sample Size ($n$)**: Larger $n \implies$ Higher Power.
2. **Effect Size ($d$)**: Larger effect $\implies$ Higher Power.
3. **Significance Level ($lpha$)**: Larger $lpha$ (e.g. $0.05$ vs $0.01$) $\implies$ Higher Power (trades off more Type I errors).
4. **Variability ($\sigma$)**: Lower variance $\implies$ Higher Power.

## 4. Power Analysis Target Standard
In AI and A/B testing, standard target power is **$80\%$ ($1 - eta = 0.80 \implies eta = 0.20$)** at $lpha = 0.05$.

## 5. Summary
Type I error $lpha$ is False Alarm; Type II error $eta$ is Missed Discovery; Power $1-eta \ge 0.80$ guarantees sufficient sample size to detect real effects.
