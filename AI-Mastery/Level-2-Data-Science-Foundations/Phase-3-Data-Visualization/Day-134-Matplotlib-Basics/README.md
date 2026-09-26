# Day 134 — Matplotlib Basics

## Learning Objectives
- Master the Matplotlib Object-Oriented interface (`fig, ax = plt.subplots()`).
- Understand Figure vs Axes containers.
- Customize titles, labels, legends, ticks, and figure dimensions.

## Prerequisites
- Day 133: Introduction to Data Visualization

## Topics Covered
- Stateful Pyplot API (`plt.plot()`) vs Object-Oriented API (`fig, ax`)
- Understanding `Figure` (the window/page) and `Axes` (the plot canvas)
- Creating subplots using `plt.subplots()`
- Controlling figure size (`figsize=(w, h)`) and DPI (`dpi=100`)
- Setting titles (`ax.set_title()`), labels (`ax.set_xlabel()`), limits (`ax.set_xlim()`)
- Adding gridlines, legends, and saving figures with `plt.savefig()`

## Why This Matters
The Object-Oriented interface is essential for building complex multi-panel figure layouts and custom visualizations in Python.

## Real-World Usage
Generating multi-panel publication figures for academic papers and production report graphics.

## Study Order
1. Read `theory.md` for Figure/Axes architecture.
2. Review `examples.md` for OO API code.
3. Run `code.py` to generate sample plots.
4. Complete `practice.md` and check `solution.md`.

## Practical Work
- Build a multi-line plot using `fig, ax = plt.subplots()`.

## Interview Preparation
- What is the difference between `plt.plot()` and `ax.plot()`?

## Completion Checklist
- [ ] I understand Figure vs Axes objects.
- [ ] I can use `fig, ax = plt.subplots()`.
- [ ] I can customize plot titles, labels, grids, and legends.
- [ ] I can save plots at custom DPI resolutions.

## Difficulty
Intermediate
