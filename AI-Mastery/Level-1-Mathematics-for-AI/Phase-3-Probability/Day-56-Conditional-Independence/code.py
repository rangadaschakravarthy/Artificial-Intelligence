import numpy as np

def naive_bayes_predict(priors, likelihoods, test_sample):
    # priors: [P(Y=0), P(Y=1)]
    # likelihoods: 2xD matrix of P(X_i=1 | Y=y)
    n_classes = len(priors)
    log_posteriors = np.zeros(n_classes)
    
    for c in range(n_classes):
        log_prior = np.log(priors[c])
        # Log likelihood under conditional independence
        feature_probs = likelihoods[c]
        # P(x_i | Y) if x_i=1 else 1 - P(x_i | Y)
        sample_probs = np.where(test_sample == 1, feature_probs, 1.0 - feature_probs)
        log_likelihood = np.sum(np.log(sample_probs))
        log_posteriors[c] = log_prior + log_likelihood
        
    # Softmax / Normalize probabilities
    exp_log = np.exp(log_posteriors - np.max(log_posteriors))
    probs = exp_log / np.sum(exp_log)
    return probs

def main():
    print("--- Day 56: Conditional Independence & Naive Bayes ---")
    
    # 2 Classes: [Ham, Spam]
    priors = np.array([0.7, 0.3])
    # 3 Features: ["free", "winner", "meeting"]
    likelihoods = np.array([
        [0.05, 0.01, 0.40], # P(X_i=1 | Ham)
        [0.80, 0.60, 0.02]  # P(X_i=1 | Spam)
    ])
    
    # Test sample: Email contains "free" (1) and "winner" (1), but NOT "meeting" (0)
    sample = np.array([1, 1, 0])
    
    probs = naive_bayes_predict(priors, likelihoods, sample)
    
    print(f"
Test Email Features [free=1, winner=1, meeting=0]:")
    print(f"  P(Ham | Features):  {probs[0]:.4f}")
    print(f"  P(Spam | Features): {probs[1]:.4f} ({probs[1]*100:.2f}%)")

if __name__ == "__main__":
    main()
