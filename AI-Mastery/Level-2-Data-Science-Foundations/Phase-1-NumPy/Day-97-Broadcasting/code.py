import numpy as np

def main():
    # 1. Scalar & Row Broadcasting
    M = np.ones((3, 3))
    print("Matrix M:
", M)
    print("M + 10 (Scalar):
", M + 10)
    
    v_row = np.array([1, 2, 3])
    print("
M + v_row (Row-wise):
", M + v_row)
    
    # 2. Column Broadcasting
    v_col = v_row[:, np.newaxis] # (3, 1)
    print("
M + v_col (Column-wise):
", M + v_col)
    
    # 3. Outer Grid Construction
    x = np.array([1, 2, 3])
    y = np.array([10, 20])
    grid = x[:, np.newaxis] + y[np.newaxis, :]
    print("
Outer Grid (3, 1) + (1, 2) -> (3, 2):
", grid)
    
    # 4. Feature Standardization Demo
    X = np.array([[10.0, 100.0], [20.0, 200.0], [30.0, 300.0]])
    means = X.mean(axis=0)
    print("
Feature Means:", means)
    print("Centered X (X - means):
", X - means)

if __name__ == "__main__":
    main()
