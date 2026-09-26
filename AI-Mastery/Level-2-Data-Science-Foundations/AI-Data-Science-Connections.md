# AI and Data Science Connections

This document details how Level 2 Data Science Foundations directly supports and powers Artificial Intelligence (AI) and Machine Learning (ML) algorithms taught in Level 3 and beyond.

---

## 1. NumPy ➔ Numerical Representation & Vectorized Computations
- **Vectorized Array Operations**: Neural Network forward and backward propagation steps rely entirely on vectorized array matrix operations rather than slow Python loops.
- **Linear Algebra (`numpy.linalg`)**: Dot products, matrix inversions, and eigenvalue decompositions compute principal components (PCA) and linear regression weights $\mathbf{w} = (X^T X)^{-1} X^T y$.
- **Tensor Shapes**: Multidimensional arrays model scalars (0D), feature vectors (1D), tabular datasets (2D), RGB image channels (3D), and image batches (4D).

---

## 2. Pandas ➔ Tabular Data Manipulation & Feature Engineering
- **Entity Feature Extraction**: `df.groupby()` aggregates historical entity transaction logs into predictive features (e.g. `user_avg_spend`).
- **Data Reshaping**: `pd.pivot_table()` constructs sparse user-item interaction matrices for collaborative filtering recommendation systems.
- **Time Series Alignment**: `DatetimeIndex` and `.shift(1)` generate autoregressive lag features for time series forecasting without target leakage.

---

## 3. Data Visualization ➔ Pattern Discovery & Model Diagnostics
- **Exploratory Data Analysis**: Histograms and boxplots expose feature skewness and extreme outliers before model selection.
- **Correlation Heatmaps**: `sns.heatmap(df.corr())` identifies multi-collinear feature pairs, guiding feature reduction.
- **Model Diagnostics**: Visualizing loss curves (Train vs Validation Loss over epochs) diagnoses underfitting vs overfitting.

---

## 4. Data Preprocessing ➔ ML-Ready Numeric Representation
- **Categorical Encoding**: `pd.get_dummies()` and `OneHotEncoder` map discrete string labels to orthogonal binary basis vectors in $\mathbb{R}^K$.
- **Feature Scaling**: Z-score Standardization and Min-Max Normalization transform feature scales to ensure gradient descent convergence and fair distance metrics in KNN and SVM algorithms.
- **Outlier Capping**: Winsorization (`.clip()`) bounds extreme values, preserving linear model stability.
- **Train/Test Isolation**: Enforces strict leakage boundaries by fitting transformers ONLY on training partitions.
