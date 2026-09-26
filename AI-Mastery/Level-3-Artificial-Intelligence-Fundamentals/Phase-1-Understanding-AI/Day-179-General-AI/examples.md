# Day 179 Worked Examples: General AI

## Example 1 — Practical: Conceptual Benchmark Evaluation
```python
benchmarks = [
    {"test": "Wozniak Coffee Test", "description": "Enter a strange house, locate kitchen, find coffee machine, and brew coffee autonomously."},
    {"test": "Nilsson Employment Test", "description": "Enroll as a new employee in an ordinary office job and perform duties as effectively as a human."},
    {"test": "Turing Test (Extended)", "description": "Sustain open-domain multimodal conversation indistinguishably from a human."}
]

for b in benchmarks:
    print(f"[{b['test']}]: {b['description']}")
```
