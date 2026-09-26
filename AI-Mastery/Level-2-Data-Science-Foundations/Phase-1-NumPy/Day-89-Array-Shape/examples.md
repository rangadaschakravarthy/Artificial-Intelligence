# Day 89 Worked Examples: Array Shape

## Example 1 — Beginner: Inspecting Shapes of Different Tensors
```python
import numpy as np

v = np.array([1, 2, 3, 4])
m = np.array([[1, 2], [3, 4], [5, 6]])
t = np.ones((2, 3, 4))

print("Vector Shape:", v.shape) # (4,)
print("Matrix Shape:", m.shape) # (3, 2)
print("Tensor Shape:", t.shape) # (2, 3, 4)
```

## Example 2 — Practical: Reshaping with Automatic Dimension (-1)
```python
import numpy as np

data = np.arange(20) # 20 elements

grid1 = data.reshape(4, -1) # 4 rows -> 5 cols
grid2 = data.reshape(-1, 2) # 2 cols -> 10 rows

print("Grid 1 Shape:", grid1.shape)
print("Grid 2 Shape:", grid2.shape)
```

## Example 3 — Intermediate: Validating Matrix Multiplication Inner Dimensions
```python
import numpy as np

A = np.random.randn(5, 3) # (5, 3)
B = np.random.randn(3, 2) # (3, 2)

if A.shape[1] == B.shape[0]:
    C = np.dot(A, B)
    print("Matrix Multiplication Success! Result Shape:", C.shape) # (5, 2)
else:
    print("Shape Mismatch!")
```

## Example 4 — Real Dataset: Flattening Image Batches for ML Classifier
```python
import numpy as np

# 100 grayscale images of 28x28 pixels: Shape (100, 28, 28)
images = np.random.randn(100, 28, 28)

# Flatten images for Scikit-Learn input: Shape (100, 784)
flat_features = images.reshape(images.shape[0], -1)
print("Flattened Feature Matrix Shape:", flat_features.shape)
```

## Example 5 — AI/ML Application: Permuting Tensor Axes (Image Transpose)
```python
import numpy as np

# PyTorch format: (Batch, Channels, Height, Width) -> (10, 3, 32, 32)
pytorch_tensor = np.zeros((10, 3, 32, 32))

# Convert to Matplotlib format: (Batch, Height, Width, Channels) -> (10, 32, 32, 3)
mpl_tensor = np.transpose(pytorch_tensor, (0, 2, 3, 1))
print("Matplotlib Tensor Shape:", mpl_tensor.shape)
```
