import numpy as np

class ScratchGaussianNB:
    def fit(self, X, y):
        self.classes = np.unique(y)
        n_classes = len(self.classes)
        n_features = X.shape[1]
        
        self.means = np.zeros((n_classes, n_features))
        self.vars = np.zeros((n_classes, n_features))
        self.priors = np.zeros(n_classes)
        
        for idx, c in enumerate(self.classes):
            X_c = X[y == c]
            self.means[idx, :] = np.mean(X_c, axis=0)
            self.vars[idx, :] = np.var(X_c, axis=0) + 1e-9 # Add epsilon for stability
            self.priors[idx] = X_c.shape[0] / float(X.shape[0])
            
    def predict(self, X):
        log_posteriors = []
        for idx, c in enumerate(self.classes):
            log_prior = np.log(self.priors[idx])
            # Gaussian Log Likelihood
            mean = self.means[idx]
            var = self.vars[idx]
            log_likelihood = -0.5 * np.sum(np.log(2 * np.pi * var) + ((X - mean)**2) / var, axis=1)
            log_posteriors.append(log_prior + log_likelihood)
            
        log_posteriors = np.array(log_posteriors) # Shape: (K, N)
        return self.classes[np.argmax(log_posteriors, axis=0)]

def main():
    print("--- Day 60: Naive Bayes Algorithm Mathematics ---")
    
    # Generate synthetic 2-class dataset
    np.random.seed(42)
    X0 = np.random.normal(loc=0.0, scale=1.0, size=(100, 2))
    X1 = np.random.normal(loc=2.5, scale=1.0, size=(100, 2))
    X = np.vstack([X0, X1])
    y = np.array([0]*100 + [1]*100)
    
    # Train Scratch Gaussian Naive Bayes
    gnb = ScratchGaussianNB()
    gnb.fit(X, y)
    
    # Evaluate Accuracy
    preds = gnb.predict(X)
    acc = np.mean(preds == y)
    
    print("
1. Scratch Gaussian Naive Bayes Results:")
    print(f"  Class 0 Learned Means: {gnb.means[0]}")
    print(f"  Class 1 Learned Means: {gnb.means[1]}")
    print(f"  Training Accuracy:     {acc * 100:.2f}%")

if __name__ == "__main__":
    main()
