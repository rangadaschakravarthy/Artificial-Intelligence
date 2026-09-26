# Day 142 Theory: Seaborn Introduction

### 1. What Is It?
Seaborn is a Python statistical data visualization library based on Matplotlib, providing a high-level declarative interface for drawing attractive statistical graphics natively from Pandas DataFrames.

### 2. Core Concepts
- **`hue`**: Splits plots into colored sub-groups based on a categorical column.
- **`style` / `size`**: Maps categories to line markers or point dimensions.
- **`palette`**: Applies harmonious color schemes (qualitative, sequential, or diverging).

### 3. Syntax
```python
import seaborn as sns
sns.set_theme(style='whitegrid', palette='deep')
sns.scatterplot(data=df, x='Age', y='Salary', hue='Department', style='Gender')
```

### 4. Summary
Seaborn simplifies statistical plotting by mapping Pandas columns directly to visual channels (`hue`, `style`, `size`).
