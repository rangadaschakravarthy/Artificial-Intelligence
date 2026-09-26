# Day 138 — Scatter Plots

## Learning Objectives
- Evaluate bivariate relationships and correlation between continuous variables using `ax.scatter()`.
- Encode third and fourth dimensions using point size (Bubble Charts) and color mapping.
- Overlay trendlines and regression lines.

## Prerequisites
- Day 134: Matplotlib Basics
- Day 130: Exploratory Data Analysis

## Topics Covered
- `ax.scatter()` parameters: `c` (color array), `s` (size array), `cmap`, `alpha`
- Bubble charts (3D continuous representation via size)
- Adding colormaps and colorbars (`fig.colorbar()`)
- Overlaying linear trendlines (`np.polyfit()`)
- Identifying clusters, outliers, and non-linear patterns

## Why This Matters
Scatter plots are the primary diagnostic tool for inspecting pairwise feature correlation and identifying non-linear data structures.

## Practical Work
- Build a bubble chart mapping Salary vs Experience, with Bubble Size = Performance Rating and Color = Age.

## Difficulty
Intermediate
