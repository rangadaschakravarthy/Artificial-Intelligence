# Day 167 Theory: Correlation-Based Selection

### 1. What Is It?
Correlation-Based Selection is a Filter feature selection technique that drops redundant features highly correlated with each other while retaining features strongly correlated with the target variable.

### 2. Multi-Collinearity Problem
If two features $X_1$ and $X_2$ have correlation $|r| pprox 1.0$, they convey identical information. Retaining both inflates model variance and makes coefficient estimates unstable in linear models.

### 3. Syntax (Automated Upper-Triangle Pruning)
```python
corr_matrix = X.corr().abs()
upper = corr_matrix.where(np.triu(np.ones(corr_matrix.shape), k=1).astype(bool))
to_drop = [column for column in upper.columns if any(upper[column] > 0.85)]
X_selected = X.drop(columns=to_drop)
```

### 4. Summary
Dropping 1 feature from highly collinear pairs ($|r| > 0.85$) removes redundancy without information loss.
