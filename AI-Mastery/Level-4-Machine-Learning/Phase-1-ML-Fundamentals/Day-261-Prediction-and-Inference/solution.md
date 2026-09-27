# Practice Solutions — Day 261

## Basic Solutions
1. Prediction & Inference establishes the structured definitions and data matrices for training ML algorithms.
2. $n$ is the total number of observations (rows); $d$ is the number of measured attributes per observation (columns).
3. It denotes a real-valued matrix with $n$ rows and $d$ columns.

## Conceptual Solutions
4. Data leakage occurs when information from the test/validation set contaminates the training set, giving falsely optimistic test metrics.
5. High model capacity can memorize training noise (overfitting); low model capacity cannot capture underlying patterns (underfitting).
6. Parameters are learned automatically from training data; hyperparameters are set manually before training begins.

## Calculation Solutions
7. $n = 500$ samples, $d = 20$ features.
8. Errors squared: $(2-2.5)^2 = 0.25$, $(4-3.5)^2 = 0.25$, $(6-6.5)^2 = 0.25$. MSE = $(0.25+0.25+0.25)/3 = 0.25$.

## Implementation Solutions
```python
import numpy as np
from sklearn.model_selection import train_test_split

# 9. Random Matrix
X = np.random.randn(100, 5)
y = np.random.randint(0, 2, size=100)

# 10. Stratified Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, stratify=y, random_state=42)
print("Train shape:", X_train.shape, "Test shape:", X_test.shape)
```

## ML Reasoning Solutions
11. The model is severely overfitting (high variance). It memorized training data but failed to generalize.
12. Use a validation set for hyperparameter tuning and model selection, reserving the test set exclusively for final unbiased evaluation.

## Dataset Questions
13. Feature matrix $X$: shape $(1000, 14)$. Target vector $y$: shape $(1000,)$.

## Interview Solutions
14. Bias is the error from overly simple assumptions; Variance is sensitivity to small fluctuations in training data. Optimal ML finds the sweet spot minimizing both.
15. Problem framing -> Data collection -> EDA -> Preprocessing -> Model training -> Validation -> Tuning -> Evaluation -> Deployment -> Monitoring.
