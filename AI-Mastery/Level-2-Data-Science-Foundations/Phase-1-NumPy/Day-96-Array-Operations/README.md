# Day 96 — Array Operations

## Learning Objectives
- Master element-wise arithmetic, comparison, and logical array operations.
- Understand in-place operators (`+=`, `-=`, `*=`) and out-of-place array allocations.
- Connect element-wise mathematical operations to Level 1 linear algebra principles.

## Prerequisites
- Day 86: NumPy Introduction

## Topics Covered
1. Element-wise arithmetic (`+`, `-`, `*`, `/`, `//`, `%`, `**`)
2. Comparison operators (`==`, `!=`, `<`, `>`, `<=`, `>=`)
3. Universal functions (ufuncs) concept
4. In-place vs Out-of-place memory operations
5. Matrix element-wise multiplication (Hadamard Product) vs Matrix Product

## Why This Matters
Element-wise array operations form the mathematical foundation for loss computation, feature scaling, and activation functions in machine learning.

## Real-World Usage
Applying feature scaling formulas $X_{	ext{scaled}} = rac{X - \mu}{\sigma}$ across entire datasets simultaneously.

## Study Order
1. Read `theory.md`.
2. Review `examples.md`.
3. Complete `practice.md`.
4. Verify using `solution.md`.
5. Run `code.py`.

## Completion Checklist
- [ ] I can perform element-wise arithmetic and comparisons on arrays.
- [ ] I understand the difference between `*` (Hadamard product) and `@` (Matrix multiplication).
- [ ] I know how in-place operators (`+=`) save memory allocation.
- [ ] I can connect element-wise operations to machine learning loss calculations.

## Difficulty
Beginner
