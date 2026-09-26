# Day 87 Worked Examples: NumPy Arrays

## Example 1 — Beginner: Creating Multi-Dimensional Arrays
```python
import numpy as np

scalar_0d = np.array(7)
vector_1d = np.array([1, 2, 3])
matrix_2d = np.array([[1, 2], [3, 4]])
tensor_3d = np.array([[[1], [2]], [[3], [4]]])

print("0D ndim:", scalar_0d.ndim)
print("1D ndim:", vector_1d.ndim)
print("2D ndim:", matrix_2d.ndim)
print("3D ndim:", tensor_3d.ndim)
```

## Example 2 — Practical: Memory View vs Copy Demo
```python
import numpy as np

original = np.array([10, 20, 30, 40, 50])
view_arr = original[1:4] # View
copy_arr = original[1:4].copy() # Explicit Copy

view_arr[0] = 999 # Mutates original!
print("Original after view edit:", original)

copy_arr[1] = 888 # Does NOT mutate original
print("Original after copy edit:", original)
```

## Example 3 — Intermediate: Strides and Pointer Memory Alignment
```python
import numpy as np

x = np.arange(6, dtype=np.int32).reshape(2, 3)
print("Matrix:
", x)
print("Shape:", x.shape)
print("Strides:", x.strides) # (12, 4) -> 12 bytes to move 1 row, 4 bytes to move 1 col

# Checking flags
print("C-Contiguous:", x.flags.c_contiguous)
```

## Example 4 — Real Dataset: Batch of Grayscale Images (3D Tensor)
```python
import numpy as np

# 4 images, each 28x28 pixels (like MNIST dataset)
batch_images = np.zeros((4, 28, 28), dtype=np.uint8)
print("Batch Tensor Shape:", batch_images.shape)
print("Single Image Shape:", batch_images[0].shape)
```

## Example 5 — AI/ML Application: Linear Model Weight & Bias Representation
```python
import numpy as np

# 3 input features, 2 output neurons
W = np.random.randn(3, 2) # 2D Matrix of Weights
b = np.random.randn(2)    # 1D Vector of Biases

x = np.array([1.5, -2.0, 0.5]) # 1D Input sample
y_pred = np.dot(x, W) + b
print("Output prediction vector shape:", y_pred.shape)
```
