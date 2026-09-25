# Day 64 Theory: Data Types

### 1. Simple Definition
Data types define the nature and mathematical properties of values in a dataset, determining which statistical operations and ML models can be applied.

### 2. Intuition
You cannot average zip codes (nominal), but you can average house prices (ratio). Treating categorical ratings as continuous numbers causes flawed ML predictions.

### 3. Mathematical Definition
Stevens' 4 Levels of Measurement:
1. Nominal: Categories without order (e.g. Red, Blue).
2. Ordinal: Categories with order, but unequal intervals (e.g. Low, Medium, High).
3. Interval: Numerical with equal intervals, but arbitrary zero (e.g. Temperature in Celsius).
4. Ratio: Numerical with true meaningful zero (e.g. Income, Distance).

### 4. Mathematical Notation
- Discrete: X in Z (Integers) or finite categorical set C.
- Continuous: X in R (Real numbers).

### 5. Formula
Min-Max Scaling (Ratio/Interval):
x_norm = (x - x_min) / (x_max - x_min)

One-Hot Encoding Vector:
e_i = [0, ..., 1, ..., 0]^T

### 6. Symbol Explanation
- x_norm: Scaled feature value in [0, 1]
- e_i: Standard basis vector representing category i

### 7. Step-by-Step Calculation
Convert Ordinal data ["Small", "Medium", "Large"] to numerical:
Mapping: Small -> 0, Medium -> 1, Large -> 2.
Input: ["Medium", "Small", "Large"] -> Output: [1, 0, 2].

### 8. Second Concrete Example
Nominal feature "City": ["NY", "SF", "LA"].
One-Hot Matrix:
NY -> [1, 0, 0]
SF -> [0, 1, 0]
LA -> [0, 0, 1]

### 9. Common Mistakes
- Applying Mean to Nominal/Ordinal features.
- Performing division or ratio calculations on Interval data (e.g., 20°C is not "twice as hot" as 10°C).

### 10. AI Connection
Neural Networks require numerical input vectors. Proper feature encoding preserves data geometry without introducing artificial distance artifacts.

### 11. Algorithm Connection
- Decision Trees handle mixed nominal/ordinal features natively.
- Logistic Regression / SVMs require One-Hot or Target Encoding.

### 12. Practical Interpretation
Data type dictates pre-processing pipelines: Imputation strategy, Scaling, and Encoding.

### 13. Interview Insight
Question: Why shouldn't you use Ordinal Encoding for Nominal data like Country Names?
Answer: Ordinal encoding assigns implicit numbers (1, 2, 3), forcing linear models to assume Country 3 > Country 2 > Country 1 and imposing false geometric distance in feature space.

### 14. Summary
Categorizing features into Nominal, Ordinal, Interval, and Ratio ensures mathematically sound model inputs.
