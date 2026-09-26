# Day 169 Theory: Train-Test Concept

### 1. What Is It?
The Train-Test concept partitions a dataset into independent sub-samples: a Training set used to learn model parameters, and an unseen Test set used to evaluate generalization performance.

### 2. Stratified Splitting
In imbalanced classification (e.g. 95% Non-Churn, 5% Churn), random splitting can yield test sets with 0% churn rows. `stratify=y` ensures train and test splits maintain identical class proportions.

### 3. Syntax
```python
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.20,
    random_state=42,
    stratify=y
)
```

### 4. Summary
`train_test_split()` isolates unseen data, while `stratify=y` preserves target class distributions across splits.
