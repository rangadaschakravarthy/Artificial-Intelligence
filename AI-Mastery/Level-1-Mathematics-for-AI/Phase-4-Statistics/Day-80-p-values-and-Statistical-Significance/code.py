import numpy as np
from scipy import stats

def cohens_d(group1, group2):
    n1, n2 = len(group1), len(group2)
    s1, s2 = np.var(group1, ddof=1), np.var(group2, ddof=1)
    s_pooled = np.sqrt(((n1 - 1)*s1 + (n2 - 1)*s2) / (n1 + n2 - 2))
    d = (np.mean(group2) - np.mean(group1)) / s_pooled
    return d

def main():
    print("--- Day 80: p-values and Statistical Significance ---")
    
    # Model A vs Model B Accuracy Cross-Validation Scores
    np.random.seed(42)
    scores_A = np.random.normal(loc=0.85, scale=0.03, size=30)
    scores_B = np.random.normal(loc=0.87, scale=0.03, size=30) # +2% true lift
    
    # 2-Sample Independent t-Test
    t_stat, p_val = stats.ttest_ind(scores_A, scores_B)
    d_val = cohens_d(scores_A, scores_B)
    
    alpha = 0.05
    
    print("1. Model B vs Model A Evaluation Report:")
    print(f"  Model A Mean Accuracy: {np.mean(scores_A)*100:.2f}%")
    print(f"  Model B Mean Accuracy: {np.mean(scores_B)*100:.2f}%")
    print(f"  Absolute Lift:         {(np.mean(scores_B) - np.mean(scores_A))*100:+.2f}%")
    print(f"  Calculated t-Stat:     {t_stat:.4f}")
    print(f"  Computed p-value:      {p_val:.4f}")
    print(f"  Cohen's d Effect Size: {d_val:.4f} ({'Medium' if 0.5 <= abs(d_val) < 0.8 else 'Large' if abs(d_val)>=0.8 else 'Small'})")
    print(f"  Statistical Decision:  {'REJECT H0 (Statistically Significant Lift!)' if p_val < alpha else 'FAIL TO REJECT H0'}")

if __name__ == "__main__":
    main()
