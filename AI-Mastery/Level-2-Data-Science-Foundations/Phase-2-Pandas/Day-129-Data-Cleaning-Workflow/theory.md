# Day 129 Theory: Data Cleaning Workflow

### 1. What Is It?
A Data Cleaning Workflow is a systematic, sequential pipeline that transforms raw, unverified data into a validated, high-quality analytical dataset.

### 2. Why Does It Exist?
Ad-hoc cleaning leads to missed errors, silent bugs, and un-reproducible analysis. A structured workflow ensures quality control and pipeline reliability.

### 3. Intuition
Like refining crude oil into gasoline: crude data enters, debris/impurities are filtered out sequentially, structural specs are enforced, and clean fuel emerges.

### 4. Syntax (Modular Cleaning Function Pattern)
```python
def clean_pipeline(raw_df):
    df = raw_df.copy()
    # Step 1: Standardize Column Names
    df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')
    # Step 2: Remove Exact Duplicates
    df = df.drop_duplicates()
    # Step 3: Type Conversions
    df['price'] = df['price'].replace(r'[\$,]', '', regex=True).astype(float)
    # Step 4: Handle Missing Values
    df['category'] = df['category'].fillna('Unknown')
    return df
```

### 5. The 10-Step Data Cleaning Pipeline
1. **Raw Inspection**: Check `.info()`, `.shape`, `.head()`.
2. **Standardize Headers**: Convert column titles to lowercase snake_case.
3. **Deduplication**: Identify and drop duplicate records.
4. **Data Type Casting**: Convert numeric strings, dates, and categories to proper dtypes.
5. **String Cleaning**: Strip trailing whitespace, normalize case, remove special characters.
6. **Missing Value Treatment**: Impute or drop `NaN`s appropriately per column domain.
7. **Invalid Value Handling**: Correct impossible entries (e.g. `Age = -5` or `Score = 9999`).
8. **Outlier Auditing**: Identify extreme anomalies and determine domain validity.
9. **Derived Feature Validation**: Ensure calculated columns maintain internal mathematical consistency.
10. **Validation Assertions**: Run automated unit checks before exporting final dataset.

### 6. How It Works
The pipeline applies clean, idempotent transformation rules sequentially to input DataFrames, validating structural assumptions at each milestone.

### 7. Simple Example
```python
import pandas as pd
raw = pd.DataFrame({' Name ': [' Alice ', ' Alice '], ' Age ': ['25', '25']})
df = raw.copy()
df.columns = df.columns.str.strip()
df = df.drop_duplicates()
df['Age'] = df['Age'].astype(int)
print(df)
```

### 8. Intermediate Example
```python
import pandas as pd
raw = pd.DataFrame({
    'Cust_ID': [1, 1, 2, 3],
    'Spend': ['$100.50', '$100.50', '$250.00', 'INVALID'],
    'Date': ['2023-01-01', '2023-01-01', '2023-01-02', '2023-01-03']
})
# Pipeline
df = raw.drop_duplicates().copy()
df['Spend'] = pd.to_numeric(df['Spend'].str.replace('$', ''), errors='coerce')
df['Spend'].fillna(df['Spend'].median(), inplace=True)
print(df)
```

### 9. Output Interpretation
Produces a fully cleaned, correctly typed DataFrame with zero missing critical values, no duplicates, and validated data types.

### 10. Common Mistakes
- Modifying the original raw DataFrame in-place without creating a working copy.
- Applying data imputation steps before train/test splitting during ML preprocessing.

### 11. Data Science Connection
Essential prerequisite step before any Exploratory Data Analysis (EDA) or model training.

### 12. AI/ML Connection
Garbage In, Garbage Out (GIGO): ML models trained on dirty data produce biased, inaccurate predictions regardless of model complexity.

### 13. Interview Insight
Question: "How do you structure a production-grade data cleaning workflow?"
Answer: Encapsulate transformations into modular, functional pipelines with explicit logging and assertion validations at each step.

### 14. Summary
A structured 10-step cleaning workflow systematically standardizes headers, casts types, handles missing values/duplicates, and validates dataset integrity.
