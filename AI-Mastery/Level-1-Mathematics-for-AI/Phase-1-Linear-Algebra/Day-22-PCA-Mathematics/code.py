# Day 22 — PCA Mathematics
import numpy as np

# 1. Generate Synthetic 2D Dataset (correlated features)
np.random.seed(42)
x1 = np.random.normal(0, 1, 100)
x2 = 2.0 * x1 + np.random.normal(0, 0.5, 100)
X = np.column_stack([x1, x2])

print(f"Original Data X shape: {X.shape}")

# 2. Step 1: Mean Centering
X_mean = np.mean(X, axis=0)
X_centered = X - X_mean

# 3. Step 2: Covariance Matrix (1 / (N-1) * X_c^T * X_c)
N = X.shape[0]
cov_matrix = (1.0 / (N - 1)) * (X_centered.T @ X_centered)
print(f"\nCovariance Matrix:\n{cov_matrix}")

# 4. Step 3: Eigendecomposition of Covariance Matrix
eigenvalues, eigenvectors = np.linalg.eigh(cov_matrix)

# Sort in descending order
idx = np.argsort(eigenvalues)[::-1]
eigenvalues = eigenvalues[idx]
eigenvectors = eigenvectors[:, idx]

print(f"\nSorted Eigenvalues: {eigenvalues}")
print(f"Top Principal Component (Vector 1): {eigenvectors[:, 0]}")

# 5. Step 4: Explained Variance Ratio
var_ratio = eigenvalues / np.sum(eigenvalues)
print(f"Explained Variance Ratio: PC1 = {var_ratio[0]*100:.2f}%, PC2 = {var_ratio[1]*100:.2f}%")

# 6. Step 5: Project Data onto 1st Principal Component (2D -> 1D)
W1 = eigenvectors[:, :1]  # Top 1 eigenvector
Z_1D = X_centered @ W1
print(f"\nProjected 1D Data shape: {Z_1D.shape}")
