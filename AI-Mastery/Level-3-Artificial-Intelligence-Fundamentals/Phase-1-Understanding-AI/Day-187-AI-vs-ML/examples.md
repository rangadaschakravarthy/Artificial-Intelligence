# Day 187 Worked Examples: AI vs ML

## Example 1 — Practical: Non-ML AI vs ML AI
```python
# Non-ML AI: A* Shortest Path Graph Search (Deterministic Graph Algorithm)
def non_ml_ai_search(graph, start, goal):
    return f"Path found from {start} to {goal} using A* Search algorithm."

# ML AI: Churn Prediction Model (Statistical Model Learned from Data)
def ml_ai_predict(user_features):
    score = user_features["tenure"] * -0.5 + user_features["calls"] * 0.8
    return "High Churn Risk" if score > 0 else "Low Churn Risk"

print("Non-ML AI Output:", non_ml_ai_search(None, "NodeA", "NodeB"))
print("ML AI Output:    ", ml_ai_predict({"tenure": 2, "calls": 5}))
```
