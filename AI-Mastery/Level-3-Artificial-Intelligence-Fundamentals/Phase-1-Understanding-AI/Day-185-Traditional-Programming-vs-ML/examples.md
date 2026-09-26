# Day 185 Worked Examples: Traditional Programming vs ML

## Example 1 — Practical: Tax Calculator (Traditional) vs Fraud Detector (ML)
```python
# Traditional: Explicit Tax Rules
def calculate_tax(income):
    if income <= 50000:
        return income * 0.10
    else:
        return 5000 + (income - 50000) * 0.20

print("Traditional Tax Output:", calculate_tax(60000))
```
