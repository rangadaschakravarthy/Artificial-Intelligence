# Day 158 Theory: One-Hot Encoding

### 1. What Is It?
One-Hot Encoding converts a nominal categorical feature with $K$ unique categories into $K$ binary indicator columns ($0$ or $1$), where exactly one column is "hot" ($1$) for each observation.

### 2. Dummy Variable Trap
If $K$ binary columns are created for $K$ categories, their row sum equals $1$ ($\sum_{j=1}^K x_{ij} = 1$), creating perfect linear dependency (multi-collinearity) with the intercept vector. Dropping 1 category column ($K-1$ columns) resolves multi-collinearity.

### 3. Syntax
```python
# Pandas:
df_ohe = pd.get_dummies(df, columns=['Color'], drop_first=True, dtype=int)

# Scikit-Learn:
from sklearn.preprocessing import OneHotEncoder
ohe = OneHotEncoder(drop='first', sparse_output=False, handle_unknown='ignore')
X_ohe = ohe.fit_transform(df[['Color']])
```

### 4. Summary
One-Hot Encoding represents nominal categories as orthogonal binary vectors without introducing false magnitude ordering.
