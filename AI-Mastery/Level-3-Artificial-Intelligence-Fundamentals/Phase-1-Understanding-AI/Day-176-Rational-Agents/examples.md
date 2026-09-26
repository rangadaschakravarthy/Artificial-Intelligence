# Day 176 Worked Examples: Rational Agents

## Example 1 — Practical: Expected Utility Decision
```python
# Decision Under Uncertainty: Crossing the Street
actions = {
    "Look Both Ways & Cross": {"P(Safe)": 0.999, "Utility_Safe": 10, "P(Hit)": 0.001, "Utility_Hit": -1000},
    "Cross Blindly": {"P(Safe)": 0.70, "Utility_Safe": 10, "P(Hit)": 0.30, "Utility_Hit": -1000}
}

for action, vals in actions.items():
    eu = (vals["P(Safe)"] * vals["Utility_Safe"]) + (vals["P(Hit)"] * vals["Utility_Hit"])
    print(f"Action: '{action}' -> Expected Utility: {eu:.2f}")
```
