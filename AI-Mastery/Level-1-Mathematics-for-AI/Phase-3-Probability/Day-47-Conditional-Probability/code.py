import numpy as np

def compute_confusion_metrics(TP, FP, FN, TN):
    precision = TP / (TP + FP) if (TP + FP) > 0 else 0.0
    recall = TP / (TP + FN) if (TP + FN) > 0 else 0.0
    specificity = TN / (TN + FP) if (TN + FP) > 0 else 0.0
    accuracy = (TP + TN) / (TP + FP + FN + TN)
    return precision, recall, specificity, accuracy

def main():
    print("--- Day 47: Conditional Probability ---")
    
    # 1. Direct Conditional Probability Calculation
    # P(Cat AND Whiskers) = 0.25, P(Whiskers) = 0.30
    P_both = 0.25
    P_whiskers = 0.30
    P_cat_given_whiskers = P_both / P_whiskers
    
    print("
1. Animal Classification Conditional Probability:")
    print(f"  P(Whiskers):               {P_whiskers:.2f}")
    print(f"  P(Cat AND Whiskers):       {P_both:.2f}")
    print(f"  P(Cat | Whiskers):         {P_cat_given_whiskers:.4f}")
    
    # 2. Confusion Matrix as Conditional Probabilities
    TP, FP, FN, TN = 150, 50, 25, 775
    prec, rec, spec, acc = compute_confusion_metrics(TP, FP, FN, TN)
    
    print("
2. Machine Learning Confusion Matrix Metrics:")
    print(f"  Counts: TP={TP}, FP={FP}, FN={FN}, TN={TN}")
    print(f"  Precision   P(Y=1 | Y_hat=1): {prec:.4f}")
    print(f"  Recall      P(Y_hat=1 | Y=1): {rec:.4f}")
    print(f"  Specificity P(Y_hat=0 | Y=0): {spec:.4f}")
    print(f"  Accuracy:                      {acc:.4f}")

if __name__ == "__main__":
    main()
