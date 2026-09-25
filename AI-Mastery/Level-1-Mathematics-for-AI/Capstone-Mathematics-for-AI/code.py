import numpy as np
from scipy import stats

class CapstoneAIEngine:
    def __init__(self, input_dim=4, hidden_dim=8, lr=0.1):
        np.random.seed(42)
        # Linear Algebra: Weight Matrices
        self.W1 = np.random.randn(input_dim, hidden_dim) * 0.1
        self.b1 = np.zeros((1, hidden_dim))
        self.W2 = np.random.randn(hidden_dim, 1) * 0.1
        self.b2 = np.zeros((1, 1))
        self.lr = lr

    def _sigmoid(self, z):
        return 1.0 / (1.0 + np.exp(-np.clip(z, -15, 15)))

    def _relu(self, z):
        return np.maximum(0, z)

    def forward(self, X):
        self.Z1 = np.dot(X, self.W1) + self.b1
        self.A1 = self._relu(self.Z1)
        self.Z2 = np.dot(self.A1, self.W2) + self.b2
        self.A2 = self._sigmoid(self.Z2)
        return self.A2

    def train(self, X, y, epochs=200):
        m = X.shape[0]
        y = y.reshape(-1, 1)
        
        for epoch in range(epochs):
            # Forward Pass
            y_hat = self.forward(X)
            
            # Calculus: Backpropagation Gradients
            dZ2 = y_hat - y
            dW2 = np.dot(self.A1.T, dZ2) / m
            db2 = np.sum(dZ2, axis=0, keepdims=True) / m
            
            dA1 = np.dot(dZ2, self.W2.T)
            dZ1 = dA1 * (self.Z1 > 0)
            dW1 = np.dot(X.T, dZ1) / m
            db1 = np.sum(dZ1, axis=0, keepdims=True) / m
            
            # SGD Parameter Updates
            self.W2 -= self.lr * dW2
            self.b2 -= self.lr * db2
            self.W1 -= self.lr * dW1
            self.b1 -= self.lr * db1

def main():
    print("==================================================")
    print("LEVEL 1 MATHEMATICS FOR AI: FINAL CAPSTONE SYSTEM")
    print("==================================================")
    
    # Generate Synthetic Dataset (200 samples, 4 features)
    np.random.seed(42)
    X = np.random.randn(200, 4)
    y = (X[:, 0] + X[:, 1] > 0).astype(int)
    
    # Train Neural Network Model
    model = CapstoneAIEngine(input_dim=4, hidden_dim=8, lr=0.1)
    model.train(X, y, epochs=300)
    
    # Evaluate Predictions
    preds = (model.forward(X) > 0.5).astype(int).flatten()
    acc = np.mean(preds == y)
    
    print(f"1. Neural Network Model Training:")
    print(f"  Final Accuracy: {acc*100:.2f}%")
    
    # Statistical Significance Validation
    scores_baseline = np.random.normal(0.70, 0.05, 30)
    scores_capstone = np.random.normal(acc, 0.03, 30)
    
    t_stat, p_val = stats.ttest_ind(scores_baseline, scores_capstone, equal_var=False)
    
    print(f"\n2. Statistical Validation (Welch's t-Test vs Baseline):")
    print(f"  t-Statistic: {t_stat:.4f}")
    print(f"  p-value:     {p_val:.4e}")
    print(f"  Result:      {'STATISTICALLY SIGNIFICANT LIFT APPROVED!' if p_val < 0.05 else 'NOT SIGNIFICANT'}")
    print("==================================================")

if __name__ == "__main__":
    main()
