# Day 110 Theory: Loading Datasets

### 1. What Is It?
Pandas dataset loading functions (`read_csv`, `read_excel`, `read_json`) read external data files from disk or URLs and parse them into structured `DataFrame` objects.

### 2. Why Does It Exist?
Data is stored in diverse formats (CSVs, TSVs, Excel workbooks, JSON payloads). Automated C-parsers parse text strings into typed numeric arrays automatically.

### 3. Intuition
`read_csv` is like an automated data importer that opens a text file, splits lines by commas, detects column headers, converts numbers to floats/ints, and packages everything into an Excel-like DataFrame.

### 4. Syntax
```python
import pandas as pd

# Basic CSV Read
df = pd.read_csv('data.csv')

# Advanced CSV Read with parameters
df = pd.read_csv(
    'data.csv',
    sep=',',
    header=0,
    usecols=['Age', 'Income'],
    dtype={'Age': 'int32'},
    na_values=['MISSING', '-999']
)
```

### 5. Parameters
- `filepath_or_buffer`: File path string or URL.
- `sep` / `delimiter`: Character separator (default `','`).
- `header`: Row index to use as column names (default `0`).
- `usecols`: List of column names to load (saves memory!).
- `na_values`: Strings to recognize as `NaN`.
- `chunksize`: Number of rows to yield per iteration chunk.

### 6. How It Works
Pandas uses an optimized C-parser (`engine='c'`) to read raw file bytes, tokenize lines using delimiter specifications, infer dtypes, and allocate underlying NumPy blocks.

### 7. Simple Example
```python
import pandas as pd
import io

csv_data = "Name,Age\nAlice,25\nBob,30"
df = pd.read_csv(io.StringIO(csv_data))
print(df)
```

### 8. Intermediate Example
```python
import pandas as pd
import io

csv_data = "ID|Val\n101|-999\n102|50"
df = pd.read_csv(io.StringIO(csv_data), sep='|', na_values=['-999'])
print(df) # -999 parsed as NaN!
```

### 9. Output Interpretation
`na_values=['-999']` instructs the parser to treat string `'-999'` as missing value `NaN`.

### 10. Common Mistakes
- Trying to read tab-separated TSV files using default comma `sep=','` (Use `sep='\t'`).
- Loading massive 10GB CSV files without specifying `usecols` or `chunksize`, causing memory overflow.

### 11. Data Science Connection
The initial step in every data science and Machine Learning project.

### 12. AI/ML Connection
Loading training datasets $X, y$ from CSV storage into DataFrames before feature preprocessing.

### 13. Interview Insight
Question: "How do you load a 20GB CSV file on a laptop with only 8GB of RAM using Pandas?"
Answer: Use the `chunksize` parameter in `pd.read_csv('file.csv', chunksize=10000)`. It returns an iterable reader yielding 10,000-row DataFrame chunks at a time, allowing processing without crashing system RAM.

### 14. Summary
Pandas provides robust file parsers (`read_csv`). Use `usecols`, `na_values`, and `chunksize` to optimize memory and data parsing quality.
