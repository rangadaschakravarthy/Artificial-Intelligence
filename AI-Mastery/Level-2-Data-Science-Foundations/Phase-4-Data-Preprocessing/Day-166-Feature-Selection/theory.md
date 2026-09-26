# Day 166 Theory: Feature Selection

### 1. What Is It?
Feature Selection is the process of selecting a subset of relevant features for use in model construction, eliminating redundant, uninformative, or noisy variables.

### 2. Three Main Categories
1. **Filter Methods**: Evaluate features independently using statistical metrics (Correlation, Variance, Chi-Square, ANOVA $F$-test) before model training.
2. **Wrapper Methods**: Evaluate feature subsets by iteratively training a specific ML model (Recursive Feature Elimination - RFE, Forward/Backward Selection).
3. **Embedded Methods**: Perform feature selection inherently during model training (Lasso L1 regularization, Tree Feature Importance).

### 3. Syntax (VarianceThreshold)
```python
from sklearn.feature_selection import VarianceThreshold

selector = VarianceThreshold(threshold=0.01) # Drops features with variance < 0.01
X_high_var = selector.fit_transform(X)
```

### 4. Summary
Feature selection reduces model complexity, prevents overfitting, and accelerates computation by discarding uninformative features.
