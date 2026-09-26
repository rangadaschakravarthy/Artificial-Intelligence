# Day 88 Worked Examples: Array Dimensions

## Example 1 — Beginner: Visualizing Axes Operations
```python
import numpy as np

arr = np.array([[10, 20, 30],
                [40, 50, 60]])

print("Original Shape:", arr.shape)
print("Mean along axis=0 (column means):", arr.mean(axis=0)) # [25., 35., 45.]
print("Mean along axis=1 (row means):   ", arr.mean(axis=1)) # [20., 50.]
```

## Example 2 — Practical: Promoting 1D Vector to 2D Column Vector
```python
import numpy as np

v = np.array([1, 2, 3, 4])
print("Original 1D shape:", v.shape)

# Method 1: np.newaxis
col_v1 = v[:, np.newaxis]
print("Col vector shape (newaxis):", col_v1.shape)

# Method 2: np.expand_dims
col_v2 = np.expand_dims(v, axis=1)
print("Col vector shape (expand_dims):", col_v2.shape)
```

## Example 3 — Intermediate: Squeezing Dummy Dimensions
```python
import numpy as np

tensor = np.array([[[10], [20], [30]]]) # Shape (1, 3, 1)
print("Original Shape:", tensor.shape)

squeezed = np.squeeze(tensor)
print("Squeezed Shape:", squeezed.shape) # (3,)
print("Squeezed Values:", squeezed)
```

## Example 4 — Real Dataset: Normalizing Image Channels
```python
import numpy as np

# Batch of 2 RGB images of 3x3 pixels: Shape (2, 3, 3, 3) -> (Batch, H, W, Channels)
batch_img = np.random.randint(0, 256, (2, 3, 3, 3))

# Compute per-channel mean across Batch, Height, and Width: axes=(0, 1, 2)
channel_means = batch_img.mean(axis=(0, 1, 2))
print("Per-channel RGB means shape:", channel_means.shape) # (3,)
print("RGB Means:", channel_means)
```

## Example 5 — AI/ML Application: Feature Matrix Reshaping for ML Model Input
```python
import numpy as np

# Single sample feature vector: Shape (4,)
sample = np.array([5.1, 3.5, 1.4, 0.2])

# Scikit-learn models expect 2D array input of shape (n_samples, n_features)
model_input = sample[np.newaxis, :]
print("Model Input Shape:", model_input.shape) # (1, 4)
```
