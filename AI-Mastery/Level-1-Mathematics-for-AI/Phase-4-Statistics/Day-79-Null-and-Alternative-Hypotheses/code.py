import numpy as np

def generate_ai_hypotheses(scenario_type, metric_name, value=0.0):
    scenarios = {
        'ab_test_lift': (
            f"H0: {metric_name}_variant - {metric_name}_control <= 0.0",
            f"Ha: {metric_name}_variant - {metric_name}_control > 0.0 (One-Tailed Right)"
        ),
        'model_equivalence': (
            f"H0: {metric_name}_modelA - {metric_name}_modelB = 0.0",
            f"Ha: {metric_name}_modelA - {metric_name}_modelB != 0.0 (Two-Tailed)"
        ),
        'latency_threshold': (
            f"H0: {metric_name} >= {value} ms",
            f"Ha: {metric_name} < {value} ms (One-Tailed Left)"
        ),
        'feature_relevance': (
            f"H0: beta_{metric_name} = 0.0",
            f"Ha: beta_{metric_name} != 0.0 (Two-Tailed)"
        )
    }
    return scenarios.get(scenario_type, ("H0: Undefined", "Ha: Undefined"))

def main():
    print("--- Day 79: Null and Alternative Hypotheses ---")
    
    test_cases = [
        ('ab_test_lift', 'Conversion_Rate', 0.0),
        ('model_equivalence', 'Accuracy', 0.0),
        ('latency_threshold', 'P99_Latency', 50.0),
        ('feature_relevance', 'Income', 0.0)
    ]
    
    print("AI Scenario Hypothesis Formulations:")
    print("==================================================")
    for s_type, m_name, val in test_cases:
        h0, ha = generate_ai_hypotheses(s_type, m_name, val)
        print(f"Scenario: [{s_type.upper()}]")
        print(f"  Null Hypothesis:        {h0}")
        print(f"  Alternative Hypothesis: {ha}")
        print("--------------------------------------------------")

if __name__ == "__main__":
    main()
