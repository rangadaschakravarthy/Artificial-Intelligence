# Day 141 Worked Examples: Customizing Matplotlib

## Example 1 — Practical: Custom Style & Point Annotations
```python
import matplotlib.pyplot as plt
import numpy as np

plt.style.use('seaborn-v0_8-whitegrid')
x = np.linspace(0, 10, 100)
y = np.sin(x)

fig, ax = plt.subplots(figsize=(8, 4))
ax.plot(x, y, color='navy', linewidth=2, label='Signal')

# Peak Annotation
max_idx = np.argmax(y)
ax.annotate('Peak Max', xy=(x[max_idx], y[max_idx]),
            xytext=(x[max_idx] + 1, y[max_idx] + 0.2),
            arrowprops=dict(facecolor='red', shrink=0.05, width=1, headwidth=6))

ax.set_title("Annotated Signal Plot")
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

fig.savefig("custom_annotation.png", bbox_inches='tight')
plt.close(fig)
print("Saved custom_annotation.png")
```
