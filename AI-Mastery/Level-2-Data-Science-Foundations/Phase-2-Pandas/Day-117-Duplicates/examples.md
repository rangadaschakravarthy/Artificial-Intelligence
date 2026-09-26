# Day 117 Worked Examples: Duplicates

## Example 1 — Beginner: Detecting & Dropping Exact Row Duplicates
```python
import pandas as pd

df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Alice', 'Charlie', 'Bob'],
    'Age': [25, 30, 25, 35, 30]
})

print("Duplicate Mask (df.duplicated()):
", df.duplicated())
print("
Total Duplicate Rows Count:", df.duplicated().sum())

# Drop exact duplicates (keeps first occurrence by default)
df_clean = df.drop_duplicates()
print("
Deduplicated DataFrame:
", df_clean)
```

## Example 2 — Practical: Deduplicating by Column Subset (keep='first' vs 'last')
```python
import pandas as pd

# Transaction Log where User_ID 101 has multiple transactions
df = pd.DataFrame({
    'User_ID': [101, 101, 102, 103, 101],
    'Status': ['Pending', 'Approved', 'Approved', 'Pending', 'Refunded'],
    'Timestamp': ['10:00', '10:05', '10:10', '10:15', '10:30']
})

# Keep FIRST transaction per User_ID
df_first = df.drop_duplicates(subset=['User_ID'], keep='first')

# Keep LAST (latest) transaction per User_ID
df_last = df.drop_duplicates(subset=['User_ID'], keep='last')

print("Keep FIRST Transaction per User:
", df_first)
print("
Keep LAST Transaction per User:
", df_last)
```

## Example 3 — Intermediate: Dropping ALL Duplicates (keep=False)
```python
import pandas as pd

df = pd.DataFrame({
    'Item': ['A', 'B', 'B', 'C', 'D', 'D'],
    'Price': [10, 20, 20, 30, 40, 40]
})

# keep=False removes B and D completely!
df_unique_only = df.drop_duplicates(keep=False)

print("Original DataFrame:
", df)
print("
Only Non-Repeated Unique Items (keep=False):
", df_unique_only)
```

## Example 4 — Real Dataset: Auditing Primary Key Uniqueness
```python
import pandas as pd

users = pd.DataFrame({
    'Email': ['alice@gmail.com', 'bob@yahoo.com', 'alice@gmail.com', 'david@corp.org'],
    'Signup_Date': ['2026-01-01', '2026-01-02', '2026-01-03', '2026-01-04']
})

is_unique = users['Email'].is_unique
print("Is Email Column Unique?", is_unique)

if not is_unique:
    duplicate_emails = users[users['Email'].duplicated(keep=False)]
    print("
Duplicate Email Records Found:
", duplicate_emails)
```

## Example 5 — AI/ML Application: Preventing Train-Test Data Leakage via Deduplication
```python
import pandas as pd

# Combined Dataset prior to split
dataset = pd.DataFrame({
    'Feature_1': [1.0, 2.0, 3.0, 1.0, 4.0],
    'Feature_2': [10.0, 20.0, 30.0, 10.0, 40.0],
    'Target': [0, 1, 0, 0, 1]
})

# Deduplicate dataset before train/test split to prevent identical rows in both splits
clean_dataset = dataset.drop_duplicates().reset_index(drop=True)

print("Original Dataset Length: ", len(dataset))
print("Deduplicated Length:    ", len(clean_dataset))
```
