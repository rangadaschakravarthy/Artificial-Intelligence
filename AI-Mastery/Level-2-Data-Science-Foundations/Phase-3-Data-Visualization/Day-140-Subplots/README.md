# Day 140 — Subplots

## Learning Objectives
- Arrange multiple charts in multi-panel figure grids using `plt.subplots()`.
- Master GridSpec layout configurations with `plt.subplot2grid()` and `GridSpec`.
- Share axes scales across subplots using `sharex=True` and `sharey=True`.

## Prerequisites
- Day 134: Matplotlib Basics

## Topics Covered
- Creating multi-panel grids (`fig, axes = plt.subplots(rows, cols)`)
- Indexing 2D axes arrays (`axes[row, col]`)
- Sharing axes ranges with `sharex=True` and `sharey=True`
- Complex non-uniform layouts using `matplotlib.gridspec.GridSpec`
- Fixing title/label collisions using `fig.tight_layout()` and `fig.subplots_adjust()`

## Why This Matters
Executive dashboards and diagnostic reporting require presenting multiple complementary charts within a single organized figure.

## Practical Work
- Build a $2 	imes 2$ grid containing a Line Chart, Bar Chart, Histogram, and Scatter Plot.

## Difficulty
Intermediate
