# Day 169 — Train-Test Concept

## Learning Objectives
- Understand dataset partitioning into Train, Validation, and Test sets.
- Master `sklearn.model_selection.train_test_split` with `stratify` and `random_state`.
- Enforce strict isolation boundaries between training metrics and unseen validation data.

## Prerequisites
- Day 168: Data Leakage

## Topics Covered
- Dataset Partitions: Training Set (60-80%), Validation Set (10-20%), Test Set (10-20%)
- `train_test_split()` parameters: `test_size`, `random_state`, `stratify`
- Stratified Splitting for imbalanced classification targets (`stratify=y`)
- Time-series temporal splitting vs random shuffling
- Fitting vs Transforming boundaries

## Practical Work
- Perform a stratified 80/20 train/test split on an imbalanced target dataset.

## Difficulty
Intermediate
