# Day 156 Worked Examples: Encoding

## Example 1 — Practical: Custom Frequency Encoder Implementation
```python
import pandas as pd

def frequency_encode(df, col_name):
    # Compute relative frequency proportion
    freq_map = df[col_name].value_counts(normalize=True).to_dict()
    return df[col_name].map(freq_map)

df = pd.DataFrame({'City': ['NY', 'SF', 'NY', 'LA', 'NY', 'SF']})
df['City_Freq'] = frequency_encode(df, 'City')
print("Frequency Encoded DataFrame:
", df)
```
