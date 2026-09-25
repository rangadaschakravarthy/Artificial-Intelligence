# Day 18 — Tensors

## Learning Objectives
- Understand Tensors as multi-dimensional arrays generalizing scalars, vectors, and matrices
- Master tensor ranks (0D Scalar, 1D Vector, 2D Matrix, 3D/4D High-D Tensors)
- Understand tensor shape, axes/dimensions, and strides
- Manipulate image batches and video tensors in PyTorch/NumPy conventions (`B, C, H, W`)

## Prerequisites
Day 2 — Scalars and Vectors, Day 7 — Matrices

## Topics Covered
- Tensor Definition and Tensor Rank (Order)
- 0D Tensor (Scalar), 1D Tensor (Vector), 2D Tensor (Matrix)
- 3D Tensors (Time Series / RGB Grayscale), 4D Tensors (Image Batches), 5D Tensors (Video)
- Tensor Shapes, Axes, and Permutations (`transpose`, `reshape`, `permute`)
- Tensors in PyTorch and TensorFlow deep learning frameworks

## Why This Matters for AI
All modern deep learning frameworks (PyTorch, TensorFlow, JAX) are built entirely around Tensors. Input batches, neural layer parameters, and attention maps are stored as 3D, 4D, or 5D tensors.

## Study Order
1. Read theory.md
2. Study examples.md
3. Run code.py
4. Complete practice.md
5. Verify with solution.md

## Practical Work
Manipulate high-dimensional tensors in NumPy, permute image axes, and reshape batch arrays.

## Interview Preparation
Explain tensor rank vs matrix rank, and PyTorch `B, C, H, W` image batch tensor conventions.

## Completion Checklist
- [ ] I can identify 0D, 1D, 2D, 3D, and 4D tensors
- [ ] I understand tensor shape and axes
- [ ] I can reshape and permute tensors in Python
- [ ] I know PyTorch `(B, C, H, W)` batch convention

## Estimated Difficulty
Beginner
