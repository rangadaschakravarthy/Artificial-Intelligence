# Day 90 — Array Data Types

## Learning Objectives
- Master NumPy numerical data types (`int32`, `int64`, `float32`, `float64`, `bool_`, `complex128`).
- Understand memory footprint, precision, and type casting (`astype`).
- Learn overflow, underflow, and numerical stability in data processing.

## Prerequisites
- Day 86: NumPy Introduction

## Topics Covered
1. Built-in NumPy `dtype` categories (Integers, Floats, Booleans, Strings)
2. Bit precision (8-bit, 16-bit, 32-bit, 64-bit) and byte size
3. Explicit type conversion using `.astype()`
4. Integer overflow and floating-point precision loss
5. Memory optimization for large ML datasets

## Why This Matters
Choosing appropriate data types cuts dataset memory usage by 50%–75% and accelerates GPU training speed in Deep Learning.

## Real-World Usage
Downcasting `float64` tabular data to `float32` or `float16` to fit large ML datasets into GPU VRAM.

## Study Order
1. Read `theory.md`.
2. Review `examples.md`.
3. Complete `practice.md`.
4. Verify using `solution.md`.
5. Run `code.py`.

## Completion Checklist
- [ ] I can list common NumPy data types and their byte sizes.
- [ ] I can convert array types safely using `.astype()`.
- [ ] I understand integer overflow and underflow risks.
- [ ] I can optimize memory footprint using compact data types.

## Difficulty
Beginner
