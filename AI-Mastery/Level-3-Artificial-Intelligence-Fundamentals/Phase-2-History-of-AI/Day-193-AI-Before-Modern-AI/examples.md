# Day 193 Worked Examples: AI Before Modern AI & Early Ideas

## Example 1 — Practical: Boolean Logic Syllogism Evaluator
```python
def syllogism_evaluator(all_men_mortal, socrates_is_man):
    # Aristotle's Deductive Logic
    socrates_mortal = all_men_mortal and socrates_is_man
    return socrates_mortal

print("Is Socrates Mortal?", syllogism_evaluator(True, True))
```
