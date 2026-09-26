# Day 149 Solutions: Visualization Selection

## Level 1 — Basic
1. Line Chart.
2. Scatter Plot or Correlation Heatmap.
3. 3D perspective distorts wedge angles and areas, making visual comparison of proportions visually inaccurate.

## Level 2 — Coding
1. Objective: 1D Distribution -> Histogram with KDE (`sns.histplot(scores, kde=True)`).

## Level 3 — Data Analysis
1. Line charts connect adjacent data points with lines, implying continuous interpolation between points. Unordered categorical variables have no continuous sequence, so connecting them with lines creates false trend artifacts.
