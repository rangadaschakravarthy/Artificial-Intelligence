# Day 175 Worked Examples: Intelligent Agents

## Example 1 — Practical: PEAS Specification Table
```python
peas_database = {
    "Medical Diagnosis System": {
        "P": "Healthy patient, minimized costs, zero misdiagnoses",
        "E": "Patient, hospital staff, lab test equipment",
        "A": "Display medical diagnosis, recommend treatments, order tests",
        "S": "Keyboard entry of symptoms, lab test results, vitals monitors"
    },
    "Chess AI": {
        "P": "Win game, minimize move count",
        "E": "8x8 chessboard, opponent pieces",
        "A": "Move piece on board",
        "S": "Board state sensor / move input"
    }
}

for system, peas in peas_database.items():
    print(f"
--- PEAS for {system} ---")
    for key, val in peas.items():
        print(f"  {key}: {val}")
```
