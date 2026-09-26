# Day 86 Worked Examples: NumPy Introduction

## Example 1 — Beginner: Creating Arrays from Lists
```python
import numpy as np
python_list = [10, 20, 30]
np_array = np.array(python_list)
print("Array:", np_array)
print("Type:", type(np_array))
```
Output:
Array: [10 20 30]
Type: <class 'numpy.ndarray'>

## Example 2 — Practical: Speed Benchmark (List vs NumPy)
```python
import time
import numpy as np

size = 1_000_000
py_list = list(range(size))
np_arr = np.arange(size)

start = time.time()
py_res = [x * 2 for x in py_list]
py_time = time.time() - start

start = time.time()
np_res = np_arr * 2
np_time = time.time() - start

print(f"Python List Time: {py_time:.4f}s")
print(f"NumPy Array Time: {np_time:.4f}s")
print(f"Speedup Factor: {py_time / np_time:.2f}x faster!")
```

## Example 3 — Intermediate: Inspecting Array Attributes
```python
import numpy as np
data = np.array([[1, 2, 3], [4, 5, 6]], dtype=np.int32)
print("ndim:", data.ndim)
print("shape:", data.shape)
print("size:", data.size)
print("dtype:", data.dtype)
print("itemsize:", data.itemsize, "bytes")
print("nbytes:", data.nbytes, "bytes")
```

## Example 4 — Real Dataset: Representing Image Pixels
```python
import numpy as np
# 2x2 RGB Image (2 rows, 2 columns, 3 color channels)
image_tensor = np.array([
    [[255, 0, 0], [0, 255, 0]],
    [[0, 0, 255], [255, 255, 255]]
], dtype=np.uint8)

print("Image shape:", image_tensor.shape)
print("Top-left pixel RGB:", image_tensor[0, 0])
```

## Example 5 — AI/ML Application: Feature Matrix Representation
```python
import numpy as np
# 3 samples, 2 features (Age, Income in $k)
X = np.array([
    [25, 55.0],
    [30, 72.5],
    [45, 120.0]
])
print("Feature matrix X shape:", X.shape)
print("Mean age & income:", X.mean(axis=0))
```
