# Day 157 Theory: Label Encoding

### 1. What Is It?
Label Encoding assigns a unique sequential integer ($0, 1, 2, \dots, K-1$) to each distinct categorical level in a variable.

### 2. When to Use
- **Ordinal Variables**: Categories possess an intrinsic ranking (`'Small' < 'Medium' < 'Large'`).
- **Tree-Based Models**: Random Forests and XGBoost handle integer-encoded categorical features effectively without distance distortion.
- **Target Vector $y$**: Encoding multi-class classification target labels.

### 3. The Magnitude Bias Danger
If applied to **nominal** (unordered) features (e.g. `Red=0, Blue=1, Green=2`), linear models ($y = w_1 x + b$) assume `Green` is mathematically 2x `Blue`, introducing false linear relationships.

### 4. Syntax
```python
# Explicit Dictionary Mapping (Recommended for Ordinal Features):
order_map = {'Basic': 0, 'Standard': 1, 'Premium': 2}
df['Tier_Encoded'] = df['Tier'].map(order_map)

# Scikit-Learn OrdinalEncoder:
from sklearn.preprocessing import OrdinalEncoder
oe = OrdinalEncoder(categories=[['Low', 'Medium', 'High']])
df[['Tier_OE']] = oe.fit_transform(df[['Tier']])
```

### 5. Summary
Use explicit dictionary mapping or `OrdinalEncoder` for ordered categories, and avoid Label Encoding nominal categories in linear models.
