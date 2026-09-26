# Day 86 — NumPy Introduction

## Learning Objectives
- Understand what NumPy (Numerical Python) is and why it forms the bedrock of data science and AI.
- Differentiate between native Python lists and NumPy `ndarray` objects in memory layout and performance.
- Learn basic NumPy array creation and installation verification.

## Prerequisites
- Level 1: Linear Algebra (Vectors and Matrices)
- Basic Python syntax (Lists, Loops, Functions)

## Topics Covered
1. What is NumPy and C-array memory backing
2. Python Lists vs NumPy Arrays (Contiguous Memory Layout)
3. Installing & Importing NumPy (`import numpy as np`)
4. Core ndarray object attributes
5. First vector and matrix creations

## Why This Matters
All modern AI libraries (Pandas, Scikit-Learn, PyTorch, TensorFlow) rely on NumPy ndarrays under the hood. NumPy enables C-speed vectorized numerical computing in Python.

## Real-World Usage
Processing image pixel tensors, audio waveforms, text embedding vectors, and large tabular datasets at high performance.

## Study Order
1. Read `theory.md` (14 detailed sections).
2. Examine `examples.md` (5 worked numerical & benchmarking examples).
3. Attempt all exercises in `practice.md`.
4. Validate solutions using `solution.md`.
5. Run and experiment with `code.py`.

## Practical Work
Compare execution speed between Python `for` loops and NumPy vector operations over 1,000,000 elements.

## Interview Preparation
Be ready to explain contiguous vs non-contiguous memory, GIL bypass in C-extensions, and type homogeneity.

## Completion Checklist
- [ ] I understand why NumPy is faster than Python lists.
- [ ] I can explain contiguous memory allocation.
- [ ] I can import NumPy and check its version.
- [ ] I can create basic 1D and 2D arrays.
- [ ] I can identify mistakes like passing mixed types into NumPy arrays.
- [ ] I can connect NumPy arrays to Level 1 vector/matrix foundations.

## Difficulty
Beginner
