# Day 129 — Data Cleaning Workflow

## Learning Objectives
- Execute an end-to-end data cleaning pipeline on raw, messy datasets.
- Systematically inspect, fix datatypes, handle missing values, remove duplicates, and validate clean data.
- Structure reproducible, modular Python data cleaning functions.

## Prerequisites
- Day 115: Missing Values
- Day 117: Duplicates
- Day 118: Data Type Conversion

## Topics Covered
- Structured 10-Step Data Cleaning Framework
- Raw data inspection and metadata audit
- Schema alignment and data type casting
- Handling missing data and duplicate row policy
- Invalid value filtering and range bounds enforcement
- Text standardization and string whitespace stripping
- Clean data output validation and assertion testing

## Why This Matters
Real-world data is dirty, incomplete, misformatted, and full of invalid entries. Data cleaning accounts for 60–80% of a Data Scientist's project time.

## Real-World Usage
Cleaning raw web-scraped job listings containing missing salaries, invalid dates, duplicate entries, and messy string locations.

## Study Order
1. Read `theory.md` for the 10-step cleaning pipeline.
2. Review `examples.md` for pipeline code structure.
3. Run `code.py` to see complete automated cleaning.
4. Complete `practice.md` and check `solution.md`.

## Practical Work
- Implement a reusable `clean_dataset(df)` function.
- Process a dirty e-commerce log containing nulls, duplicates, and string currency symbols (`"$100.00"`).

## Interview Preparation
- Describe your step-by-step framework for cleaning a completely un-inspected dataset.
- How do you ensure a data cleaning pipeline does not cause subtle data leakage?

## Completion Checklist
- [ ] I can follow a systematic data cleaning framework.
- [ ] I can write modular cleaning functions.
- [ ] I can validate cleaned output using assertion checks.
- [ ] I can document cleaning steps reproducibly.

## Difficulty
Intermediate
