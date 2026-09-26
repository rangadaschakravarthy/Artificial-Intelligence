# Day 93 Worked Examples: Slicing

## Example 1 — Beginner: 1D Array Slicing Operations
```python
import numpy as np

arr = np.array([0, 10, 20, 30, 40, 50, 60, 70])

print("First 3 elements:", arr[:3])      # [0, 10, 20]
print("Elements index 2 to 5:", arr[2:5]) # [20, 30, 40]
print("Every 2nd element:", arr[::2])     # [0, 20, 40, 60]
print("Reversed array:", arr[::-1])       # [70, 60, ..., 0]
```

## Example 2 — Practical: Extracting Sub-matrices and Columns
```python
import numpy as np

matrix = np.array([
    [10, 11, 12, 13],
    [14, 15, 16, 17],
    [18, 19, 20, 21]
])

print("First 2 rows:
", matrix[:2, :])
print("Columns 1 and 2:
", matrix[:, 1:3])
print("Top-Right 2x2 Sub-matrix:
", matrix[:2, 2:])
```

## Example 3 — Intermediate: Rank Preservation in Slicing
```python
import numpy as np

m = np.arange(9).reshape(3, 3)

row_1d = m[1, :]   # Integer row index -> 1D vector (3,)
row_2d = m[1:2, :] # Slice row index -> 2D matrix (1, 3)

print("1D Row:", row_1d, "Shape:", row_1d.shape)
print("2D Row:
", row_2d, "Shape:", row_2d.shape)
```

## Example 4 — Real Dataset: Splitting Features and Targets
```python
import numpy as np

# Dataset with 4 samples: 3 Features (X1, X2, X3) and 1 Target Label (Y)
dataset = np.array([
    [1.0, 2.0, 3.0, 0],
    [4.0, 5.0, 6.0, 1],
    [7.0, 8.0, 9.0, 0],
    [2.0, 4.0, 6.0, 1]
])

X = dataset[:, :-1] # All rows, all columns except last -> Features
y = dataset[:, -1]  # All rows, last column -> Target labels

print("Features X shape:", X.shape) # (4, 3)
print("Target y shape:", y.shape)   # (4,)
```

## Example 5 — AI/ML Application: Image Cropping & Bounding Box Extraction
```python
import numpy as np

# RGB Image of shape (100, 100, 3)
image = np.random.randint(0, 256, (100, 100, 3), dtype=np.uint8)

# Bounding box coordinates: ymin=20, ymax=60, xmin=30, xmax=70
cropped_roi = image[20:60, 30:70, :]

print("Original Image Shape:", image.shape)
print("Cropped ROI Shape:   ", cropped_roi.shape) # (40, 40, 3)
```
