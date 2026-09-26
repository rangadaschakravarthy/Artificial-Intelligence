# Day 94 Theory: Boolean and Fancy Indexing

### 1. What Is It?
- **Boolean Indexing**: Selecting array elements where a boolean mask condition evaluates to `True`.
- **Fancy Indexing**: Passing an array or list of integer indices to select elements in custom, non-contiguous order.

### 2. Why Does It Exist?
Slicing can only extract contiguous or fixed-step patterns. Boolean and Fancy indexing allow arbitrary, conditional, and non-contiguous data selection.

### 3. Intuition
- Boolean indexing is like applying a custom filter search in Excel (e.g., "Show rows where Income > 50k").
- Fancy indexing is like handing a librarian a specific list of page numbers `[3, 12, 45, 99]` to pull out.

### 4. Syntax
```python
import numpy as np

arr = np.array([10, 25, 30, 45, 50])

# Boolean Indexing
mask = arr > 30
filtered = arr[mask] # [45, 50]

# Bitwise combination
combined = arr[(arr > 20) & (arr < 50)] # [25, 30, 45]

# Fancy Indexing
fancy = arr[[0, 3, 4]] # [10, 45, 50]
```

### 5. Parameters
- `mask`: Boolean array of identical shape (or broadcastable shape).
- `indices`: Integer array/list specifying index locations.

### 6. How It Works
Unlike slicing (which creates a metadata view over existing memory), Fancy and Boolean indexing construct a **brand new memory copy** containing the selected elements.

### 7. Simple Example
```python
import numpy as np
a = np.array([1, -2, 3, -4, 5])
a[a < 0] = 0 # Replace negative numbers with zero!
print(a) # [1, 0, 3, 0, 5]
```

### 8. Intermediate Example
```python
import numpy as np
m = np.arange(12).reshape(4, 3)
# Select rows 0 and 3, columns 1 and 2
sub = m[[0, 3], :][:, [1, 2]]
print("Selected Rows & Cols:
", sub)
```

### 9. Output Interpretation
`m[[0, 3], :]` extracts rows 0 and 3. `[:, [1, 2]]` selects columns 1 and 2 from those rows.

### 10. Common Mistakes
- Using Python keywords `and` / `or` instead of element-wise operators `&` / `|`.
- Forgetting parentheses around conditions (`arr > 10 & arr < 20` fails due to operator precedence; must write `(arr > 10) & (arr < 20)`!).

### 11. Data Science Connection
Pandas conditional querying (`df[df['age'] > 30]`) is built directly on NumPy boolean masking.

### 12. AI/ML Connection
Selecting positive training samples $y == 1$, removing outliers beyond 3 standard deviations, and applying ReLU activations $\max(0, x)$.

### 13. Interview Insight
Question: "Does boolean indexing return a view or a copy?"
Answer: Boolean and Fancy indexing always return a **memory copy**, whereas slicing returns a view. Modifying a boolean-indexed array does not alter the original array unless assigned directly (`arr[mask] = val`).

### 14. Summary
Use boolean masks with `&`, `|`, `~` for conditional filtering. Use integer index arrays for custom non-contiguous selection. Both return copies.
