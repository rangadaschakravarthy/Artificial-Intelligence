# Day 132 Theory: Pandas Mini Project Architecture

### 1. What Is It?
The Pandas Mini Project is a comprehensive capstone workflow integrating dataset loading, cleaning, EDA, aggregation, reshaping, time series analysis, and ML feature preparation.

### 2. Why Does It Exist?
Mastering individual functions (`.groupby()`, `.fillna()`, `pd.merge()`) is insufficient. Real-world data science requires chaining these functions into a cohesive analytical pipeline.

### 3. Project Architecture (6 Pipeline Stages)
```
[ Stage 1: Raw Ingestion & Audit ]
               │
               ▼
[ Stage 2: Systematic Data Cleaning ]  <-- Deduplicate, Cast Dtypes, Impute Nulls
               │
               ▼
[ Stage 3: Exploratory Data Analysis ]  <-- Summary Stats, Correlation, Frequency
               │
               ▼
[ Stage 4: Business Insights & Aggregation ]  <-- GroupBy, Pivot Tables, Time Series
               │
               ▼
[ Stage 5: ML Dataset Preprocessing ]  <-- Feature Matrix X, Target y, One-Hot Encoding
               │
               ▼
[ Stage 6: Validation & Artifact Export ]  <-- Parquet/CSV Export, Assertion Audit
```

### 4. Stage Breakdown
- **Stage 1 (Ingestion)**: Load raw dataset and log `.shape`, `.dtypes`, missing values.
- **Stage 2 (Cleaning)**: Standardize headers, strip currency symbols, convert date types, handle missing values, drop duplicates.
- **Stage 3 (EDA)**: Compute statistical summaries, inspect distributions, analyze correlations.
- **Stage 4 (Business Insights)**: Group transactions by customer cohort, build monthly revenue pivot tables, compute rolling averages.
- **Stage 5 (ML Preprocessing)**: Define target label (e.g. `High_Value_Customer`), create feature matrix $X$, one-hot encode categories.
- **Stage 6 (Validation)**: Run quality assertions and export clean artifacts.

### 5. Summary
This project synthesizes all Phase 2 learning outcomes into a production-grade data science workflow.
