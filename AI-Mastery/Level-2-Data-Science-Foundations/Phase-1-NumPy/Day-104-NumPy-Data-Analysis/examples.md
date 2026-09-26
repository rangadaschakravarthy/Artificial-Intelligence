# Day 104 Worked Examples: NumPy Data Analysis

## Example 1 — Beginner: Percentiles and Five-Number Summary
```python
import numpy as np

data = np.array([12, 15, 18, 22, 30, 45, 50, 65, 88, 95])

p0 = np.min(data)
p25 = np.percentile(data, 25)
p50 = np.median(data)
p75 = np.percentile(data, 75)
p100 = np.max(data)

print("Five-Number Summary:")
print(f"Min (0%):   {p0}")
print(f"Q1 (25%):   {p25}")
print(f"Q2 (50%):   {p50}")
print(f"Q3 (75%):   {p75}")
print(f"Max (100%): {p100}")
```

## Example 2 — Practical: Correlation Matrix Calculation
```python
import numpy as np

# Dataset with 3 features: [Feature 0, Feature 1 (correlated to F0), Feature 2 (random)]
rng = np.random.default_rng(42)
f0 = rng.normal(10, 2, 100)
f1 = f0 * 2.5 + rng.normal(0, 0.5, 100) # Strong positive correlation
f2 = rng.uniform(0, 100, 100)           # Uncorrelated noise

X = np.column_stack((f0, f1, f2))

# Compute 3x3 Correlation Matrix (rowvar=False for column features)
corr = np.corrcoef(X, rowvar=False)

print("Correlation Matrix (3x3):
", np.round(corr, 3))
```

## Example 3 — Intermediate: Data Binning with np.histogram & np.digitize
```python
import numpy as np

ages = np.array([18, 22, 25, 35, 42, 58, 63, 71])

# Define bin edges: [18-30), [30-50), [50-80)
bin_edges = np.array([18, 30, 50, 80])

# Assign each age to a bin index (1, 2, or 3)
bin_indices = np.digitize(ages, bin_edges)

print("Ages:       ", ages)
print("Bin Indices:", bin_indices)
```

## Example 4 — Real Dataset: Identifying & Removing Outliers via IQR Rule
```python
import numpy as np

# House Prices in $k (with extreme outliers)
prices = np.array([150, 160, 175, 180, 190, 200, 210, 220, 850, 1200])

q25, q75 = np.percentile(prices, [25, 75])
iqr = q75 - q25
lower_bound = q25 - 1.5 * iqr
upper_bound = q75 + 1.5 * iqr

mask_valid = (prices >= lower_bound) & (prices <= upper_bound)
clean_prices = prices[mask_valid]
outliers = prices[~mask_valid]

print("Q1:", q25, "Q3:", q75, "IQR:", iqr)
print("Upper Outlier Threshold:", upper_bound)
print("Detected Outliers:", outliers)
print("Clean Prices:", clean_prices)
```

## Example 5 — AI/ML Application: Feature Selection based on Correlation Threshold
```python
import numpy as np

# 4 Features
rng = np.random.default_rng(42)
f0 = rng.normal(0, 1, 100)
f1 = f0 * 0.99 # Redundant feature! (corr ≈ 1.0)
f2 = rng.normal(0, 1, 100)
f3 = rng.normal(0, 1, 100)

X = np.column_stack((f0, f1, f2, f3))
corr_matrix = np.corrcoef(X, rowvar=False)

# Identify features with pairwise correlation > 0.95
threshold = 0.95
high_corr_pairs = []
for i in range(X.shape[1]):
    for j in range(i + 1, X.shape[1]):
        if abs(corr_matrix[i, j]) > threshold:
            high_corr_pairs.append((i, j, corr_matrix[i, j]))

print("Correlation Matrix:
", np.round(corr_matrix, 2))
print("Redundant High-Correlation Feature Pairs (>0.95):", high_corr_pairs)
```
