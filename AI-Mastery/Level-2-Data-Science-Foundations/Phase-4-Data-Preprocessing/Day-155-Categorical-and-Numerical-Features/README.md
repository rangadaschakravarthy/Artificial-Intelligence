# Day 155 — Categorical and Numerical Features

## Learning Objectives
- Automate detection and separation of numerical vs categorical feature columns in DataFrames.
- Handle high-cardinality vs low-cardinality categorical variables.
- Detect numerical features disguised as strings and categorical features disguised as integers.

## Prerequisites
- Day 154: Features and Targets

## Topics Covered
- Automatic column type inspection using `df.select_dtypes()`
- Low-cardinality (e.g. `< 10` unique levels) vs High-cardinality (e.g. `> 100` unique levels) categories
- Detecting integer-encoded categorical features (e.g. `ZipCode = 90210` or `Status_Code = 1, 2, 3`)
- Converting object columns to pandas `category` dtype
- Defining dedicated preprocessing sub-pipelines for numerical vs categorical columns

## Practical Work
- Write an automated feature splitter function that partitions DataFrame columns into `num_cols`, `low_card_cat_cols`, and `high_card_cat_cols`.

## Difficulty
Intermediate
