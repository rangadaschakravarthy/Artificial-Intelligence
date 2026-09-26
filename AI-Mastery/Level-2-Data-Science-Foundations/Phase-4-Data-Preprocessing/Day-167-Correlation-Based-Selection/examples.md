# Day 167 Worked Examples: Correlation-Based Selection

## Example 1 — Practical: Automated Upper-Triangle Correlation Pruner
```python
import pandas as pd
import numpy as np

np.random.seed(42)
f1 = np.random.randn(100)
f2 = f1 * 0.95 + np.random.randn(100) * 0.05 # Highly correlated with f1
f3 = np.random.randn(100)

df = pd.DataFrame({'F1': f1, 'F2': f2, 'F3': f3})

# Compute absolute correlation matrix
corr_matrix = df.corr().abs()
upper = corr_matrix.where(np.triu(np.ones(corr_matrix.shape), k=1).astype(bool))
to_drop = [col for col in upper.columns if any(upper[col] > 0.85)]

df_pruned = df.drop(columns=to_drop)
print("Dropped Redundant Features:", to_drop)
print("Pruned Feature Set Columns:", list(df_pruned.columns))
```
