# Day 157 Solutions: Label Encoding

## Level 1 — Basic
1. Ordinal Categorical data (data with intrinsic sequential ranking).
2. The error introduced when linear models treat arbitrary integer codes assigned to nominal categories as meaningful mathematical magnitudes.
3. `OrdinalEncoder` (designed for 2D feature matrices $X$; `LabelEncoder` is intended for 1D target vector $y$).

## Level 2 — Coding
1. `df['Risk_Code'] = df['Risk_Level'].map({'Low': 0, 'Medium': 1, 'High': 2})`

## Level 3 — Data Analysis
1. Decision trees evaluate threshold splits ($x_i \ge c$) partitioning feature space along axis planes. Integer encoding allows trees to isolate individual category codes via sequential splits without relying on continuous linear distance metrics.
