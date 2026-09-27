# Machine Learning Evaluation Metrics Reference

## 1. Regression Metrics

| Metric | Formula | Range | Best Value | Sensitivity to Outliers | Primary Use Case |
| ------ | ------- | ----- | ---------- | ----------------------- | ---------------- |
| **MAE** | $\frac{1}{n} \sum \|y_i - \hat{y}_i\|$ | $[0, \infty)$ | $0.0$ | Low | Linear interpretation in target units |
| **MSE** | $\frac{1}{n} \sum (y_i - \hat{y}_i)^2$ | $[0, \infty)$ | $0.0$ | **High** | Optimization loss functions (differentiable) |
| **RMSE** | $\sqrt{\text{MSE}}$ | $[0, \infty)$ | $0.0$ | **High** | Standard error metric in target units |
| **$R^2$** | $1 - \frac{\text{SS}_{\text{res}}}{\text{SS}_{\text{tot}}}$ | $(-\infty, 1.0]$ | $1.0$ | Medium | Explains proportion of variance captured |

---

## 2. Classification Metrics

| Metric | Formula | Range | Best Value | When Useful | When Misleading |
| ------ | ------- | ----- | ---------- | ----------- | --------------- |
| **Accuracy** | $\frac{TP + TN}{TP + TN + FP + FN}$ | $[0, 1.0]$ | $1.0$ | Balanced class distributions | **Severely misleading on imbalanced datasets** |
| **Precision** | $\frac{TP}{TP + FP}$ | $[0, 1.0]$ | $1.0$ | High cost of False Positives (e.g., Spam filter) | Ignores False Negatives |
| **Recall** | $\frac{TP}{TP + FN}$ | $[0, 1.0]$ | $1.0$ | High cost of False Negatives (e.g., Cancer detection) | Ignores False Positives |
| **F1-Score** | $2 \times \frac{\text{Precision} \times \text{Recall}}{\text{Precision} + \text{Recall}}$ | $[0, 1.0]$ | $1.0$ | Imbalanced classes needing precision/recall balance | When one error type is vastly more critical |
| **ROC-AUC** | Area under TPR vs FPR curve | $[0, 1.0]$ | $1.0$ | General ranking capability across all thresholds | Can look overly optimistic on extreme imbalance |
| **PR-AUC** | Area under Precision vs Recall curve | $[0, 1.0]$ | $1.0$ | **Extreme class imbalance** (e.g. Fraud 0.1%) | Baseline equals positive class ratio |

---

## 3. Clustering Metrics

| Metric | Formula / Principle | Range | Best Value | Interpretation |
| ------ | ------------------- | ----- | ---------- | -------------- |
| **Inertia (WCSS)** | $\sum_{k=1}^K \sum_{x \in C_k} \|x - \mu_k\|^2$ | $[0, \infty)$ | Lower is better | Measures internal cluster compactness |
| **Silhouette Score** | $s(i) = \frac{b(i) - a(i)}{\max(a(i), b(i))}$ | $[-1.0, +1.0]$ | $+1.0$ | $+1$: well separated, $0$: overlapping, $-1$: misclustered |
