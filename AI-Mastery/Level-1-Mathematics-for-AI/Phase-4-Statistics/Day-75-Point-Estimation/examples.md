# Day 75 Worked Examples: Point Estimation

## Example 1: Very Easy — Unbiased Mean Estimator
Sample: [4, 6, 8]. Point estimate x_bar = 18 / 3 = 6.0.

## Example 2: Beginner — Evaluating Bias
Estimator T = x_bar + 2. E[T] = E[x_bar] + 2 = μ + 2.
Bias = (μ + 2) - μ = +2. (Biased estimator!).

## Example 3: Intermediate — Computing MSE
Estimator A: Bias = 0, Var = 10 => MSE = 0^2 + 10 = 10.
Estimator B: Bias = 1, Var = 4 => MSE = 1^2 + 4 = 5.
Estimator B is preferred because its total MSE (5) is lower despite being biased!

## Example 4: AI Focus — Ridge Regression Bias-Variance Tradeoff
OLS estimator: Unbiased, high variance when features are collinear.
Ridge estimator: Biased by λ, but variance drops significantly, lowering test set MSE.

## Example 5: Real-World AI — Estimating Model Accuracy
Validation Accuracy on n=1,000 test images = 92.4%. 92.4% is the point estimate of true generalization accuracy.
