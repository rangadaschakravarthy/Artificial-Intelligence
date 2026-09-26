# Day 110 Worked Examples: Loading Datasets

## Example 1 — Beginner: Reading CSV with Custom Parameters
```python
import pandas as pd
import io

# Simulated CSV content with missing value indicator 'N/A'
csv_text = "ID;Name;Salary\n1;Alice;70000\n2;Bob;N/A\n3;Charlie;95000"

df = pd.read_csv(
    io.StringIO(csv_text),
    sep=';',
    na_values=['N/A']
)

print("Parsed DataFrame:
", df)
print("
Missing Value Count:
", df.isna().sum())
```

## Example 2 — Practical: Selecting Column Subsets with usecols
```python
import pandas as pd
import io

csv_text = "ColA,ColB,ColC,ColD\n1,2,3,4\n5,6,7,8"

# Load only ColA and ColC to save RAM memory
df = pd.read_csv(io.StringIO(csv_text), usecols=['ColA', 'ColC'])
print("Loaded Subset DataFrame:
", df)
```

## Example 3 — Intermediate: Chunked Reading for Large Files
```python
import pandas as pd
import io

# Simulated 6-row CSV file
csv_text = "Val\n10\n20\n30\n40\n50\n60"

# Read in chunks of 2 rows at a time
total_sum = 0
for chunk in pd.read_csv(io.StringIO(csv_text), chunksize=2):
    total_sum += chunk['Val'].sum()
    print("Processed Chunk of shape:", chunk.shape)

print("Total Sum across all chunks:", total_sum)
```

## Example 4 — Real Dataset: Parsing JSON Payloads
```python
import pandas as pd
import io

json_text = '[{"User": "U1", "Score": 85, "Active": true}, {"User": "U2", "Score": 92, "Active": false}]'

df_json = pd.read_json(io.StringIO(json_text))
print("Parsed JSON DataFrame:
", df_json)
print("Data Types:
", df_json.dtypes)
```

## Example 5 — AI/ML Application: Specifying Explicit Feature dtypes during Loading
```python
import pandas as pd
import io

csv_text = "Age,Income,Default\n25,50000.0,0\n40,85000.0,0\n35,62000.0,1"

# Specify float32 dtypes directly during load for ML training
dtype_dict = {'Age': 'int32', 'Income': 'float32', 'Default': 'int8'}

df_ml = pd.read_csv(io.StringIO(csv_text), dtype=dtype_dict)
print("ML Pre-typed DataFrame Dtypes:
", df_ml.dtypes)
```
