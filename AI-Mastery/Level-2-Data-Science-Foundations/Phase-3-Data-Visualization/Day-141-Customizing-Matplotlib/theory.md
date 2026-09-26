# Day 141 Theory: Customizing Matplotlib

### 1. What Is It?
Matplotlib customization controls figure styling using global `rcParams` dictionaries, built-in stylesheet presets, and targeted annotation tools.

### 2. Key Syntax
```python
# Style Sheets:
plt.style.use('ggplot')

# Custom rcParams:
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['axes.edgecolor'] = '#333333'

# Text Annotations:
ax.annotate('Peak Value', xy=(x_peak, y_peak), xytext=(x_text, y_text),
            arrowprops=dict(facecolor='black', shrink=0.05))
```

### 3. Summary
`plt.style.use()` updates theme aesthetics globally, while `ax.annotate()` adds precise explanatory callout text.
