# Day 171 Worked Examples: Preprocessing for Machine Learning

## Example 1 — Practical: Model-Specific Preprocessing Dual Pipeline
```python
import pandas as pd
from sklearn.preprocessing import StandardScaler, OrdinalEncoder, OneHotEncoder

df = pd.DataFrame({
    'Age': [25, 45, 35],
    'Tier': ['Low', 'High', 'Medium'],
    'Spend': [1000, 5000, 2500]
})

# Pipeline A: For Linear / SVM Models (Requires Scaling & One-Hot)
X_linear = pd.get_dummies(df, columns=['Tier'], drop_first=True, dtype=float)
scaler = StandardScaler()
X_linear[['Age', 'Spend']] = scaler.fit_transform(X_linear[['Age', 'Spend']])

# Pipeline B: For Tree Models (Unscaled & Ordinal Encoded)
oe = OrdinalEncoder(categories=[['Low', 'Medium', 'High']])
X_tree = df.copy()
X_tree['Tier_Code'] = oe.fit_transform(X_tree[['Tier']])
X_tree.drop(columns=['Tier'], inplace=True)

print("Linear Model Input Matrix X:
", X_linear.round(2))
print("
Tree Model Input Matrix X:
", X_tree)
```
