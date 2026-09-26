# Day 97 Theory: Broadcasting

### 1. What Is It?
Broadcasting is NumPy's mechanism for performing element-wise operations between arrays of different shapes without making unnecessary, memory-expensive copies of the smaller array.

### 2. Why Does It Exist?
If you have a $1000 	imes 100$ feature matrix and want to subtract a 100-element mean vector, copying the mean vector 1,000 times wastes RAM. Broadcasting streams the 100-element vector virtually down all 1,000 rows.

### 3. Intuition
Imagine stamping a single row pattern repeatedly onto a long paper roll as it passes through a printing press. The press doesn't store 1,000 pre-printed rolls; it applies the single stamp dynamically.

### 4. Syntax
```python
import numpy as np

# Matrix (3, 3) + Vector (3,)
M = np.ones((3, 3))
v = np.array([10, 20, 30])
res = M + v # Row-wise broadcasting!

# Column-wise broadcasting using np.newaxis
v_col = v[:, np.newaxis] # Shape (3, 1)
res_col = M + v_col
```

### 5. Parameters
- **Broadcasting Rule 1**: If arrays differ in rank, prepend `1`s to the shape of the smaller rank array until ranks match.
- **Broadcasting Rule 2**: Two dimensions are compatible if they are equal, OR if one of them is `1`.

### 6. How It Works
NumPy checks trailing shape dimensions from right to left:
- Array A: `(5, 4)`
- Array B: `(   4)` -> Padded to `(1, 4)`
- Dimension 1: $4 == 4$ (Match!)
- Dimension 0: $5$ vs $1$ ($1$ stretches to $5$). Result Shape: `(5, 4)`.

### 7. Simple Example
```python
import numpy as np
a = np.array([[1], [2], [3]]) # Shape (3, 1)
b = np.array([10, 20])        # Shape (2,) -> Padded to (1, 2)
print(a + b) # Output Shape (3, 2) Grid!
```

### 8. Intermediate Example
```python
import numpy as np
X = np.arange(12).reshape(4, 3)
means = X.mean(axis=0) # Shape (3,)
X_centered = X - means  # Subtract column means from each row!
print("Centered Matrix Shape:", X_centered.shape) # (4, 3)
```

### 9. Output Interpretation
`X - means` broadcasts `means` `(3,)` across all 4 rows of `X` `(4, 3)` cleanly.

### 10. Common Mistakes
- Trying to broadcast `(4, 3)` matrix with `(4,)` vector without converting `(4,)` to column shape `(4, 1)`.
- Assuming broadcasting physically copies memory in RAM (it only adjusts stride calculations!).

### 11. Data Science Connection
Subtracting column means, dividing by column standard deviations, and applying feature weights across Pandas DataFrames.

### 12. AI/ML Connection
Adding bias vector $b$ `(Out,)` to linear layer output matrix $XW$ `(Batch, Out)` in PyTorch / TensorFlow forward passes.

### 13. Interview Insight
Question: "Are shapes `(5, 1, 4)` and `(3, 4)` compatible for broadcasting?"
Answer: Yes! 1) Pad `(3, 4)` to `(1, 3, 4)`. 2) Right-to-left check: $4==4$, $1$ stretches to $3$, $5$ stretches to $1$. Output shape is `(5, 3, 4)`.

### 14. Summary
Broadcasting aligns trailing dimensions from right to left. Dimensions match if equal or if one is `1`.
