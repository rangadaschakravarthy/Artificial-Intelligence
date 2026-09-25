import numpy as np
import re

class NaiveBayesTextClassifier:
    def __init__(self, alpha=1.0):
        self.alpha = alpha # Laplace smoothing parameter
        self.vocab = {}
        self.class_priors = {}
        self.word_counts = {}
        self.total_word_counts = {}
        
    def _clean_text(self, text):
        text = text.lower()
        words = re.findall(r'[a-z]+', text)
        return words

    def fit(self, docs, labels):
        n_docs = len(docs)
        classes = np.unique(labels)
        
        # Build Vocabulary
        vocab_set = set()
        for doc in docs:
            words = self._clean_text(doc)
            vocab_set.update(words)
        self.vocab = {word: idx for idx, word in enumerate(sorted(vocab_set))}
        vocab_size = len(self.vocab)
        
        # Initialize counts
        for c in classes:
            self.word_counts[c] = np.zeros(vocab_size)
            self.total_word_counts[c] = 0
            
        # Count words per class
        for doc, label in zip(docs, labels):
            words = self._clean_text(doc)
            for w in words:
                if w in self.vocab:
                    idx = self.vocab[w]
                    self.word_counts[label][idx] += 1
                    self.total_word_counts[label] += 1
                    
        # Compute Priors
        for c in classes:
            self.class_priors[c] = np.mean(labels == c)

    def predict_proba(self, docs):
        vocab_size = len(self.vocab)
        classes = list(self.class_priors.keys())
        results = []
        
        for doc in docs:
            words = self._clean_text(doc)
            log_posteriors = []
            
            for c in classes:
                log_prior = np.log(self.class_priors[c])
                # Laplace smoothed likelihoods
                denom = self.total_word_counts[c] + self.alpha * vocab_size
                log_lik = 0.0
                for w in words:
                    if w in self.vocab:
                        w_idx = self.vocab[w]
                        count = self.word_counts[c][w_idx]
                        prob = (count + self.alpha) / denom
                        log_lik += np.log(prob)
                log_posteriors.append(log_prior + log_lik)
                
            # Softmax normalization
            log_posteriors = np.array(log_posteriors)
            exp_scores = np.exp(log_posteriors - np.max(log_posteriors))
            probs = exp_scores / np.sum(exp_scores)
            results.append(probs)
            
        return np.array(results)

def bayesian_credit_risk_updater(prior_default, likelihood_ratios):
    # Odds formulation: Posterior_Odds = Prior_Odds * Product(Likelihood_Ratios)
    prior_odds = prior_default / (1.0 - prior_default)
    posterior_odds = prior_odds * np.prod(likelihood_ratios)
    posterior_default = posterior_odds / (1.0 + posterior_odds)
    return posterior_default

def main():
    print("==================================================")
    print("--- Day 62: Phase 3 Probability AI Mini-Project ---")
    print("==================================================")
    
    # Part 1: Spam Classification System
    train_docs = [
        "Free lottery prize money claim now",
        "Winner guaranteed cash bonus click link",
        "Cheap medical prescriptions buy now",
        "Meeting schedule project status update report",
        "Weekly team sync agenda discussion notes",
        "Please review attached project roadmap document"
    ]
    train_labels = np.array([1, 1, 1, 0, 0, 0]) # 1 = Spam, 0 = Ham
    
    nb = NaiveBayesTextClassifier(alpha=1.0)
    nb.fit(train_docs, train_labels)
    
    test_docs = [
        "Claim free cash bonus now",
        "Project status team meeting"
    ]
    probs = nb.predict_proba(test_docs)
    
    print("
1. Text Spam Classifier Predictions:")
    for doc, prob in zip(test_docs, probs):
        print(f"  Text: '{doc}'")
        print(f"    P(Ham):  {prob[0]:.4f}")
        print(f"    P(Spam): {prob[1]:.4f} -> Prediction: {'SPAM' if prob[1] > 0.5 else 'HAM'}")
        
    # Part 2: Bayesian Credit Risk Engine
    base_prior_default = 0.03 # 3% base risk
    # Sequential evidence likelihood ratios:
    # 1. Missed 60-day payment (LR = 8.0)
    # 2. Credit Card Utilization > 90% (LR = 4.0)
    evidences = [8.0, 4.0]
    
    updated_risk = bayesian_credit_risk_updater(base_prior_default, evidences)
    print("
2. Bayesian Credit Risk Assessment Engine:")
    print(f"  Base Population Default Prior: {base_prior_default*100:.2f}%")
    print(f"  Evidence 1 (Missed Payment LR=8.0)")
    print(f"  Evidence 2 (High Utilization LR=4.0)")
    print(f"  Updated Posterior Default Risk: {updated_risk*100:.2f}%")
    print("==================================================")

if __name__ == "__main__":
    main()
