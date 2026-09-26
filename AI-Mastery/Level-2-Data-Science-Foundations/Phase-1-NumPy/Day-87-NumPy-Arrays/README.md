# Day 87 — NumPy Arrays

## Learning Objectives
- Deeply understand the internal layout of the `ndarray` object.
- Master memory strides, buffers, pointer offsets, and flags.
- Create 0D, 1D, 2D, 3D, and N-dimensional arrays cleanly.

## Prerequisites
- Day 86: NumPy Introduction

## Topics Covered
1. Anatomy of `ndarray` (Data buffer, dtype, shape, strides)
2. Creating 0D Scalars, 1D Vectors, 2D Matrices, 3D Tensors
3. Array Flags (`C_CONTIGUOUS`, `F_CONTIGUOUS`, `WRITEABLE`)
4. Views vs Copies in memory allocation
5. Connecting `ndarray` dimensions to AI tensor structures

## Why This Matters
Understanding how ndarrays store data prevents subtle memory bugs, unintended array mutations, and performance degradation in high-performance ML pipelines.

## Real-World Usage
Representing multi-spectral satellite imagery (3D/4D tensors), batch video frames, and transformer multi-head attention matrices.

## Study Order
1. Read `theory.md`.
2. Review `examples.md`.
3. Complete `practice.md`.
4. Verify using `solution.md`.
5. Run `code.py`.

## Completion Checklist
- [ ] I can create 0D, 1D, 2D, and 3D arrays.
- [ ] I understand array strides and contiguous memory flags.
- [ ] I can distinguish memory views from deep copies.
- [ ] I can connect 2D arrays to feature matrices and 3D arrays to RGB images.

## Difficulty
Beginner
