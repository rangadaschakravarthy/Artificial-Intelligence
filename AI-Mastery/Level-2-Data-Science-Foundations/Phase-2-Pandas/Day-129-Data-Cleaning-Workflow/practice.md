# Day 129 Practice Questions: Data Cleaning Workflow

## Level 1 — Basic
1. What are the first three steps in a structured 10-step data cleaning pipeline?
2. How do you convert column headers to clean snake_case titles in Pandas?
3. What Pandas method converts numeric strings containing errors (`'INVALID'`) into `NaN`?
4. True or False: You should always make a copy (`df.copy()`) before applying cleaning pipelines to raw data.
5. What assertion statement verifies that zero missing values remain in a DataFrame?

## Level 2 — Coding
1. Write code to strip leading and trailing whitespace from all string columns in a DataFrame.
2. Clean column `'Salary'` containing strings like `'$85,000.00'` into `float64`.
3. Drop duplicate rows based on subset column `'Customer_ID'`.
4. Replace invalid ages (`Age < 0` or `Age > 120`) with `NaN`.
5. Implement a unit assertion check verifying that DataFrame shape has at least 1 row post-cleaning.

## Level 3 — Data Analysis
1. Build a clean customer master dataset from dirty CRM exports.
2. Process raw scraped job posting data (extract salaries, clean locations, handle missing remote flags).
3. Clean sensor telemetry logs containing invalid negative pressure readings and duplicate timestamps.
4. Process financial transaction tables by stripping currency symbols and coercing date formats.
5. Build an automated validation function checking 5 data quality assertions on cleaned output.

## Level 4 — Debugging
1. Fix error: `AttributeError: Can only use .str accessor with string values` when running `.str.strip()` on a mixed-type column.
2. Fix pipeline bug where cleaning steps modify global raw DataFrame state unexpectedly.
3. Correct silent bug where numeric string cleaning turns numbers into unexpected `NaN` values due to unescaped regex parameters.

## Level 5 — AI/ML Application
1. Implement a complete data cleaning function that prepares raw web data into a leak-free ML dataset.
2. Why should outlier removal rules be defined during EDA rather than blindly applied during data cleaning?
3. How do automated assertion checks prevent silent downstream model failures?

## Level 6 — Interview Questions
1. Walk through your complete end-to-end framework for cleaning a 1-million-row unknown dataset.
2. How do you document data cleaning decisions for reproducibility and stakeholder transparency?
3. What is the difference between data cleaning and feature engineering?
4. How do you handle missing values when 40% of rows in a key column are missing?
5. How do you design a data cleaning pipeline to run safely in production on automated batches?
