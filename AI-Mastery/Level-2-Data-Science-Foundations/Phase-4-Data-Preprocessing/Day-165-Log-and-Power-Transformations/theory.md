# Day 165 Theory: Log and Power Transformations

### 1. What Is It?
Log and Power Transformations apply non-linear mathematical operations to stabilize variance and convert right-skewed continuous variables into Gaussian bell curves.

### 2. Formulas
- **Log1p**: $f(x) = \ln(1 + x)$ (safe for $x \ge 0$).
- **Box-Cox**:
  $$y^{(\lambda)} = egin{cases} rac{x^\lambda - 1}{\lambda} & 	ext{if } \lambda 
eq 0 \ \ln(x) & 	ext{if } \lambda = 0 \end{cases} \quad (x > 0)$$
- **Yeo-Johnson**: Extends Box-Cox to handle negative values and zeros ($x \le 0$).

### 3. Syntax
```python
# Log1p:
df['Income_Log'] = np.log1p(df['Income'])

# Yeo-Johnson PowerTransformer:
from sklearn.preprocessing import PowerTransformer
pt = PowerTransformer(method='yeo-johnson')
df['Income_PT'] = pt.fit_transform(df[['Income']])
```

### 4. Summary
Log1p compresses right-skewed tails, while Yeo-Johnson automatically optimizes power parameters for positive and negative values.
