# Day 65 Solutions: Measures of Central Tendency

## Level 1: Basic Concepts
1. Mean: sum/n; Median: middle sorted value; Mode: most frequent value.
2. Mean.
3. Mode.
4. Mean Squared Error (MSE / L2 Loss).
5. Mean Absolute Error (MAE / L1 Loss).

## Level 2: Calculation
6. Mean = 62/6 = 10.33; Sorted [5, 8, 8, 12, 17, 20] -> Median = (8+12)/2 = 10; Mode = 8.
7. G = sqrt(2 * 8) = sqrt(16) = 4.
8. H = 2 / (1/40 + 1/60) = 2 / (5/120) = 240 / 5 = 48 mph.
9. F1 = 2*(0.6*0.8)/(0.6+0.8) = 0.96 / 1.4 = 0.6857.
10. Median = (9 + 12) / 2 = 10.5.

## Level 3: Conceptual
11. d/dc [ sum (x_i - c)^2 ] = -2 sum (x_i - c) = 0 => sum x_i = n c => c = x_bar.
12. Derivative of |x_i - c| is -1 for x_i > c and +1 for x_i < c. Setting sum = 0 requires equal number of points above and below c => c = Median.
13. AM-GM-HM inequality: H <= G <= A with equality iff all x_i are equal.
14. Symmetry means left and right halves mirror around peak, forcing peak (mode), middle 50% (median), and center of mass (mean) to coincide.
15. In right-skewed data: Mode < Median < Mean (outliers pull mean right).

## Level 4: AI Applications
16. L1 MAE penalty grows linearly, whereas MSE squares outlier errors, pulling model predictions severely towards noise.
17. Median is unaffected by extreme skewed values, avoiding corrupted imputations.
18. Harmonic mean forces both precision and recall to be high for a good F1 score.
19. Outliers heavily pull cluster centroids (means), distorting cluster boundaries.
20. Replaces batch statistics during evaluation to ensure deterministic predictions.

## Level 5: Interview Solutions
21. Set dL/dc = 0 => -2 sum (y_i - c) = 0 => sum y_i - n c = 0 => c = (1/n) sum y_i = y_bar.
22. Speed is distance/time. When distance is constant, time is inversely proportional to speed; harmonic mean averages rates correctly over fixed distance.
23. Mean imputation preserves total sum but is sensitive to outliers; Median imputation is robust to outliers and preserves rank distribution better.
