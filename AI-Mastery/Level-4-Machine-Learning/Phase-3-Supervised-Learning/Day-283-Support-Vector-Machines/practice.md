# Practice Questions — Day 283

## Basic Questions
1. Define classification in Machine Learning.
2. What is a Confusion Matrix? List its 4 components.
3. Define Precision, Recall, and F1-Score.

## Conceptual Questions
4. Why is Accuracy misleading when evaluating a rare fraud detection model (0.1% fraud rate)?
5. Explain the Sigmoid function and why it is used in Logistic Regression.
6. Compare Decision Trees vs Random Forests in terms of variance and overfitting.

## Calculation Questions
7. Given $TP=40, TN=50, FP=10, FN=0$, compute Accuracy, Precision, Recall, and F1-Score.
8. Compute Entropy for a node with 5 positive and 5 negative samples.

## Implementation Questions
9. Write a Python function computing the Sigmoid activation $\sigma(z) = \frac{1}{1 + e^{-z}}$.
10. Build a scikit-learn `RandomForestClassifier` and plot feature importances.

## ML Reasoning Questions
11. You are building a cancer detection classifier where missing a positive case is fatal. Should you optimize for Precision or Recall? Explain.
12. A Decision Tree gets 100% training accuracy but 60% test accuracy. Recommend 3 hyperparameters to tune.

## Dataset Questions
13. Identify class distribution ratios in a given target vector $y$.

## Interview Questions
14. Prove that the derivative of the Sigmoid function is $\sigma'(z) = \sigma(z)(1 - \sigma(z))$.
15. How does the Kernel Trick allow SVMs to construct non-linear decision boundaries without explicitly computing high-dimensional feature vectors?
