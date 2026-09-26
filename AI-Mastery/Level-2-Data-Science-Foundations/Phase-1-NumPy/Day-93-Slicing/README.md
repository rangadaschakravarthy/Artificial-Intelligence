# Day 93 — Slicing

## Learning Objectives
- Master multidimensional array slicing using syntax `[start:stop:step]`.
- Understand zero-copy views created during array slicing.
- Extract sub-matrices, specific rows, columns, and step-strided slices cleanly.

## Prerequisites
- Day 92: Indexing

## Topics Covered
1. 1D Slicing Syntax (`arr[start:stop:step]`)
2. 2D Slicing (`matrix[row_start:row_stop, col_start:col_stop]`)
3. Row and Column extraction (`matrix[i, :]` vs `matrix[:, j]`)
4. Reversing arrays using step `-1` (`arr[::-1]`)
5. Memory views, mutation dangers, and explicit copying

## Why This Matters
Slicing is used constantly to separate feature input matrices $X$ from target labels $y$ and split training datasets into sub-batches.

## Real-World Usage
Extracting Regions of Interest (ROI) bounding boxes from image tensors (`img[y1:y2, x1:x2]`).

## Study Order
1. Read `theory.md`.
2. Review `examples.md`.
3. Complete `practice.md`.
4. Verify using `solution.md`.
5. Run `code.py`.

## Completion Checklist
- [ ] I can slice 1D arrays and 2D matrices.
- [ ] I know how to extract an entire row or column using `:`.
- [ ] I understand that slicing returns a memory view, not a copy.
- [ ] I can reverse array elements using step `-1`.

## Difficulty
Beginner
