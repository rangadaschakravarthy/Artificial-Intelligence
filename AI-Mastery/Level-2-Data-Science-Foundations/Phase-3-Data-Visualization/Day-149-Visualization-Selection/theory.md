# Day 149 Theory: Visualization Selection

### 1. What Is It?
Visualization Selection is the systematic process of matching analytical questions and data structures to the most effective graphical format.

### 2. Decision Framework Matrix
| Objective | Variable Types | Optimal Chart Type | Alternative |
|---|---|---|---|
| **Trend over Time** | Time + Continuous | Line Chart (`ax.plot`) | Area Chart |
| **Comparison** | Categorical + Continuous | Bar Chart (`ax.bar`) | Lollipop Chart |
| **Distribution** | 1 Continuous | Histogram / KDE (`sns.histplot`) | Box Plot |
| **Group Comparison** | Cat + Continuous | Box Plot / Violin Plot | Swarm Plot |
| **Relationship** | 2 Continuous | Scatter Plot (`ax.scatter`) | Bubble Chart |
| **Correlation Matrix**| Multi-Continuous | Heatmap (`sns.heatmap`) | Pair Plot |
| **Composition** | Categorical Parts of Whole | Stacked Bar | Treemap |

### 3. Summary
Match visualization types strictly to analytical goals: Line for trend, Bar for comparison, Histogram/Boxplot for distribution, Scatter/Heatmap for relationship.
