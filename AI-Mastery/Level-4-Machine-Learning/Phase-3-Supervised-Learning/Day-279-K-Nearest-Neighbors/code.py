# Code — Day 279: K-Nearest Neighbors ($k$-NN)
import numpy as np
from sklearn.datasets import make_classification
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix, classification_report, roc_auc_score

def demonstrate_classification():
    print("--- Day 279: K-Nearest Neighbors ($k$-NN) Demo ---")
    
    # 1. Generate Binary Dataset
    X, y = make_classification(n_samples=200, n_features=4, n_informative=3, random_state=42)
    
    # 2. Fit Logistic Regression & Random Forest
    log_reg = LogisticRegression().fit(X, y)
    rf = RandomForestClassifier(n_estimators=50, random_state=42).fit(X, y)
    
    y_pred_log = log_reg.predict(X)
    y_prob_log = log_reg.predict_proba(X)[:, 1]
    
    print("Logistic Regression Confusion Matrix:\n", confusion_matrix(y, y_pred_log))
    print(f"ROC-AUC Score: {roc_auc_score(y, y_prob_log):.3f}")
    print("\nClassification Report:\n", classification_report(y, y_pred_log))

if __name__ == "__main__":
    demonstrate_classification()
