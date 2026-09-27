# Practice Solutions — Day 278

## Basic Solutions
1. Classification maps feature inputs $X$ to discrete class labels $y \in \{1, \dots, K\}$.
2. Confusion Matrix components: True Positives (TP), True Negatives (TN), False Positives (FP), False Negatives (FN).
3. $\text{Precision} = \frac{TP}{TP+FP}$, $\text{Recall} = \frac{TP}{TP+FN}$, $\text{F1} = \frac{2 \cdot \text{Precision} \cdot \text{Recall}}{\text{Precision} + \text{Recall}}$.

## Conceptual Solutions
4. A dummy model predicting 0 for all instances achieves 99.9% accuracy while detecting 0 fraud cases (0% recall).
5. Sigmoid maps any real-valued number $z \in (-\infty, \infty)$ to a valid probability range $(0, 1)$.
6. Decision Trees have high variance and overfit easily; Random Forests average multiple de-correlated trees, significantly reducing variance.

## Calculation Solutions
7. $\text{Accuracy} = \frac{40+50}{100} = 0.90$. $\text{Precision} = \frac{40}{40+10} = 0.80$. $\text{Recall} = \frac{40}{40+0} = 1.00$. $\text{F1} = 2 \frac{0.8 \times 1.0}{0.8 + 1.0} = \frac{1.6}{1.8} = 0.889$.
8. $\text{Entropy} = -\left[0.5 \log_2(0.5) + 0.5 \log_2(0.5)\right] = -[0.5(-1) + 0.5(-1)] = 1.0$ bit.

## Implementation Solutions
```python
import numpy as np
from sklearn.ensemble import RandomForestClassifier

# 9. Sigmoid
def sigmoid(z):
    return 1.0 / (1.0 + np.exp(-z))

# 10. Random Forest
X = np.random.randn(100, 4)
y = np.random.randint(0, 2, 100)
rf = RandomForestClassifier(n_estimators=50, random_state=42).fit(X, y)
print("Feature Importances:", rf.feature_importances_)
```

## ML Reasoning Solutions
11. Optimize for Recall. A False Negative (missing cancer) is fatal, whereas a False Positive can be caught with follow-up testing.
12. Reduce `max_depth`, increase `min_samples_split`, or decrease `max_features` to prune the tree and reduce overfitting.

## Dataset Questions
13. Class distribution: count occurrences of each unique target label in $y$ divided by $n$.

## Interview Solutions
14. Derivation: $\sigma'(z) = \frac{d}{dz}(1 + e^{-z})^{-1} = -(1 + e^{-z})^{-2}(-e^{-z}) = \frac{e^{-z}}{(1 + e^{-z})^2} = \frac{1}{1 + e^{-z}} \cdot \frac{e^{-z}}{1 + e^{-z}} = \sigma(z)(1 - \sigma(z))$.
15. Kernel function $K(\mathbf{x}_i, \mathbf{x}_j) = \langle \Phi(\mathbf{x}_i), \Phi(\mathbf{x}_j) \rangle$ computes inner products in Hilbert feature space directly without ever calculating high-dimensional transformation $\Phi(\mathbf{x})$ explicitly.
