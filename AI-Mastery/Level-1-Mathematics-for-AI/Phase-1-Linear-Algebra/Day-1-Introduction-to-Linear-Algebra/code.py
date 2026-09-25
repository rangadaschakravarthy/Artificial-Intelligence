# Day 1 — Introduction to Linear Algebra
# Implementation of basic scalar, vector, and matrix representations

import numpy as np

# 1. Manual Implementation (Pure Python)
def manual_linear_model(x_vec, weights, bias):
    """Calculates y = w^T * x + b using basic python lists"""
    dot_product = 0.0
    for i in range(len(x_vec)):
        dot_product += x_vec[i] * weights[i]
    return dot_product + bias

# Input data sample: House with 2000 sq ft, 3 bedrooms, 10 years old
house_features = [2000.0, 3.0, 10.0]
feature_weights = [120.0, 15000.0, -2000.0]
base_bias = 50000.0

predicted_price_manual = manual_linear_model(house_features, feature_weights, base_bias)
print(f"Manual Python Output: ${predicted_price_manual:,.2f}")

# 2. NumPy Implementation (Vectorized)
x_np = np.array(house_features)
w_np = np.array(feature_weights)
b_np = base_bias

predicted_price_numpy = np.dot(w_np, x_np) + b_np
print(f"NumPy Vectorized Output: ${predicted_price_numpy:,.2f}")

# Verify equality
assert np.isclose(predicted_price_manual, predicted_price_numpy)
print("Success: Manual calculation matches NumPy implementation!")
