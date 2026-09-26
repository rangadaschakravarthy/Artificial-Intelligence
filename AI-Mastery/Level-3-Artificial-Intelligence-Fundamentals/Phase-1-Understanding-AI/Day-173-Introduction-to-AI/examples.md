# Day 173 Worked Examples: Introduction to AI

## Example 1 — Beginner: Classifying Systems into the 4 AI Quadrants
```python
systems = [
    {"name": "ELIZA Chatbot", "quadrant": "Acting Humanly", "reason": "Imitates human conversation patterns"},
    {"name": "Cognitive Architecture (SOAR)", "quadrant": "Thinking Humanly", "reason": "Models human working memory and problem solving"},
    {"name": "Automated Logic Theorem Prover", "quadrant": "Thinking Rationally", "reason": "Evaluates formal logic syllogisms for validity"},
    {"name": "Chess Engine (Stockfish)", "quadrant": "Acting Rationally", "reason": "Calculates moves maximizing expected win utility"}
]

for s in systems:
    print(f"[{s['name']}] -> {s['quadrant']} ({s['reason']})")
```

## Example 2 — Practical: Percept-Action Agent Mapping
```python
# Simple Vacuum Environment Agent
class ReflexVacuumAgent:
    def __init__(self):
        pass
    def select_action(self, location, status):
        if status == "Dirty":
            return "Suck"
        elif location == "A":
            return "Right"
        elif location == "B":
            return "Left"

agent = ReflexVacuumAgent()
print("Action for (Location A, Dirty):", agent.select_action("A", "Dirty"))
print("Action for (Location A, Clean):", agent.select_action("A", "Clean"))
```
