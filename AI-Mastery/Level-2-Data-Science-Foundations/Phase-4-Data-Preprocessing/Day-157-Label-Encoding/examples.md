# Day 157 Worked Examples: Label Encoding

## Example 1 — Practical: Explicit Ordinal Dictionary Mapping
```python
import pandas as pd

df = pd.DataFrame({
    'Education': ['High School', 'Bachelors', 'PhD', 'Masters', 'Bachelors'],
    'Performance': ['Needs Imp', 'Meets', 'Exceeds', 'Exceeds', 'Meets']
})

# Define explicit ordinal hierarchies
edu_map = {'High School': 0, 'Bachelors': 1, 'Masters': 2, 'PhD': 3}
perf_map = {'Needs Imp': 0, 'Meets': 1, 'Exceeds': 2}

df['Edu_Ordinal'] = df['Education'].map(edu_map)
df['Perf_Ordinal'] = df['Performance'].map(perf_map)

print("Explicitly Ordinal Encoded DataFrame:
", df)
```
