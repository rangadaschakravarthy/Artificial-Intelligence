# Day 172 — Data Preprocessing Mini Project: Machine-Learning-Ready Dataset Preparation

## Learning Objectives
- Execute a complete, leak-free Data Preprocessing capstone project on a messy raw dataset.
- Process raw data through all 12 preprocessing stages from raw ingest to final ML-ready arrays.
- Validate dataset shape, non-null assertions, and export clean $X_{	ext{train}}$, $X_{	ext{test}}$, $y_{	ext{train}}$, and $y_{	ext{test}}$ artifacts.

## Prerequisites
- Days 153–171 (Phase 4 Data Preprocessing Complete)

## Topics Covered
- End-to-End Preprocessing Project Pipeline:
  1. Raw Data Ingestion & Audit
  2. Missing Value Imputation
  3. Deduplication & Invalid Filtering
  4. Categorical Encoding (Ordinal & One-Hot)
  5. Outlier Detection & Winsorization Capping
  6. Feature Transformation (Log1p)
  7. Train/Test Split (80/20 Stratified)
  8. Feature Scaling (Fit on Train, Transform on Test)
  9. Correlation-Based Feature Selection
  10. Preprocessing Pipeline Verification & Quality Assertions
  11. Exporting ML-Ready Parquet / CSV Arrays
- Final Curriculum Capstone Synthesis

## Why This Matters
This capstone mini-project marks the completion of Level 2 Data Science Foundations, producing high-quality ML-ready datasets ready for Level 3 Machine Learning algorithms.

## Practical Work
- Execute the complete 11-stage preprocessing pipeline in `code.py` and output clean $X$ and $y$ artifacts.

## Completion Checklist
- [ ] I can build an end-to-end leak-free data preprocessing pipeline.
- [ ] I can handle missing values, encodings, scaling, and feature selection.
- [ ] I can produce machine-learning-ready datasets for Level 3.

## Difficulty
Advanced
