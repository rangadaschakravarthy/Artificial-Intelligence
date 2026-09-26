# Day 181 Worked Examples: Symbolic AI

## Example 1 — Practical: Symbolic Rule-Based Inference
```python
# Knowledge Base (Facts & Rules)
facts = {"has_wings": True, "can_fly": True}

# Inference Engine
def infer_animal(knowledge):
    if knowledge.get("has_wings") and knowledge.get("can_fly"):
        return "Bird"
    return "Unknown"

print("Inferred Entity:", infer_animal(facts))
```
