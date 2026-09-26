# Day 146 — Seaborn Heatmaps

## Learning Objectives
- Visualize 2D correlation matrices and cross-tabulation tables using `sns.heatmap()`.
- Display hierarchical clustering heatmaps with dendrograms using `sns.clustermap()`.
- Customize annotations, numeric formatting, colormaps, and mask upper/lower triangles.

## Prerequisites
- Day 126: Pivot Tables
- Day 130: Exploratory Data Analysis
- Day 142: Seaborn Introduction

## Topics Covered
- `sns.heatmap()` syntax and parameters: `annot`, `fmt`, `cmap`, `linewidths`, `cbar`
- Masking correlation upper triangles (`np.triu()`)
- Diverging colormaps (`'coolwarm'`, `'vlag'`) vs Sequential colormaps (`'Blues'`, `'viridis'`)
- Hierarchical clustering with `sns.clustermap()`
- Visualizing DataFrame correlation matrices `df.corr()`

## Why This Matters
Heatmaps are the standard visualization tool for detecting feature collinearity and presenting pivot table matrices.

## Practical Work
- Plot a masked Pearson correlation heatmap showing correlation values formatted to 2 decimal places.

## Difficulty
Intermediate
