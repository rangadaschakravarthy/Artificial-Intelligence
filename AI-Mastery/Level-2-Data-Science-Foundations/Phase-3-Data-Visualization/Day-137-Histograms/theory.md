# Day 137 Theory: Histograms

### 1. What Is It?
A Histogram partitions continuous numerical data into consecutive non-overlapping intervals (bins) and displays counts of observations falling into each bin.

### 2. Key Parameters
- `bins`: Number of bins (e.g. `bins=30`) or explicit edge arrays.
- `density`: bool. If `True`, normalizes counts to form a probability density (area under histogram equals 1.0).
- `cumulative`: bool. If `True`, displays cumulative distribution (CDF).

### 3. Syntax
```python
n, bins, patches = ax.hist(data, bins=25, density=True, alpha=0.6, color='g', edgecolor='black')
```

### 4. Summary
Histograms illustrate dataset continuous distribution shape, spread, and modal peaks.
