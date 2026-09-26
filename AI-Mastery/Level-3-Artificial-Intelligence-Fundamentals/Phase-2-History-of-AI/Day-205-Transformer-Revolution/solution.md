# Day 205 Solutions: Transformer Revolution

## Level 1 — Basic
1. *Attention Is All You Need* (Vaswani et al., 2017).
2. Sequential processing. RNNs process tokens one by one ($O(N)$ sequential steps), blocking GPU parallelization. Transformers compute self-attention over all tokens in parallel.
