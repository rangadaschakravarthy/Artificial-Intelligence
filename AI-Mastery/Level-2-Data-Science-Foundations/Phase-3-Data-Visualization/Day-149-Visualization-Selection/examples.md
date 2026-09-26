# Day 149 Worked Examples: Visualization Selection

## Example 1 — Practical: Selecting & Generating Correct Chart
```python
# Question: "Compare median salary across 5 company departments"
# Objective: Categorical Comparison -> Horizontal Bar Chart
import matplotlib.pyplot as plt

depts = ['Engineering', 'Sales', 'Product', 'Marketing', 'HR']
median_salary = [110, 85, 95, 75, 65]

fig, ax = plt.subplots(figsize=(8, 4))
bars = ax.barh(depts, median_salary, color='steelblue')
ax.set_title("Median Salary by Department (Optimal Choice)")
ax.set_xlabel("Salary ($K)")
ax.bar_label(bars, fmt='$%dK', padding=3)

fig.savefig("correct_chart_selection.png", bbox_inches='tight')
plt.close(fig)
print("Saved correct_chart_selection.png")
```
