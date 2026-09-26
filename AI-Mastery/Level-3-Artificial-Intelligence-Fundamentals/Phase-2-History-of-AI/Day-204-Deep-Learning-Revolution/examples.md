# Day 204 Worked Examples: Deep Learning Revolution

## Example 1 — Practical: ImageNet Error Rate Milestone Progression
```python
milestones = [
    {"year": 2010, "model": "Traditional Computer Vision", "top5_error": "28.2%"},
    {"year": 2012, "model": "AlexNet (Deep CNN)", "top5_error": "15.3%"},
    {"year": 2014, "model": "VGG / GoogLeNet", "top5_error": "6.7%"},
    {"year": 2015, "model": "ResNet (Human-surpassing)", "top5_error": "3.5%"}
]

for m in milestones:
    print(f"Year {m['year']} [{m['model']}] -> Top-5 Error: {m['top5_error']}")
```
