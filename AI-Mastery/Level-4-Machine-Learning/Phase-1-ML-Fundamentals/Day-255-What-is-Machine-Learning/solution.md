# Practice Solutions — Day 255

## Basic Solutions
1. Machine Learning is a branch of AI where computer systems learn patterns from data to make predictions without explicit step-by-step programming.
2. Task ($T$), Experience ($E$), and Performance Measure ($P$).
3. Traditional programming takes Data + Rules to output Answers; ML takes Data + Answers to learn Rules/Models.

## Conceptual Solutions
4. Natural language contains infinite nuances, idioms, and context dependencies that create an unmaintainable combinatorial explosion of hand-coded `if-else` rules.
5. Generalization is a model's ability to make accurate predictions on new, unseen data that was not part of its training set.
6. Choose traditional programming when business rules are deterministic, fully known, regulatory-mandated, and simple (e.g., tax calculation).

## Calculation Solutions
7. For $x=2: \hat{y} = 3(2)+5 = 11$. For $x=4: \hat{y} = 17$. For $x=6: \hat{y} = 23$.
8. Errors: $|10-11|=1$, $|20-19|=1$, $|30-32|=2$. Mean Absolute Error = $(1+1+2)/3 = 1.33$.

## Implementation Solutions
9. Python Rule-Based Function:
```python
def is_spam_rule(text):
    keywords = ["free", "winner", "cash prize", "urgent"]
    return any(word in text.lower() for word in keywords)
```
10. Scikit-learn Linear Regression:
```python
import numpy as np
from sklearn.linear_model import LinearRegression

X = np.array([[1], [2], [3], [4], [5]])
y = np.array([3, 5, 7, 9, 11])
model = LinearRegression().fit(X, y)
print("Slope:", model.coef_[0], "Intercept:", model.intercept_)
```

## ML Reasoning Solutions
11. Yes. Loan approval depends on complex non-linear interactions among income, credit history, debt ratio, and macroeconomic factors where historical data exists.
12. No. Tax bracket calculations are exact deterministic legal rules. Machine learning would introduce unnecessary uncertainty into an exact formula.

## Dataset Questions
13. Input Feature $X$: Study hours (independent variable). Target $y$: Final exam score (dependent variable).

## Interview Solutions
14. Task $T$: Detect obstacles and steer vehicle safely. Experience $E$: Millions of miles of camera/LiDAR data collected. Performance $P$: Disengagement rate per 1,000 miles.
15. While massive clean data often compensates for simpler models, poor quality/noisy data or fundamentally flawed model assumptions cannot be saved by data volume alone.
