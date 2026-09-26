# Day 190 Worked Examples: AI System Architecture

## Example 1 — Practical: End-to-End AI Router Microservice Pipeline
```python
def ai_system_pipeline(raw_percept):
    # Layer 1: Ingestion & Preprocessing
    clean_percept = raw_percept.strip().lower()
    
    # Layer 2: Inference / Search Engine
    if "emergency" in clean_percept:
        decision = "Priority Dispatch"
    else:
        decision = "Standard Queue"
        
    # Layer 3: Safety Guardrail Actuation
    return f"Executing Action: [{decision}] for Percept: '{clean_percept}'"

print(ai_system_pipeline(" EMERGENCY: Medical assistance needed "))
```
