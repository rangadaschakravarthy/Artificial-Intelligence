# Day 100 Theory: Mathematical Functions

### 1. What Is It?
NumPy mathematical functions are vectorized C-implemented ufuncs that compute elementary mathematical operations (`exp`, `log`, `sin`, `sqrt`, `round`) element-by-element across arrays.

### 2. Why Does It Exist?
Applying scalar Python `math` functions in a loop is slow and fails on vector input arrays. NumPy ufuncs operate directly on whole `ndarray` buffers at C-speed.

### 3. Intuition
Instead of manually calculating logarithms or exponentials for 1,000 numbers using a handheld calculator, NumPy ufuncs execute compiled math hardware instructions across all 1,000 array elements instantly.

### 4. Syntax
```python
import numpy as np

x = np.array([1.0, 2.0, 3.0])

# Exponential & Logarithm
exp_x = np.exp(x)
log_x = np.log(x)     # Natural log (base e)
log1p_x = np.log1p(x) # Accurate log(1 + x) for small x

# Trigonometric
sin_x = np.sin(x)

# Rounding
rounded = np.round(x, decimals=2)
```

### 5. Parameters
- `x`: Input array.
- `out`: Optional output array buffer destination.

### 6. How It Works
NumPy delegates to C standard math libraries (`libm` / Intel SVML), utilizing vector SIMD math routines (e.g. `__v2df_log`) that evaluate polynomial expansions in CPU registers.

### 7. Simple Example
```python
import numpy as np
a = np.array([0.0, np.pi / 2, np.pi])
print("Sin values:", np.sin(a)) # [0. 1. 0.]
```

### 8. Intermediate Example
```python
import numpy as np
# Numerical stability with log1p
small_x = 1e-15
print("Standard log(1 + x) loss:", np.log(1.0 + small_x)) # Underflow precision loss!
print("Numerically stable log1p:", np.log1p(small_x))     # Exact!
```

### 9. Output Interpretation
`np.log1p(x)` computes $\ln(1 + x)$ accurately for values near zero where standard $1.0 + x$ loses floating point precision.

### 10. Common Mistakes
- Taking `np.log(0)` or `np.log(-1)` resulting in `-inf` or `nan` with `RuntimeWarning`.
- Confusing `np.round()` (rounds to nearest even) with standard rounding expectations.

### 11. Data Science Connection
Transforming skewed distribution feature columns in Pandas DataFrames using `np.log1p()` to normalize variance.

### 12. AI/ML Connection
Implementing Tanh activation $	anh(x) = 	ext{np.tanh}(x)$ and Binary Cross-Entropy loss $	ext{NLL} = -[y \ln(p) + (1-y) \ln(1-p)]$.

### 13. Interview Insight
Question: "Why is `np.log1p(x)` preferred over `np.log(1 + x)` when $x$ is very small ($x pprox 10^{-15}$)?"
Answer: Floating point representation of $1.0 + 10^{-15}$ loses precision bits due to catastrophic cancellation. `np.log1p(x)` uses a Taylor series expansion specifically designed to evaluate $\ln(1 + x)$ without adding $1.0$ first.

### 14. Summary
NumPy ufuncs perform fast, vectorized mathematical calculations. Use `np.log1p` for small decimal stability and `np.exp` for exponential scaling.
