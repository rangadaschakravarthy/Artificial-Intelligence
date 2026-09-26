# Day 201 Worked Examples: Second AI Winter

## Example 1 — Practical: Simulating Rule Base Conflict Overhead
```python
# Demonstrating how adding rules creates combinatorial rule conflicts
rule_count = [100, 1000, 10000]
for r in rule_count:
    potential_conflicts = (r * (r - 1)) // 2
    print(f"Rules: {r:5d} -> Potential Rule Conflicts: {potential_conflicts:10,d}")
```
