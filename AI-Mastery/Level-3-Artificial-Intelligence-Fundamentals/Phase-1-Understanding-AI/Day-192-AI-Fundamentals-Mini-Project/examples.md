# Day 192 Worked Examples: AI Fundamentals Mini Project

## Complete Workflow Overview
```python
def smart_router(request_text):
    # Pathway 1: Automation Check
    if request_text.startswith("BACKUP"):
        return "Automation Engine: Executing Script"
    # Pathway 2: Symbolic Rule Check
    elif "cancel" in request_text and "refund" in request_text:
        return "Symbolic Rule Engine: Process Refund Approval"
    # Pathway 3: ML Intent Engine
    else:
        return "ML Intent Engine: Classify Natural Language Request"
```
