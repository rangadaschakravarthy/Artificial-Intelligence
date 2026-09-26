# Day 162 — Outlier Detection

## Learning Objectives
- Identify statistical outliers using IQR (Interquartile Range) and Z-Score threshold methods.
- Distinguish between genuine extreme observations and erroneous data entry corruptions.
- Visualize outliers using Box plots and Scatter plots.

## Prerequisites
- Day 115: Outliers (Level 1 Statistics)
- Day 139: Box Plots
- Day 161: Standardization

## Topics Covered
- What is an Outlier? (Definition & Causes)
- Interquartile Range (IQR) Rule: $[	ext{Q1} - 1.5	ext{IQR}, 	ext{Q3} + 1.5	ext{IQR}]$
- Z-Score Threshold Rule ($|Z| > 3.0$)
- Percentile Bounds Rule (e.g. 1st and 99th percentiles)
- Genuine vs Erroneous Outliers (Domain Knowledge rule)

## Practical Work
- Write an outlier detection function returning boolean masks using both IQR and Z-score criteria.

## Difficulty
Intermediate
