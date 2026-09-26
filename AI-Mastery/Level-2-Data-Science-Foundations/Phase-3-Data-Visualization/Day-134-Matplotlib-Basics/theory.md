# Day 134 Theory: Matplotlib Basics

### 1. What Is It?
Matplotlib's Object-Oriented (OO) API provides explicit figure handle management through two primary classes: `Figure` (top-level canvas container) and `Axes` (individual subplot area containing axis lines, ticks, labels, and plots).

### 2. Why Does It Exist?
Stateful `plt.plot()` works for simple 1-line plots but becomes messy and error-prone when building multi-chart layouts. The OO API explicitly scopes styling commands to designated `Axes` handles.

### 3. Architecture
```
Figure (Entire Page Container)
└── Axes (Individual Subplot Canvas)
    ├── Axis (X-Axis & Y-Axis lines)
    │   ├── Ticks (Major & Minor tick marks)
    │   └── Labels (Axis text titles)
    ├── Title
    ├── Legend
    └── Spines (Outer bounding box frames)
```

### 4. Syntax
```python
fig, ax = plt.subplots(figsize=(8, 5), dpi=100)
ax.plot(x, y, color='navy', linestyle='--', label='Trend')
ax.set_title("Title Text", fontsize=14)
ax.set_xlabel("X Label")
ax.set_ylabel("Y Label")
ax.grid(True, alpha=0.3)
ax.legend(loc='upper right')
fig.savefig("output.png", bbox_inches='tight')
plt.close(fig)
```

### 5. Summary
The OO API (`fig, ax`) provides robust control over Matplotlib figures and subplots.
