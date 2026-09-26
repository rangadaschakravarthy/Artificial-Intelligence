# Day 95 Worked Examples: Reshaping

## Example 1 — Beginner: Reshaping 1D to 2D
```python
import numpy as np

vec = np.arange(6) # [0, 1, 2, 3, 4, 5]
mat_2x3 = vec.reshape(2, 3)
mat_3x2 = vec.reshape(3, 2)

print("2x3 Matrix:
", mat_2x3)
print("3x2 Matrix:
", mat_3x2)
```

## Example 2 — Practical: Flatten vs Ravel Comparison
```python
import numpy as np

grid = np.array([[10, 20], [30, 40]])

r_view = grid.ravel()   # View
f_copy = grid.flatten() # Copy

r_view[0] = 999
print("Original Grid after ravel edit:
", grid) # Mutated!
print("Flatten Copy:", f_copy)                   # Unchanged [10, 20, 30, 40]
```

## Example 3 — Intermediate: Transposing and Swapping Axes
```python
import numpy as np

# 2D Matrix Transpose
m = np.array([[1, 2, 3], [4, 5, 6]]) # Shape (2, 3)
print("Matrix Transpose (3, 2):
", m.T)

# 3D Tensor Axis Swap
tensor = np.zeros((2, 3, 4))
swapped = tensor.swapaxes(0, 2) # Swap axis 0 and axis 2
print("Swapped Shape:", swapped.shape) # (4, 3, 2)
```

## Example 4 — Real Dataset: Converting Image Channel Format (HWC to CHW)
```python
import numpy as np

# OpenCV/Matplotlib Image Format: (Height, Width, Channels) -> (28, 28, 3)
hwc_image = np.random.randint(0, 256, (28, 28, 3), dtype=np.uint8)

# Convert to PyTorch Conv2D Format: (Channels, Height, Width) -> (3, 28, 28)
chw_image = np.transpose(hwc_image, (2, 0, 1))

print("Original HWC Shape:", hwc_image.shape)
print("PyTorch CHW Shape: ", chw_image.shape)
```

## Example 5 — AI/ML Application: Preparing Image Batches for Neural Net Input
```python
import numpy as np

# Single grayscale image of size 28x28: Shape (28, 28)
single_img = np.random.randn(28, 28)

# Neural network expects batch dimension: Shape (1, 1, 28, 28) -> (Batch, Channels, Height, Width)
batch_input = single_img.reshape(1, 1, 28, 28)
print("Batch Neural Net Input Shape:", batch_input.shape)
```
