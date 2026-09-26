# Day 134 Worked Examples: Matplotlib Basics

## Example 1 — Beginner: OO Interface Line Plot
```python
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(6, 4))
ax.plot([1, 2, 3, 4], [10, 25, 20, 35], color='green', marker='s')
ax.set_title("OO Line Plot")
ax.set_xlabel("Time Step")
ax.set_ylabel("Value")
fig.savefig("oo_basic.png")
plt.close(fig)
print("Saved oo_basic.png")
```

## Example 2 — Practical: Multi-Series OO Customization
```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 50)
y1 = np.sin(x)
y2 = np.cos(x)

fig, ax = plt.subplots(figsize=(8, 4))
ax.plot(x, y1, label='Sin(x)', color='blue', linewidth=2)
ax.plot(x, y2, label='Cos(x)', color='red', linestyle='--')

ax.set_title("Trigonometric Functions")
ax.set_xlabel("X (radians)")
ax.set_ylabel("Amplitude")
ax.set_ylim(-1.5, 1.5)
ax.grid(True, linestyle=':', alpha=0.6)
ax.legend(loc='upper right')

fig.savefig("trig_plot.png", bbox_inches='tight')
plt.close(fig)
print("Saved trig_plot.png")
```
