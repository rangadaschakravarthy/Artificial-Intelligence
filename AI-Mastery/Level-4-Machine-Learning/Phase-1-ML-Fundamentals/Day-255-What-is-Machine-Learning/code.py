# Code — Day 255: What Is Machine Learning?
import numpy as np
from sklearn.linear_model import LinearRegression

def traditional_rule_predict(square_feet):
    """Traditional Rule-Based Approach: Hardcoded formula."""
    return square_feet * 200.0 + 15000.0

def machine_learning_approach():
    """Machine Learning Approach: Learn relationship from empirical data."""
    # Training Data: X (features: sqft), y (target: price in $)
    X_train = np.array([[800], [1000], [1200], [1500], [1800], [2000]])
    y_train = np.array([175000, 210000, 250000, 310000, 370000, 410000])

    # 1. Manual Fit (Least Squares Linear Slope/Intercept)
    X_mean = np.mean(X_train)
    y_mean = np.mean(y_train)
    w_manual = np.sum((X_train.ravel() - X_mean) * (y_train - y_mean)) / np.sum((X_train.ravel() - X_mean) ** 2)
    b_manual = y_mean - w_manual * X_mean

    # 2. Scikit-Learn Model Fit
    model = LinearRegression()
    model.fit(X_train, y_train)

    print("--- Machine Learning Paradigm Demonstration ---")
    print(f"Manual Calculated Formula : Price = {w_manual:.2f} * sqft + {b_manual:.2f}")
    print(f"Sklearn Learned Formula   : Price = {model.coef_[0]:.2f} * sqft + {model.intercept_:.2f}")

    # Test Prediction for 1400 sqft house
    test_sqft = np.array([[1400]])
    pred_rule = traditional_rule_predict(1400)
    pred_ml = model.predict(test_sqft)[0]

    print(f"\nPrediction for 1400 sq ft house:")
    print(f"  Traditional Rule Output : ${pred_rule:,.2f}")
    print(f"  Machine Learning Output  : ${pred_ml:,.2f}")

if __name__ == "__main__":
    machine_learning_approach()
