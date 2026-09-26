# Day 167 — Correlation-Based Selection

## Learning Objectives
- Identify and eliminate multi-collinear feature pairs using correlation matrices.
- Master feature-to-target correlation ranking for feature selection.
- Implement automated Python functions that prune redundant features exceeding a correlation threshold ($|r| > 0.85$).

## Prerequisites
- Day 130: Exploratory Data Analysis
- Day 166: Feature Selection

## Topics Covered
- Multi-collinearity definition and consequences
- Pearson vs Spearman correlation matrices for selection
- Automated upper-triangle correlation pruning algorithms
- Feature-to-target correlation sorting
- Mutual Information score selection (`SelectKBest`, `mutual_info_classif`)

## Practical Work
- Write a function that automatically drops one column from every pair of features exhibiting Pearson $|r| > 0.85$.

## Difficulty
Intermediate
