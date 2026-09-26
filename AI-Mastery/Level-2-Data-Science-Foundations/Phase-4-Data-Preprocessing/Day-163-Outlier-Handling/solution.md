# Day 163 Solutions: Outlier Handling

## Level 1 — Basic
1. Capping extreme values beyond specified percentiles (e.g. 1st and 99th) to maximum acceptable boundary values.
2. `df['col'].clip()`.
3. Trimming deletes entire observation rows, causing loss of sample size and potential selection bias.

## Level 2 — Coding
1.
```python
q_low = df['Spend'].quantile(0.01)
q_high = df['Spend'].quantile(0.99)
df['Spend_Capped'] = df['Spend'].clip(lower=q_low, upper=q_high)
```

## Level 3 — Data Analysis
1. Deleting rows reduces sample size $N$, decreasing statistical power. Capping preserves row sample size while mitigating extreme variance distortion.
