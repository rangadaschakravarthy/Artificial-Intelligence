# Day 155 Theory: Categorical and Numerical Features

### 1. What Is It?
Separating feature types identifies which columns require numerical scaling (Standardization/Normalization) versus categorical transformations (One-Hot / Target Encoding).

### 2. Feature Classification Algorithm
- If `dtype == object` or `category`:
  - If `nunique() <= threshold`: Low-Cardinality Categorical (Use One-Hot Encoding).
  - If `nunique() > threshold`: High-Cardinality Categorical (Use Target Encoding or Frequency Encoding).
- If `dtype` is numeric (`int64`, `float64`):
  - If values are discrete codes (e.g. `ZipCode`): Recast as Categorical!
  - Otherwise: Continuous Numerical (Use Scaling).

### 3. Summary
Automated dtype auditing ensures each feature receives appropriate preprocessing transformations.
