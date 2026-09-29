# Day 160 Solutions: Normalization

## Level 1 — Basic
1. $[0, 1]$.
2. $x' = \frac{x - x_{\min}}{x_{\max} - x_{\min}}$.
3. The presence of an extreme outlier inflates $x_{\max}$ (or decreases $x_{\min}$), compressing non-outlier data into an extremely narrow sub-interval close to 0 or 1.

## Level 2 — Coding
1. `scaler = MinMaxScaler(feature_range=(-1, 1)); df['Scaled'] = scaler.fit_transform(df[['Col']])`

## Level 3 — Data Analysis
1. Computer Vision and Image Processing, where raw pixel intensity values are naturally bounded in $[0, 255]$ and normalized to $[0, 1]$ for Neural Network inputs.
