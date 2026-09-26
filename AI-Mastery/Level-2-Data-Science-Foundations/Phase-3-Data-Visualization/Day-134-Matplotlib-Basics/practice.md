# Day 134 Practice Questions: Matplotlib Basics

## Level 1 — Basic
1. What does `fig` represent in `fig, ax = plt.subplots()`?
2. What does `ax` represent?
3. How do you set title and x-axis label using the OO API?
4. What parameter controls figure dimensions in `plt.subplots()`?
5. How do you prevent cropped legend labels when saving a figure?

## Level 2 — Coding
1. Create a figure of size `(10, 5)` using `plt.subplots()`.
2. Plot `x = [1,2,3]` vs `y = [2,4,6]` with a dashed red line.
3. Add gridlines with `alpha=0.4`.
4. Set y-axis limits between `0` and `10`.
5. Save figure as `'custom_plot.png'` with `dpi=300`.

## Level 3 — Data Analysis
1. Build a multi-metric financial chart comparing Revenue and Profit lines.

## Level 4 — Debugging
1. Fix error: `AttributeError: 'AxesSubplot' object has no attribute 'xlabel'` (Use `.set_xlabel()` instead of `.xlabel()`!).

## Level 5 — AI/ML Application
1. Plot train vs validation accuracy curves over 20 epochs using the OO API.

## Level 6 — Interview Questions
1. Why is the Object-Oriented interface preferred over stateful pyplot in production code?
