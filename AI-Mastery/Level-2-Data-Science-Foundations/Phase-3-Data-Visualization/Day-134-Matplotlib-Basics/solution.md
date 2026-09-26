# Day 134 Solutions: Matplotlib Basics

## Level 1 — Basic
1. `Figure` object (top-level canvas container).
2. `Axes` object (individual subplot drawing area).
3. `ax.set_title('Title')`, `ax.set_xlabel('Label')`.
4. `figsize=(width, height)`.
5. Pass `bbox_inches='tight'` to `fig.savefig()`.

## Level 2 — Coding
1. `fig, ax = plt.subplots(figsize=(10, 5))`
2. `ax.plot([1,2,3], [2,4,6], color='red', linestyle='--')`
3. `ax.grid(True, alpha=0.4)`
4. `ax.set_ylim(0, 10)`
5. `fig.savefig('custom_plot.png', dpi=300, bbox_inches='tight')`

## Level 3 — Data Analysis
1.
```python
fig, ax = plt.subplots(figsize=(8, 4))
ax.plot(months, rev, label='Revenue', color='green')
ax.plot(months, prof, label='Profit', color='blue')
ax.set_title('Financial Performance')
ax.legend()
```

## Level 4 — Debugging
1. Stateful pyplot uses `plt.xlabel()`; OO API uses `ax.set_xlabel()`.

## Level 5 — AI/ML Application
1.
```python
fig, ax = plt.subplots(figsize=(7, 4))
ax.plot(epochs, train_acc, label='Train Acc', color='blue')
ax.plot(epochs, val_acc, label='Val Acc', color='orange')
ax.set_title('Training Progress')
ax.set_xlabel('Epoch')
ax.set_ylabel('Accuracy')
ax.legend()
```

## Level 6 — Interview Questions
1. The OO API explicitly attaches plotting calls to specific figure/axes handles, preventing global state mutation bugs when managing multi-panel figures.
