# Day 198 Worked Examples: Symbolic AI and Knowledge Bases

## Example 1 — Practical: Forward Chaining Engine
```python
facts = {"croaks", "eats_flies"}
rules = [
    {"if": {"croaks", "eats_flies"}, "then": "frog"},
    {"if": {"frog"}, "then": "green"}
]

# Forward Chaining Iteration
inferred = set(facts)
changed = True
while changed:
    changed = False
    for r in rules:
        if r["if"].issubset(inferred) and r["then"] not in inferred:
            inferred.add(r["then"])
            changed = True

print("Inferred Knowledge Base Facts:", inferred)
```
