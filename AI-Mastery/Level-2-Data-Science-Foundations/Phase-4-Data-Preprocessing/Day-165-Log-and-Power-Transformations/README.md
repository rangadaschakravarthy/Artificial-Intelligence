# Day 165 — Log and Power Transformations

## Learning Objectives
- Compress right-skewed feature distributions to normal Gaussian shapes using Log and Power transformations.
- Apply `np.log1p()` for features containing zeros.
- Master Box-Cox and Yeo-Johnson transformations using `sklearn.preprocessing.PowerTransformer`.

## Prerequisites
- Day 164: Feature Transformation

## Topics Covered
- Natural Log Transformation: $y = \ln(x)$ and $y = \ln(1 + x)$ (`np.log1p()`)
- Inverse operation: Exponential $e^x$ (`np.expm1()`)
- Box-Cox Transformation ($x > 0$ required)
- Yeo-Johnson Transformation (handles zero and negative values)
- `sklearn.preprocessing.PowerTransformer` API

## Practical Work
- Apply `np.log1p()` to a heavily right-skewed income distribution and measure the reduction in skewness.

## Difficulty
Intermediate
