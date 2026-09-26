# Data Science Foundations — Technical Interview Preparation

Comprehensive technical interview questions and answers organized by core module.

---

## 1. NumPy & Vectorization
### Q1: What is the difference between a Python List and a NumPy `ndarray`?
**Answer**: Python lists store pointers to scattered objects in memory (high dynamic overhead). NumPy `ndarray` objects store contiguous blocks of homogeneous data types, enabling SIMD (Single Instruction, Multiple Data) CPU hardware acceleration and fast vectorized computations.

### Q2: What is Broadcasting in NumPy?
**Answer**: Broadcasting is NumPy's mechanism for executing element-wise operations on arrays of differing shapes. Broadcasting automatically expands smaller array dimensions along trailing axes without copying data in memory, provided dimensions are compatible.

---

## 2. Pandas & Data Manipulation
### Q3: What is the difference between `.loc` and `.iloc`?
**Answer**: `.loc[]` is label-based indexing (inclusive of stop index label). `.iloc[]` is integer positional indexing (exclusive of stop index position).

### Q4: Explain the difference between `pd.merge()` and `df.join()`.
**Answer**: `pd.merge()` defaults to matching on shared **columns** with `how='inner'`. `df.join()` defaults to matching on **row indices** with `how='left'`.

---

## 3. Data Preprocessing & Leakage
### Q5: What is Data Leakage, and how do you prevent it?
**Answer**: Data Leakage occurs when information from outside the training partition (such as test set statistics or target labels) contaminates the feature matrix. Prevent it by performing `train_test_split()` FIRST, then fitting scalers/encoders strictly on `X_train`.

### Q6: Why do distance-based algorithms require feature scaling?
**Answer**: Unscaled features with large numerical magnitudes (e.g. Income in tens of thousands) drown out small-scale features (e.g. Age in tens) during Euclidean distance calculations $\| \mathbf{x}_1 - \mathbf{x}_2 \|_2$. Scaling ensures fair feature weighting.
