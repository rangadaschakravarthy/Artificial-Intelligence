# Day 105 Solutions: Mini-Project Challenges

## Challenge Solutions
1. 
```python
ss_res = np.sum((y - y_pred)**2)
ss_tot = np.sum((y - np.mean(y))**2)
r2_score = 1.0 - (ss_res / ss_tot)
```
2. 
```python
x_min = X.min(axis=0); x_max = X.max(axis=0)
X_minmax = (X - x_min) / (x_max - x_min)
```
3. 
```python
fold_size = len(X) // 5
for fold in range(5):
    val_idx = slice(fold * fold_size, (fold + 1) * fold_size)
    X_val = X[val_idx]
```
4. `w = np.linalg.pinv(X_design.T @ X_design) @ X_design.T @ y`
5. Pipeline runs under ~0.05 seconds for 100k records due to complete C-vectorization.
