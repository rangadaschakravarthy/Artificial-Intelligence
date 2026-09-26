# Day 160 Theory: Normalization

### 1. What Is It?
Min-Max Normalization rescales numerical feature values into a fixed range, typically $[0, 1]$, based on the feature's minimum and maximum values.

### 2. Formula

$$
x' = rac{x - x_{\min}}{x_{\max} - x_{\min}}
$$

For arbitrary target range $[a, b]$:

$$
x'' = a + rac{(x - x_{\min})(b - a)}{x_{\max} - x_{\min}}
$$

### 3. Outlier Sensitivity Warning
If a feature contains an extreme outlier ($x_{\max} = 1,000,000$ while normal values range $[0, 100]$), Min-Max Normalization squashes all normal values into a tiny range $[0, 0.0001]$, destroying feature variance.

### 4. Syntax
```python
from sklearn.preprocessing import MinMaxScaler

scaler = MinMaxScaler(feature_range=(0, 1))
X_scaled = scaler.fit_transform(X_train)
```

### 5. Summary
Min-Max Normalization bounds features into $[0, 1]$, but is sensitive to extreme outliers.
