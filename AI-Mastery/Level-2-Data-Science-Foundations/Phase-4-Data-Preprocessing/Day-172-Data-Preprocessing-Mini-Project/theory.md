# Day 172 Theory: Data Preprocessing Mini Project Architecture

### 1. What Is It?
The Data Preprocessing Mini Project is the final Level 2 capstone pipeline that converts raw, messy, un-preprocessed tabular data into validated, leak-free numeric feature matrices ($X$) and target vectors ($y$) for Machine Learning.

### 2. Complete 11-Stage Pipeline Flow
```
[ 1. Ingest Raw Data ]
          │
          ▼
[ 2. Separate Target y & Features X ]
          │
          ▼
[ 3. Clean Corrupt Values & Deduplicate ]
          │
          ▼
[ 4. Perform Train/Test Split FIRST (80/20 Stratified) ]  <-- Leakage Boundary!
          │
          ▼
[ 5. Fit Imputers on Train ➔ Transform Train & Test ]
          │
          ▼
[ 6. Encode Categoricals (Ordinal & One-Hot with drop='first') ]
          │
          ▼
[ 7. Cap Outliers (Winsorize on Train bounds) ]
          │
          ▼
[ 8. Transform Skewed Features (Log1p) ]
          │
          ▼
[ 9. Fit Scaler on Train ➔ Scale Train & Test ]
          │
          ▼
[ 10. Select Features (Correlation Pruning on Train) ]
          │
          ▼
[ 11. Run Quality Assertions & Export ML Datasets ]
```

### 3. Summary
This capstone pipeline integrates all Level 2 Data Science Foundations skills into a production-grade, leak-free machine-learning dataset preparation system.
