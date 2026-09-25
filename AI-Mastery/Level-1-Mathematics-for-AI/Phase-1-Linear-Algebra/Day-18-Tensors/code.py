# Day 18 — Tensors
import numpy as np

# 1. Tensor Ranks (0D to 4D)
scalar_0d = np.array(3.14)
vector_1d = np.array([1, 2, 3])
matrix_2d = np.array([[1, 2], [3, 4]])
tensor_3d = np.random.randn(2, 3, 4)           # Time-series: (Batch, Steps, Features)
tensor_4d = np.random.randn(32, 3, 64, 64)      # Image Batch: (Batch, Channels, H, W)

print(f"0D Tensor shape: {scalar_0d.shape}, rank: {scalar_0d.ndim}")
print(f"1D Tensor shape: {vector_1d.shape}, rank: {vector_1d.ndim}")
print(f"2D Tensor shape: {matrix_2d.shape}, rank: {matrix_2d.ndim}")
print(f"3D Tensor shape: {tensor_3d.shape}, rank: {tensor_3d.ndim}")
print(f"4D Tensor shape: {tensor_4d.shape}, rank: {tensor_4d.ndim}")

# 2. Reshaping & Permuting Axes
# Flatten 4D image batch (32, 3, 64, 64) -> 2D (32, 3*64*64)
batch_flattened = tensor_4d.reshape(32, -1)
print(f"\nFlattened 2D Batch shape: {batch_flattened.shape}")

# Permute PyTorch (B, C, H, W) -> TensorFlow (B, H, W, C)
tf_tensor = np.transpose(tensor_4d, (0, 2, 3, 1))
print(f"Permuted TensorFlow shape (B, H, W, C): {tf_tensor.shape}")

# 3. Einstein Summation (einsum) Batch MatMul
A_batch = np.random.randn(10, 4, 5)
B_batch = np.random.randn(10, 5, 2)
C_batch = np.einsum('bik,bkj->bij', A_batch, B_batch)
print(f"\nEinsum Batch MatMul Output shape: {C_batch.shape} (Matches 10x4x2!)")
