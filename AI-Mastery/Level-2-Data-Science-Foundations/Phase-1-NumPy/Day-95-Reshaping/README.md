# Day 95 — Reshaping

## Learning Objectives
- Master array shape transformations using `reshape()`, `resize()`, `ravel()`, and `flatten()`.
- Learn matrix transposition (`.T`, `np.transpose()`, `swapaxes()`).
- Understand contiguous memory requirements during reshaping.

## Prerequisites
- Day 89: Array Shape

## Topics Covered
1. `reshape()` syntax and view creation rules
2. `ravel()` (zero-copy 1D view) vs `flatten()` (explicit 1D copy)
3. Matrix Transpose `.T` and `np.transpose(arr, axes)`
4. `swapaxes(axis1, axis2)` for multi-dimensional tensors
5. Fixing non-contiguous array errors using `np.ascontiguousarray()`

## Why This Matters
Reshaping tensor dimensions is required when converting raw feature data into model input dimensions (e.g. flattening image matrices before dense neural layers).

## Real-World Usage
Converting 2D single images `(28, 28)` to 4D image batches `(1, 1, 28, 28)` for PyTorch CNN inference.

## Study Order
1. Read `theory.md`.
2. Review `examples.md`.
3. Complete `practice.md`.
4. Verify using `solution.md`.
5. Run `code.py`.

## Completion Checklist
- [ ] I can reshape arrays without changing total size.
- [ ] I know the difference between `ravel()` and `flatten()`.
- [ ] I can transpose 2D matrices and N-dimensional tensors.
- [ ] I can swap specific tensor axes using `swapaxes()`.

## Difficulty
Intermediate
