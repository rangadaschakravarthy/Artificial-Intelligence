# Day 205 Worked Examples: Transformer Revolution

## Example 1 — Practical: Self-Attention Matrix Dimensions Simulation
```python
import numpy as np

# Sequence length = 4 tokens, Embedding dim d_k = 8
seq_len = 4
d_k = 8

Q = np.random.randn(seq_len, d_k)
K = np.random.randn(seq_len, d_k)
V = np.random.randn(seq_len, d_k)

# Compute Raw Attention Scores: (Q @ K.T) / sqrt(d_k)
scores = (Q @ K.T) / np.sqrt(d_k)
print("Attention Score Matrix Shape (Seq x Seq):
", scores.shape) # (4, 4)
```
