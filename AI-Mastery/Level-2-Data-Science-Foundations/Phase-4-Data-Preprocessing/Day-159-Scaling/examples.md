# Day 159 Worked Examples: Scaling

## Example 1 — Practical: Euclidean Distance Sensitivity Comparison
```python
import numpy as np

# Unscaled: Person A (Age 25, Income $50,000), Person B (Age 26, Income $50,000), Person C (Age 25, Income $80,000)
pA = np.array([25, 50000])
pB = np.array([26, 50000])
pC = np.array([25, 80000])

# Distance A to B (1 yr age diff):
dist_AB = np.linalg.norm(pA - pB) # 1.0
# Distance A to C ($30,000 income diff):
dist_AC = np.linalg.norm(pA - pC) # 30000.0

print("Unscaled Distance A to B (1 yr age diff):   ", dist_AB)
print("Unscaled Distance A to C ($30k income diff):", dist_AC)
# Income scale completely drowns out age differences!
```
