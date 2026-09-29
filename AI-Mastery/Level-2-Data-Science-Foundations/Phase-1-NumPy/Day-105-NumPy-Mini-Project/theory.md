# Day 105 Theory: NumPy Mini-Project Architecture

### 1. What Is It?
This mini-project integrates all Phase 1 NumPy concepts—array attributes, indexing, slicing, broadcasting, vectorization, statistical aggregations, and linear algebra—into a production-grade data processing workflow.

### 2. Pipeline Architecture
```
Raw Dataset Array (with NaNs & Outliers)
       │
       ▼
1. Inspection & Cleaning (Median Imputation)
       │
       ▼
2. Statistical Profiling & Outlier Clipping (1.5 * IQR)
       │
       ▼
3. Feature Standardization (Z-score via Broadcasting)
       │
       ▼
4. Model Training (Closed-Form Normal Equation w = (X^T X)^-1 X^T y)
       │
       ▼
5. Model Evaluation (MSE & R2 Metrics)
```

### 3. Step 1: Data Cleaning (Median Imputation)
Missing values represented as `np.nan` propagate errors through computations. Imputation replaces `np.nan` with non-missing column medians (`np.nanmedian`).

### 4. Step 2: Outlier Clipping (IQR Rule)
Extreme feature outliers warp linear regression weights. Features are bounded strictly to $[Q1 - 1.5 	imes 	ext{IQR}, Q3 + 1.5 	imes 	ext{IQR}]$.

### 5. Step 3: Z-Score Standardization
Broadcasting converts feature matrix $X$ into zero-mean unit-variance space:

$$
X_{	ext{std}} = \frac{X - \mu_{	ext{cols}}}{\sigma_{	ext{cols}}}
$$

### 6. Step 4: Closed-Form OLS Linear Regression
Adding a bias column of 1s to $X_{	ext{std}}$ allows solving optimal weight parameters $w$ directly using LAPACK matrix routines:

$$
w = (X_{	ext{std}}^T X_{	ext{std}})^{-1} X_{	ext{std}}^T y
$$

### 7. Summary
By completing this mini-project, you transition from basic NumPy syntax to building scalable numerical data processing engines.
