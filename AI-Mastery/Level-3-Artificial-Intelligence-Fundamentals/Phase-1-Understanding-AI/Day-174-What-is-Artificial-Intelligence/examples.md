# Day 174 Worked Examples: What is Artificial Intelligence

## Example 1 — Practical: System Evaluation Matrix
```python
systems = [
    {"name": "Rule Calculator", "perceive": False, "learn": False, "reason": False, "ai": False},
    {"name": "Expert System", "perceive": True, "learn": False, "reason": True, "ai": True},
    {"name": "Deep Learning Vision", "perceive": True, "learn": True, "reason": True, "ai": True}
]

for s in systems:
    print(f"System: {s['name']} -> AI System? {s['ai']}")
```
