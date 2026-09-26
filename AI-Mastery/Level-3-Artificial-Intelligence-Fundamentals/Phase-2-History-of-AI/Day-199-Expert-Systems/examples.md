# Day 199 Worked Examples: Expert Systems

## Example 1 — Practical: MYCIN Certainty Factor Combination
```python
def combine_certainty_factors(cf1, cf2):
    if cf1 > 0 and cf2 > 0:
        return cf1 + cf2 * (1 - cf1)
    return cf1 + cf2

r1_cf = 0.7
r2_cf = 0.5
combined = combine_certainty_factors(r1_cf, r2_cf)
print(f"Combined Certainty Factor: {combined:.2f}") # 0.85
```
