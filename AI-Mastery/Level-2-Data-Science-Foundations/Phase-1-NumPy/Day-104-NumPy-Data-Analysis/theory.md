# Day 104 Theory: NumPy Data Analysis

### 1. What Is It?
NumPy Data Analysis is the technique of exploring, summarizing, filtering, and transforming raw dataset arrays using NumPy's high-performance numerical routines.

### 2. Why Does It Exist?
Understanding data distributions, relationships, percentiles, and correlations is required prior to building statistical models or preprocessing pipelines.

### 3. Intuition
NumPy Data Analysis is like performing a medical checkup on a dataset: inspecting its average health (mean), variability (std), extreme points (percentiles), and feature relationships (correlation).

### 4. Syntax
```python
import numpy as np

# Feature Matrix X (N samples, D features)
X = np.random.randn(100, 3)

# Percentiles [25th, 50th, 75th]
q25, q50, q75 = np.percentile(X, [25, 50, 75], axis=0)

# Pearson Correlation Matrix
corr_matrix = np.corrcoef(X, rowvar=False)

# Histogram Binning
counts, bin_edges = np.histogram(X[:, 0], bins=5)
```

### 5. Parameters
- `rowvar`: Boolean in `np.corrcoef` / `np.cov`. If `False`, columns represent variables and rows represent observations.

### 6. How It Works
`np.corrcoef(X, rowvar=False)` computes covariance matrix $C = \frac{1}{N-1} X^T X$ for centered data, then normalizes by feature standard deviations:
$$
ho_{i, j} = \frac{	ext{Cov}(X_i, X_j)}{\sigma_i \sigma_j}$$

### 7. Simple Example
```python
import numpy as np
x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 4, 6, 8, 10])
print("Correlation:", np.corrcoef(x, y)[0, 1]) # 1.0 (Perfect positive correlation)
```

### 8. Intermediate Example
```python
import numpy as np
data = np.array([10, 15, 20, 25, 100]) # 100 is outlier
q25, q75 = np.percentile(data, [25, 75])
iqr = q75 - q25
upper_bound = q75 + 1.5 * iqr
clean_data = data[data <= upper_bound]
print("Clean Data (no outliers):", clean_data) # [10, 15, 20, 25]
```

### 9. Output Interpretation
The 1.5*IQR rule identifies `100` as an outlier ($100 > 25 + 1.5 	imes 10 = 40$) and filters it out cleanly.

### 10. Common Mistakes
- Forgetting `rowvar=False` in `np.corrcoef()`, causing NumPy to compute correlation between rows instead of columns/features.
- Confusing `np.quantile` (inputs `0.0..1.0`) with `np.percentile` (inputs `0..100`).

### 11. Data Science Connection
Pandas methods `.corr()`, `.quantile()`, and `.value_counts()` wrap these exact NumPy data analysis functions.

### 12. AI/ML Connection
Feature selection filters out highly correlated features ($
ho > 0.95$) to prevent multi-collinearity in linear models.

### 13. Interview Insight
Question: "How do you calculate a Pearson correlation matrix for a feature matrix $X$ using raw matrix operations in NumPy?"
Answer: Center $X$: $X_c = X - \mu$. Compute Covariance: $C = \frac{1}{N-1} X_c^T X_c$. Compute Std Vector: $s = \sqrt{	ext{diag}(C)}$. Correlation: $R = \frac{C}{s[:, 	ext{newaxis}] \cdot s[	ext{newaxis}, :]}$.

### 14. Summary
NumPy provides functions for descriptive data profiling (`percentile`, `corrcoef`, `histogram`). Use IQR bounds to detect and clean outliers.
