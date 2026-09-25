import numpy as np
from scipy import stats

class UnifiedStatisticalTester:
    @staticmethod
    def test_means(g1, g2, paired=False, alpha=0.05):
        if paired:
            stat, p_val = stats.ttest_rel(g1, g2)
            test_name = "Paired t-Test"
        else:
            stat, p_val = stats.ttest_ind(g1, g2, equal_var=False)
            test_name = "Welch's Independent 2-Sample t-Test"
            
        print(f"[{test_name}]")
        print(f"  Test Statistic: {stat:.4f}")
        print(f"  p-value:        {p_val:.4f}")
        print(f"  Result:         {'STATISTICALLY SIGNIFICANT (p < 0.05)' if p_val < alpha else 'NOT SIGNIFICANT'}")

def main():
    print("--- Day 82: Statistical Tests Suite ---")
    
    np.random.seed(42)
    # Scenario A: Paired Cross-Validation Folds (Model A vs Model B on 10 folds)
    m1_cv = np.array([0.85, 0.87, 0.84, 0.88, 0.86, 0.85, 0.89, 0.84, 0.86, 0.87])
    m2_cv = np.array([0.88, 0.89, 0.86, 0.90, 0.88, 0.87, 0.91, 0.86, 0.88, 0.89]) # Paired higher
    
    print("1. Model Comparison on 10 Identical CV Folds (Paired Design):")
    UnifiedStatisticalTester.test_means(m1_cv, m2_cv, paired=True)
    
    # Scenario B: Independent Cohorts (User Group 1 vs Group 2)
    grp1 = np.random.normal(50.0, 10.0, 50)
    grp2 = np.random.normal(55.0, 12.0, 60)
    
    print("
2. Independent User Cohort Latencies (Unpaired Design):")
    UnifiedStatisticalTester.test_means(grp1, grp2, paired=False)

if __name__ == "__main__":
    main()
