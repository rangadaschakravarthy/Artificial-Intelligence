# Day 99 Theory: Aggregation and Statistics

### 1. What Is It?
Statistical aggregations collapse array dimensions to compute summary statistics (mean, variance, min, max, argmax) across entire tensors or specified axes.

### 2. Why Does It Exist?
Raw datasets contain thousands of individual data points. Aggregation distills high-dimensional distributions into concise numerical summaries.

### 3. Intuition
Instead of reading 1,000 student test scores, `mean()` gives you the class average, `std()` gives the score spread, and `argmax()` identifies the top-scoring student.

### 4. Syntax
```python
import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6]])

# Total mean
total_mean = np.mean(arr) # 3.5

# Column means (axis=0)
col_means = np.mean(arr, axis=0) # [2.5, 3.5, 4.5]

# Max index position
max_idx = np.argmax(arr) # 5 (flattened index)
```

### 5. Parameters
- `axis`: Axis or axes along which to compute reduction.
- `ddof`: Means Delta Degrees of Freedom. `ddof=0` computes population variance; `ddof=1` computes sample variance (Bessel's correction!).
- `keepdims`: Boolean to retain reduced dimensions as length-1 axes.

### 6. How It Works
NumPy C-reducers iterate through contiguous array memory buffers, maintaining accumulator variables in CPU registers and dividing by element counts.

### 7. Simple Example
```python
import numpy as np
data = np.array([10, 20, 30, 40])
print("Mean:", np.mean(data))   # 25.0
print("Std:",  np.std(data))    # 11.18
```

### 8. Intermediate Example
```python
import numpy as np
# Array with missing NaN values
data_nan = np.array([10.0, np.nan, 30.0])
print("Standard mean:", np.mean(data_nan))    # nan!
print("NaN-robust mean:", np.nanmean(data_nan)) # 20.0
```

### 9. Output Interpretation
Standard `np.mean` propagates `nan`. `np.nanmean` ignores `nan` entries and computes the average of valid numbers.

### 10. Common Mistakes
- Forgetting `ddof=1` when computing sample variance/standard deviation (NumPy defaults to population variance `ddof=0`!).
- Applying standard `mean()` to datasets containing `NaN` values, resulting in `nan` outputs.

### 11. Data Science Connection
Pandas DataFrame `.describe()` summary tables are computed directly using NumPy statistical reduction functions.

### 12. AI/ML Connection
Converting output class probability vectors $P = [0.1, 0.7, 0.2]$ into predicted class label $\hat{y} = 	ext{argmax}(P) = 1$.

### 13. Interview Insight
Question: "Why does `np.var(arr)` give a slightly different result than `pd.Series(arr).var()`?"
Answer: NumPy defaults to population variance `ddof=0` (divides by $N$). Pandas defaults to sample variance `ddof=1` (divides by $N-1$, Bessel's correction). Set `np.var(arr, ddof=1)` to match Pandas!

### 14. Summary
Aggregation functions reduce tensor rank along specified axes. Use `argmax` for prediction class selection and `ddof=1` for sample variance.
