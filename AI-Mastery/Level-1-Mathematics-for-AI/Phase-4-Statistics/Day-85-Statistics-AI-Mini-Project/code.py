import numpy as np
from scipy import stats

class ABTestingStatisticalEngine:
    def __init__(self, alpha=0.05):
        self.alpha = alpha

    def _cohens_d(self, g1, g2):
        n1, n2 = len(g1), len(g2)
        s1, s2 = np.var(g1, ddof=1), np.var(g2, ddof=1)
        s_pooled = np.sqrt(((n1 - 1)*s1 + (n2 - 1)*s2) / (n1 + n2 - 2))
        return (np.mean(g2) - np.mean(g1)) / s_pooled if s_pooled > 0 else 0.0

    def evaluate_experiment(self, control, variant, metric_name="Metric"):
        # 1. Normality Check (Shapiro-Wilk)
        _, p_norm_ctrl = stats.shapiro(control[:100])
        _, p_norm_var = stats.shapiro(variant[:100])
        both_normal = (p_norm_ctrl > self.alpha) and (p_norm_var > self.alpha)

        # 2. Test Selection & Execution
        if both_normal:
            # Check Variance Homogeneity
            _, p_levene = stats.levene(control, variant)
            equal_var = p_levene > self.alpha
            if equal_var:
                test_name = "Student's Independent 2-Sample t-Test"
                stat, p_val = stats.ttest_ind(control, variant, equal_var=True)
            else:
                test_name = "Welch's 2-Sample t-Test (Unequal Variances)"
                stat, p_val = stats.ttest_ind(control, variant, equal_var=False)
        else:
            test_name = "Mann-Whitney U Test (Non-Parametric)"
            stat, p_val = stats.mannwhitneyu(control, variant, alternative='two-sided')

        # 3. Lift & Effect Size
        mean_ctrl = np.mean(control)
        mean_var = np.mean(variant)
        abs_lift = mean_var - mean_ctrl
        rel_lift = (abs_lift / mean_ctrl) * 100 if mean_ctrl != 0 else 0.0
        d_val = self._cohens_d(control, variant)

        # 4. Decision
        significant = p_val < self.alpha

        print("==================================================")
        print(f"--- A/B TESTING STATISTICAL REPORT: [{metric_name.upper()}] ---")
        print("==================================================")
        print(f"  Control (Variant A) Mean: {mean_ctrl:.4f}")
        print(f"  Treatment (Variant B) Mean: {mean_var:.4f}")
        print(f"  Absolute Lift:             {abs_lift:+.4f}")
        print(f"  Relative Lift:             {rel_lift:+.2f}%")
        print(f"  Diagnostic Test Selected:  {test_name}")
        print(f"  Test Statistic:            {stat:.4f}")
        print(f"  p-value:                   {p_val:.4e}")
        print(f"  Cohen's d Effect Size:     {d_val:.4f}")
        print(f"  Final Decision:            {'APPROVED FOR DEPLOYMENT (Significant Lift!)' if significant else 'REJECTED (Not Significant)'}")
        print("==================================================")

def main():
    print("==================================================")
    print("LEVEL 1 — MATHEMATICS FOR AI: CAPSTONE DAY 85")
    print("==================================================")
    
    np.random.seed(42)
    # Simulate A/B Test Data: Model A (Control) vs Model B (Treatment)
    control_latency = np.random.normal(loc=50.0, scale=8.0, size=100)
    variant_latency = np.random.normal(loc=46.5, scale=8.0, size=100) # True 3.5ms reduction
    
    engine = ABTestingStatisticalEngine(alpha=0.05)
    engine.evaluate_experiment(control_latency, variant_latency, metric_name="Execution Latency (ms)")

if __name__ == "__main__":
    main()
