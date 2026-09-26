# Day 209 Worked Examples: AI History Mini Project

## Complete Engine Overview
```python
# Fact Base
facts = {"has_fever", "has_cough"}

# Rule Base
rules = [
    {"name": "Rule 1", "if": {"has_fever", "has_cough"}, "then": "respiratory_infection"},
    {"name": "Rule 2", "if": {"respiratory_infection"}, "then": "recommend_rest_and_fluids"}
]

# Forward Chaining Execution
inferred = set(facts)
explanation = []

for r in rules:
    if r["if"].issubset(inferred):
        inferred.add(r["then"])
        explanation.append(f"Fired {r['name']}: {r['if']} -> {r['then']}")

print("Inferred Knowledge:", inferred)
print("Explanation Trace:", explanation)
```
