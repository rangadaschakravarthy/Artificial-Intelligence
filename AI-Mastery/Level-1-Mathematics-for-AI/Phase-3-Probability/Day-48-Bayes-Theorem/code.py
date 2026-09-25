import numpy as np

def bayes_update(prior, likelihood_true, likelihood_false):
    # prior = P(H)
    # likelihood_true = P(E|H)
    # likelihood_false = P(E|H_c)
    evidence = (likelihood_true * prior) + (likelihood_false * (1.0 - prior))
    posterior = (likelihood_true * prior) / evidence
    return posterior, evidence

def main():
    print("--- Day 48: Bayes' Theorem ---")
    
    # 1. Medical Diagnosis Base Rate Fallacy Example
    prior_disease = 0.001
    sensitivity = 0.99   # P(+ | Disease)
    false_pos_rate = 0.05 # P(+ | No Disease)
    
    post_disease, total_evidence = bayes_update(prior_disease, sensitivity, false_pos_rate)
    
    print("
1. Medical Diagnostic Bayesian Update:")
    print(f"  Prior P(Disease):                 {prior_disease:.4f}")
    print(f"  Sensitivity P(+ | Disease):       {sensitivity:.4f}")
    print(f"  False Alarm Rate P(+ | No Disease):{false_pos_rate:.4f}")
    print(f"  Total Positive Rate P(+):         {total_evidence:.4f}")
    print(f"  Posterior P(Disease | +):         {post_disease:.4f} ({post_disease*100:.2f}%)")
    
    # 2. Sequential Bayesian Updating (Spam Classifier 2 Words)
    print("
2. Sequential Bayesian Update with 2 Words:")
    prior_spam = 0.30
    # Word 1: "Lottery" (Likelihood ratio 10:1)
    post_step1, _ = bayes_update(prior_spam, 0.50, 0.05)
    # Word 2: "Winner" (Likelihood ratio 5:1)
    post_step2, _ = bayes_update(post_step1, 0.40, 0.08)
    
    print(f"  Initial Prior P(Spam):           {prior_spam:.4f}")
    print(f"  After Word 1 ('Lottery'): Posterior = {post_step1:.4f}")
    print(f"  After Word 2 ('Winner'):  Posterior = {post_step2:.4f}")

if __name__ == "__main__":
    main()
