# Day 191 Worked Examples: AI Applications and Limitations

## Example 1 — Practical: Demonstrating Moravec's Paradox
```python
tasks = [
    {"task": "Play Superhuman Chess", "difficulty_for_ai": "Easy", "difficulty_for_toddler": "Impossible"},
    {"task": "Walk across a room and pick up a cup", "difficulty_for_ai": "Extremely Hard", "difficulty_for_toddler": "Easy"}
]

for t in tasks:
    print(f"Task: [{t['task']}] -> AI Difficulty: {t['difficulty_for_ai']} | Toddler Difficulty: {t['difficulty_for_toddler']}")
```
