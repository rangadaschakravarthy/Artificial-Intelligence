# Day 168 Theory: Data Leakage

### 1. What Is It?
Data Leakage occurs when information from outside the training dataset (such as target labels or validation/test set statistics) is accidentally introduced into the model training pipeline.

### 2. The Golden Rule of Preprocessing
> **FIT ONLY ON TRAIN. TRANSFORM ON TRAIN AND TEST.**

$$
\mu_{	ext{train}}, \sigma_{	ext{train}} = 	ext{fit}(X_{	ext{train}})
$$

$$
X_{	ext{train, scaled}} = 	ext{transform}(X_{	ext{train}}, \mu_{	ext{train}}, \sigma_{	ext{train}})
$$

$$
X_{	ext{test, scaled}} = 	ext{transform}(X_{	ext{test}}, \mu_{	ext{train}}, \sigma_{	ext{train}})
$$

### 3. Incorrect vs Correct Preprocessing Workflows

**WRONG (Data Leakage!):**
```
Full Dataset ➔ Fit & Transform Scaler ➔ Train/Test Split
```
*Why WRONG?* `fit()` computes mean $\mu$ and std $\sigma$ over the ENTIRE dataset, leaking test set statistics into training data!

**CORRECT (Leak-Free):**
```
Full Dataset ➔ Train/Test Split ➔ Fit Scaler on Train ONLY ➔ Transform Train & Test
```

### 4. Summary
Always fit scalers, encoders, and imputers strictly on training data after performing train/test split.
