# Day 169 Solutions: Train-Test Concept

## Level 1 — Basic
1. 70% to 80%.
2. Reproducibility (ensures identical pseudo-random row partitions on every run).
3. It guarantees that training and test splits retain the exact same percentage proportion of target class labels as the original dataset.

## Level 2 — Coding
1. `X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=42, stratify=y)`

## Level 3 — Data Analysis
1. Time-series data exhibits temporal dependency (autocorrelation). Random shuffling leaks future data points into past training sets, destroying the temporal ordering required for real-world forecasting.
