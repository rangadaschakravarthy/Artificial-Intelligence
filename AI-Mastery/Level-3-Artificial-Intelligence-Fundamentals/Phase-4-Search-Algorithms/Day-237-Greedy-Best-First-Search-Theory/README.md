# Day 237: Greedy Best-First Search Theory

## Learning Objectives
- Master heuristic search theory, evaluation metrics ($g, h, f$), and implementation paradigms.
- Prove admissibility ($h(n) \le h^*(n)$) and consistency ($h(n) \le c(n, a, n') + h(n')$).
- Execute numerical trace tables and build executable Python $A^*$ and Greedy search solvers.

## Prerequisites
- Days 226-234: Foundations of Uninformed Search (BFS, DFS, UCS).

## Topics Covered
1. Heuristic Search Mechanics & Mathematical Foundations
2. Admissibility & Consistency Guarantees
3. Manual Trace Tables for $g(n), h(n), f(n)$
4. Python Implementation with `heapq`
5. Real-World Applications in Game Navigation & Robotics

## Day Checklist
- [ ] Read `theory.md` and review examples in `examples.md`.
- [ ] Run `code.py` to compare $g(n)$, $h(n)$, and $f(n)$ search dynamics.
- [ ] Solve all 26 exercises in `practice.md`.

## Difficulty Level
Advanced
