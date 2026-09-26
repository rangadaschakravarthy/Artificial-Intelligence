# Day 177 Worked Examples: AI Problem Types

## Example 1 — Practical: Mapping Problems to AI Paradigms
```python
problems = [
    {"task": "Solve Sudoku Puzzle", "type": "Constraint Satisfaction Problem (CSP)"},
    {"task": "Find shortest driving route in GPS", "type": "Heuristic Graph Search (A*)"},
    {"task": "Play Tic-Tac-Toe optimally", "type": "Adversarial Search (Minimax)"},
    {"task": "Classify credit card transaction as fraud", "type": "Supervised Machine Learning"}
]

for p in problems:
    print(f"Task: '{p['task']}' -> Type: {p['type']}")
```
