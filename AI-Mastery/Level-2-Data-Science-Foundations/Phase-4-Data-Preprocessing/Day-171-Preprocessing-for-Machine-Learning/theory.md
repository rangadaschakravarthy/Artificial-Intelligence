# Day 171 Theory: Preprocessing for Machine Learning

### 1. What Is It?
Preprocessing for Machine Learning tailors feature transformation choices directly to the mathematical assumptions of the downstream algorithm.

### 2. Algorithm Matrix Guide
| Model Family | Feature Scaling Required? | Categorical Encoding Strategy | Outlier Handling |
|---|---|---|---|
| **Linear / Logistic** | **Yes** (Standardization) | One-Hot (`drop_first=True`) | Highly Sensitive (Winsorize/Log) |
| **KNN / SVM** | **Yes** (Standard / Min-Max) | One-Hot Encoding | Sensitive |
| **Decision Trees / Forests**| **No** (Scale Invariant) | Ordinal / Label / Target | Robust to Outliers |
| **Neural Networks** | **Yes** (Min-Max / Standard) | One-Hot Encoding | Sensitive |

### 3. Summary
Linear and distance models require scaled, one-hot encoded, log-transformed features. Tree models accept raw scales and ordinal encodings.
