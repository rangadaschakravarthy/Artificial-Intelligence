import numpy as np

def main():
    # 1. Element-wise Arithmetic
    a = np.array([10, 20, 30])
    b = np.array([2, 4, 5])
    
    print("a + b:", a + b)
    print("a * b:", a * b)
    print("a / b:", a / b)
    
    # 2. Hadamard vs Matrix Product
    A = np.array([[1, 2], [3, 4]])
    B = np.array([[10, 20], [30, 40]])
    
    print("
Hadamard Product (A * B):
", A * B)
    print("Matrix Product (A @ B):   
", A @ B)
    
    # 3. In-Place Operations
    x = np.ones(3)
    x += 5
    print("
In-place x += 5:", x)
    
    # 4. MSE Loss Calculation
    y_true = np.array([1.0, 0.0, 1.0])
    y_pred = np.array([0.8, 0.2, 0.9])
    mse = np.mean((y_pred - y_true) ** 2)
    print(f"
MSE Loss: {mse:.4f}")

if __name__ == "__main__":
    main()
