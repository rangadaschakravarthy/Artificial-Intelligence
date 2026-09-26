# Day 132 Practice Questions: Pandas Mini Project

## Level 1 — Basic
1. What are the 6 primary stages of a structured Data Science Pandas project?
2. What assertion checks should be run before exporting an ML dataset?
3. How do you extract year-month period strings (`'2023-05'`) from a datetime column?
4. What Pandas method exports DataFrames to CSV files without index labels?
5. True or False: Data cleaning should happen BEFORE computing correlation matrices.

## Level 2 — Coding
1. Write code to log before and after row counts during deduplication.
2. Clean string currency column `'$1,450.99'` to `float64`.
3. Construct a monthly pivot table of sales by product line.
4. Separate features $X$ from binary target $y$ (`High_Spend = 1`).
5. Run automated unit assertions verifying zero nulls and no string object dtypes in $X$.

## Level 3 — Data Analysis
1. Analyze top 5 revenue-generating customer segments from dirty sales data.
2. Discover monthly sales seasonality trends using resampled date indexing.
3. Compute customer lifetime value (LTV) summary metrics grouped by acquisition channel.
4. Identify multi-collinear feature pairs in engineered feature matrix $X$.
5. Synthesize 4 executive recommendations based on project EDA results.

## Level 4 — Debugging
1. Fix pipeline crash caused by un-parsed date strings during monthly pivoting.
2. Correct feature misalignment when encoding train and test sets separately.
3. Fix memory leak when processing large batch transaction datasets.

## Level 5 — AI/ML Application
1. Demonstrate building an automated end-to-end data pipeline script taking raw CSV to ML $X$ and $y$.
2. Explain how mini-project modularity enables integration into production Airflow / Kubeflow DAG pipelines.
3. Validate feature matrix shapes and non-null states programmatically.

## Level 6 — Interview Questions
1. Walk through your Day 132 mini project end-to-end as if interviewing for a Senior Data Scientist position.
2. How did you handle missing values and trade-offs between dropping vs imputing in your project?
3. How would you scale this pipeline to handle 100GB datasets using Dask or PySpark?
4. What key business insights did your project uncover, and how do they connect to business strategy?
5. How do you write automated regression tests for Pandas data processing pipelines?
