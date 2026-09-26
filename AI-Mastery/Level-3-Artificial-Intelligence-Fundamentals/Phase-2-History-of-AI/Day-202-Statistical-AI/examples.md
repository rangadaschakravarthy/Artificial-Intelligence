# Day 202 Worked Examples: Statistical AI

## Example 1 — Practical: Medical Bayes Inference
```python
# P(Disease) = 0.01, P(Test+ | Disease) = 0.99, P(Test+ | No Disease) = 0.05
p_d = 0.01
p_pos_d = 0.99
p_pos_nod = 0.05

p_pos = (p_pos_d * p_d) + (p_pos_nod * (1 - p_d))
p_d_pos = (p_pos_d * p_d) / p_pos

print(f"Posterior Probability P(Disease | Test+): {p_d_pos:.4f}") # ~16.6%
```
