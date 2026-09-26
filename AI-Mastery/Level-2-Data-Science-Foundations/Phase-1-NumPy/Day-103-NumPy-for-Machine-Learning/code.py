import numpy as np

def main():
    # 1. Activation Functions
    z = np.array([-2.0, 0.0, 2.0])
    sigmoid = 1.0 / (1.0 + np.exp(-z))
    relu = np.maximum(0, z)
    
    print("Logits: ", z)
    print("Sigmoid:", np.round(sigmoid, 4))
    print("ReLU:   ", relu)
    
    # 2. Linear Regression Forward & Loss
    rng = np.random.default_rng(42)
    X = np.array([[1.0], [2.0], [3.0], [4.0]])
    y = np.array([3.0, 5.0, 7.0, 9.0]) # y = 2*x + 1
    
    w = 0.0
    b = 0.0
    lr = 0.05
    
    for epoch in range(200):
        y_pred = (X.flatten() * w) + b
        loss = np.mean((y_pred - y) ** 2)
        
        # Gradients
        dw = (2 / len(X)) * np.sum((y_pred - y) * X.flatten())
        db = (2 / len(X)) * np.sum(y_pred - y)
        
        # Updates
        w -= lr * dw
        b -= lr * db
    
    print(f"
Trained Model: y = {w:.2f}*x + {b:.2f}")
    print(f"Final MSE Loss: {loss:.6f}")

if __name__ == "__main__":
    main()
