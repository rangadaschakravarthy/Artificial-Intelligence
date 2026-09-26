# Day 141 Solutions: Customizing Matplotlib

## Level 1 — Basic
1. `plt.style.available`.
2. `ax.annotate()`.
3. `ax.spines['top'].set_visible(False)` and `ax.spines['right'].set_visible(False)`.

## Level 2 — Coding
1. `plt.style.use('dark_background')`
2. `ax.annotate('Outlier', xy=(5, 100), xytext=(6, 110), arrowprops=dict(facecolor='red'))`

## Level 3 — Data Analysis
1. Tufte's Data-to-Ink principle states that non-data ink (heavy borders, unnecessary lines) distracts viewers. Removing spines maximizes focus on data trends.
