# Day 99 Worked Examples: Aggregation and Statistics

## Example 1 — Beginner: Basic Summary Statistics
```python
import numpy as np

data = np.array([12, 15, 18, 22, 30, 45, 88])

print("Mean:              ", np.mean(data))
print("Median:            ", np.median(data))
print("Population Variance:", np.var(data))
print("Sample Variance:    ", np.var(data, ddof=1))
print("Standard Deviation: ", np.std(data))
print("Min / Max:         ", np.min(data), "/", np.max(data))
print("Range (Peak-to-Peak):", np.ptp(data))
```

## Example 2 — Practical: Positional Argmax & Argmin
```python
import numpy as np

# Model confidence scores for 4 classes: [Cat, Dog, Bird, Fish]
probabilities = np.array([0.05, 0.75, 0.15, 0.05])

predicted_class_idx = np.argmax(probabilities)
class_names = ['Cat', 'Dog', 'Bird', 'Fish']

print("Highest Probability:", np.max(probabilities))
print("Predicted Class Index:", predicted_class_idx)
print("Predicted Class Name: ", class_names[predicted_class_idx])
```

## Example 3 — Intermediate: Axis Reduction across 2D Feature Matrix
```python
import numpy as np

# 3 Patients, 3 Features: [Age, Heart Rate, Blood Sugar]
matrix = np.array([
    [25, 72, 95],
    [50, 85, 140],
    [35, 68, 110]
])

print("Overall Matrix Mean:", np.mean(matrix))
print("Feature Means (axis=0 - down columns):", np.mean(matrix, axis=0))
print("Patient Means (axis=1 - across rows):", np.mean(matrix, axis=1))
```

## Example 4 — Real Dataset: Handling Missing Values with NaN-Robust Functions
```python
import numpy as np

# Sensor readings with missing data (NaN)
sensor_data = np.array([21.5, 22.0, np.nan, 23.5, np.nan, 21.0])

print("Standard Mean:  ", np.mean(sensor_data))    # Output: nan
print("NaN-Robust Mean:", np.nanmean(sensor_data)) # Output: 22.0
print("NaN-Robust Std: ", np.round(np.nanstd(sensor_data), 2))
```

## Example 5 — AI/ML Application: Sorting Top-K Predictions using argsort
```python
import numpy as np

# Model logits for 5 classes
logits = np.array([1.2, 4.8, 0.5, 3.1, 2.0])

# Get indices that sort array in ascending order
sorted_indices = np.argsort(logits)

# Top-2 class prediction indices (reverse slice)
top_2_indices = sorted_indices[::-1][:2]

print("Logits:            ", logits)
print("Sorted Indices:    ", sorted_indices)
print("Top-2 Class Indices:", top_2_indices)
```
