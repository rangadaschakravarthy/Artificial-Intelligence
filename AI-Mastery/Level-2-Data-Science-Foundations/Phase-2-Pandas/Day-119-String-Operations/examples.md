# Day 119 Worked Examples: String Operations

## Example 1 — Beginner: Cleaning Casing & Whitespace
```python
import pandas as pd

raw_names = pd.Series(['  alice smith ', 'BOB JONES ', ' charlie BROWN '])

# Chain string methods: strip whitespace -> title case
clean_names = raw_names.str.strip().str.title()

print("Raw Names:
", raw_names)
print("
Cleaned Names:
", clean_names)
```

## Example 2 — Practical: String Replacement & Currency Cleaning
```python
import pandas as pd

prices = pd.Series(['$1,200.00', '$45.50', '$300.99', 'N/A'])

# Strip currency symbol and commas
clean_prices = (
    prices.str.replace('$', '', regex=False)
          .str.replace(',', '', regex=False)
)

# Convert to numeric
numeric_prices = pd.to_numeric(clean_prices, errors='coerce')

print("Clean Numeric Prices:
", numeric_prices)
```

## Example 3 — Intermediate: Splitting Full Names into First and Last Columns
```python
import pandas as pd

df = pd.DataFrame({
    'Full_Name': ['Alice Johnson', 'Bob Marley', 'Charlie Parker']
})

# Split by space into DataFrame columns
df[['First_Name', 'Last_Name']] = df['Full_Name'].str.split(' ', expand=True)

print("Split Name DataFrame:
", df)
```

## Example 4 — Real Dataset: Regex Pattern Extraction (Extracting Email Domains)
```python
import pandas as pd

df = pd.DataFrame({
    'User': ['U1', 'U2', 'U3'],
    'Email': ['alice123@gmail.com', 'bob_dev@yahoo.org', 'charlie@company.io']
})

# Extract domain name using Regex capture group
df['Domain'] = df['Email'].str.extract(r'@([\w\.]+)')

print("Extracted Domain DataFrame:
", df)
```

## Example 5 — AI/ML Application: Text Pattern Feature Engineering
```python
import pandas as pd

# Customer Feedback Comments
comments = pd.DataFrame({
    'Comment_ID': [101, 102, 103, 104],
    'Text': ['Great product, fast shipping!', 'Terrible service, broken item.', 'Okay quality.', 'Excellent support team!']
})

# Feature Engineering: Length of text and boolean flags
comments['Char_Count'] = comments['Text'].str.len()
comments['Word_Count'] = comments['Text'].str.split().str.len()
comments['Has_Great'] = comments['Text'].str.contains('great|excellent', case=False)

print("Text Feature Matrix:
", comments)
```
