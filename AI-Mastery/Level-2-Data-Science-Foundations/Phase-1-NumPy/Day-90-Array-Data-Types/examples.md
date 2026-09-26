# Day 90 Worked Examples: Array Data Types

## Example 1 — Beginner: Checking and Specifying Data Types
```python
import numpy as np

ints = np.array([1, 2, 3]) # Default int64 (or int32 on Windows)
floats = np.array([1.0, 2.0, 3.0]) # Default float64
bools = np.array([True, False, True])

print("Ints dtype:", ints.dtype)
print("Floats dtype:", floats.dtype)
print("Bools dtype:", bools.dtype)
```

## Example 2 — Practical: Explicit Type Casting with astype()
```python
import numpy as np

float_data = np.array([1.2, 2.8, 3.5, 4.1])
int_data = float_data.astype(np.int32) # Truncates decimals!

print("Original Floats:", float_data)
print("Casted Ints:    ", int_data)
```

## Example 3 — Intermediate: Demonstrating Integer Overflow
```python
import numpy as np

# Unsigned 8-bit integer (range 0 to 255)
u8 = np.array([250, 254, 255], dtype=np.uint8)

# Adding 10 causes modular wrapping overflow
overflow_res = u8 + 10
print("Overflow Result:", overflow_res) # [4, 8, 9]
```

## Example 4 — Real Dataset: Image Memory Optimization (uint8 vs float32)
```python
import numpy as np

# HD Image (1080p RGB) in float64 vs uint8
h, w = 1080, 1920
img_float = np.zeros((h, w, 3), dtype=np.float64) # Range 0.0 to 1.0
img_uint8 = np.zeros((h, w, 3), dtype=np.uint8)   # Range 0 to 255

print("Float64 Image Memory:", img_float.nbytes / (1024**2), "MB") # ~49.8 MB
print("Uint8 Image Memory:  ", img_uint8.nbytes / (1024**2), "MB") # ~5.9 MB
```

## Example 5 — AI/ML Application: Mixed Precision Floating Point Conversion
```python
import numpy as np

# Neural network weights in float64
weights_fp64 = np.random.randn(1000, 1000).astype(np.float64)

# Cast to float32 for standard DL framework or float16 for mixed precision
weights_fp32 = weights_fp64.astype(np.float32)
weights_fp16 = weights_fp64.astype(np.float16)

print("FP64 precision sample:", weights_fp64[0, 0])
print("FP32 precision sample:", weights_fp32[0, 0])
print("FP16 precision sample:", weights_fp16[0, 0])
```
