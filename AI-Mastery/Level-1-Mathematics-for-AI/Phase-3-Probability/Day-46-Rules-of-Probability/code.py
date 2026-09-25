import numpy as np

def simulate_ensemble_voting(n_models=3, model_acc=0.80, n_simulations=100000):
    # Simulate predictions of n independent models: 1 for correct, 0 for wrong
    predictions = np.random.binomial(1, model_acc, size=(n_simulations, n_models))
    correct_counts = np.sum(predictions, axis=1)
    # Ensemble predicts correctly if majority (> n_models / 2) are correct
    majority_threshold = (n_models // 2) + 1
    ensemble_correct = np.mean(correct_counts >= majority_threshold)
    return ensemble_correct

def main():
    print("--- Day 46: Rules of Probability ---")
    
    # 1. Addition and Complement Rules Demonstration
    P_A = 0.6
    P_B = 0.5
    P_A_and_B = 0.3
    
    P_A_or_B = P_A + P_B - P_A_and_B
    P_A_comp = 1 - P_A
    
    print("
1. Probability Rules Calculation:")
    print(f"  P(A) = {P_A}, P(B) = {P_B}, P(A AND B) = {P_A_and_B}")
    print(f"  P(A OR B) = P(A) + P(B) - P(A AND B) = {P_A_or_B:.2f}")
    print(f"  P(A Complement) = 1 - P(A) = {P_A_comp:.2f}")
    
    # 2. Ensemble Classifier Simulation vs Analytical Formula
    n_sims = 100000
    sim_acc = simulate_ensemble_voting(n_models=3, model_acc=0.80, n_simulations=n_sims)
    analytical_acc = (0.8**3) + 3 * (0.8**2) * 0.2
    
    print("
2. Ensemble Learning Reliability (3 Models @ 80% Accuracy):")
    print(f"  Single Model Accuracy:     80.00%")
    print(f"  Analytical Ensemble Acc:  {analytical_acc*100:.2f}%")
    print(f"  Simulated Ensemble Acc:   {sim_acc*100:.2f}%")

if __name__ == "__main__":
    main()
