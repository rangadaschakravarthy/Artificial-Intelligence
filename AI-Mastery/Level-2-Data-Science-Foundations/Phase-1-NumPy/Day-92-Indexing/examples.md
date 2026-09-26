# Day 92 Worked Examples: Indexing

## Example 1 — Beginner: 1D Array Indexing & Negative Indices
```python
import numpy as np

arr = np.array([10, 20, 30, 40, 50])

print("First element (index 0):", arr[0])
print("Third element (index 2):", arr[2])
print("Last element (index -1):", arr[-1])
print("Second to last (index -2):", arr[-2])
```

## Example 2 — Practical: 2D Matrix Element Access & Mutation
```python
import numpy as np

matrix = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

print("Center element (row 1, col 1):", matrix[1, 1]) # 5
print("Bottom-Right element (row 2, col 2):", matrix[2, 2]) # 9

# Mutating an element
matrix[0, 0] = 99
print("Mutated Matrix:
", matrix)
```

## Example 3 — Intermediate: 3D Tensor Indexing
```python
import numpy as np

# 3D Tensor of shape (2, 2, 3)
tensor = np.array([
    [[1, 2, 3], [4, 5, 6]],
    [[7, 8, 9], [10, 11, 12]]
])

print("Element at depth 1, row 0, col 2:", tensor[1, 0, 2]) # 9
```

## Example 4 — Real Dataset: Extracting Single Patient Record
```python
import numpy as np

# Dataset shape (4, 3): 4 Patients, 3 Features (Age, BP, Cholesterol)
patients = np.array([
    [25, 120, 180],
    [45, 140, 220],
    [35, 115, 190],
    [50, 135, 210]
])

patient_2_age = patients[1, 0]
patient_4_cholesterol = patients[3, 2]

print("Patient 2 Age:", patient_2_age)
print("Patient 4 Cholesterol:", patient_4_cholesterol)
```

## Example 5 — AI/ML Application: Extracting Top-Left Pixel from Image Batch
```python
import numpy as np

# Batch of 2 RGB images of shape (2, 32, 32, 3)
image_batch = np.random.randint(0, 256, (2, 32, 32, 3))

# Access Red channel (index 0) of top-left pixel (row 0, col 0) of Image 1 (index 0)
red_val = image_batch[0, 0, 0, 0]
print("Top-Left Red Pixel Value of Image 1:", red_val)
```
