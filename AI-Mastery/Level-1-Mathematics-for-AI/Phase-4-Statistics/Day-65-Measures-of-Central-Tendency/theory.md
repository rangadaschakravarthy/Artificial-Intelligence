# Day 65 Theory: Measures of Central Tendency

### 1. Simple Definition
Measures of central tendency are single summary values that identify the center or typical value of a probability distribution or dataset.

### 2. Intuition
If you had to summarize an entire distribution with one single prediction to minimize error, which value should you pick? The Mean minimizes squared error; the Median minimizes absolute error!

### 3. Mathematical Definition
- Arithmetic Mean: x_bar = (1/n) sum x_i
- Median: Middle value of sorted data (or mean of middle two).
- Mode: Most frequently occurring value.

### 4. Mathematical Notation
- Geometric Mean: G = (prod_{i=1}^n x_i)^(1/n)
- Harmonic Mean: H = n / sum_{i=1}^n (1 / x_i)

### 5. Formula
Arithmetic Mean: x_bar = (1/n) sum x_i
Geometric Mean: G = exp( (1/n) sum log(x_i) )
Harmonic Mean: H = n / sum (1 / x_i)

### 6. Symbol Explanation
- G: Geometric mean (used for multiplicative growth rates)
- H: Harmonic mean (used for ratios/speeds, e.g. F1-score)

### 7. Step-by-Step Calculation
Data: [2, 4, 4, 4, 10, 100] (n=6)
- Mean: (2 + 4 + 4 + 4 + 10 + 100) / 6 = 124 / 6 = 20.67
- Sorted: [2, 4, 4, 4, 10, 100] -> Middle two: 4, 4 -> Median = 4
- Mode: 4 (appears 3 times)
Notice how outlier 100 pulled Mean to 20.67, while Median stayed robust at 4!

### 8. Second Concrete Example
Precision = 0.8, Recall = 0.2.
Harmonic Mean (F1-score):
F1 = 2 * (0.8 * 0.2) / (0.8 + 0.2) = 0.32 / 1.0 = 0.32.
Arithmetic mean would be (0.8+0.2)/2 = 0.50 (misleadingly high!).

### 9. Common Mistakes
- Using Arithmetic Mean for skewed distributions (e.g. Income).
- Using Arithmetic Mean instead of Harmonic Mean for averaging speeds or rates.

### 10. AI Connection
- Loss Minimization: L2 Loss (MSE) optimal prediction is Mean. L1 Loss (MAE) optimal prediction is Median.
- Evaluation Metrics: F1-Score in Classification is Harmonic Mean of Precision and Recall.

### 11. Algorithm Connection
- k-Means Clustering uses Arithmetic Mean for cluster centroids.
- k-Medoids uses Median/Medoid for robust clustering.

### 12. Practical Interpretation
- Mean: Sensitive to extreme values.
- Median: Robust to outliers.
- Mode: Applicable to categorical data.

### 13. Interview Insight
Question: Why is F1-score defined as Harmonic Mean instead of Arithmetic Mean?
Answer: Harmonic mean penalizes extreme imbalances. If Recall is 0, Harmonic Mean is 0, whereas Arithmetic Mean would give 0.5, hiding total model failure on positive class.

### 14. Summary
Mean minimizes L2 error, Median minimizes L1 error, and Harmonic Mean penalizes imbalanced metric rates.
