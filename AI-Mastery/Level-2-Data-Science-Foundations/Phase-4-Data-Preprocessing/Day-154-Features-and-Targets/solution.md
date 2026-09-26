# Day 154 Solutions: Features and Targets

## Level 1 — Basic
1. $N 	imes d$ matrix ($N$ rows, $d$ columns).
2. Regression predicts a continuous numerical target. Classification predicts a discrete categorical class label.
3. Nominal categories have no natural mathematical ordering (e.g. Red, Green). Ordinal categories have a meaningful sequential ranking (e.g. Low, Medium, High).

## Level 2 — Coding
1.
```python
cat_cols = df.select_dtypes(include=['object', 'category']).columns.tolist()
num_cols = df.select_dtypes(include=['float64', 'int64']).columns.tolist()
```

## Level 3 — Data Analysis
1. Scaling target vector $y$ along with features distorts the real-world scale of target predictions. If $y$ is scaled during training, model predictions must be inverse-transformed back to original target units for evaluation.
