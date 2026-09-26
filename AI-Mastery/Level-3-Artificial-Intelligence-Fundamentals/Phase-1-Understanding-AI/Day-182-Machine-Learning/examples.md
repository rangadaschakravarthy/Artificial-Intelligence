# Day 182 Worked Examples: Machine Learning

## Example 1 — Practical: Tom Mitchell's T, P, E Framework Mapping
```python
ml_apps = [
    {"app": "Spam Filter", "T": "Classify emails as spam/ham", "P": "% correct classifications", "E": "Database of labeled emails"},
    {"app": "Checkers Player", "T": "Play checkers games", "P": "% games won vs opponents", "E": "History of self-play games"}
]

for app in ml_apps:
    print(f"
--- {app['app']} ---")
    print(f"  Task (T): {app['T']}")
    print(f"  Performance (P): {app['P']}")
    print(f"  Experience (E): {app['E']}")
```
