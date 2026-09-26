# Day 154 Theory: Features and Targets

### 1. What Is It?
In Machine Learning, Features ($X$) are predictive input variables, while the Target ($y$) is the output ground-truth variable the algorithm learns to predict.

### 2. Feature & Target Taxonomy
- **Continuous Feature**: Real numbers with infinite granularity (e.g. `Height = 175.4 cm`).
- **Discrete Feature**: Count integers (e.g. `Number_of_Children = 2`).
- **Nominal Feature**: Unordered categories (e.g. `Color = ['Red', 'Blue']`).
- **Ordinal Feature**: Ordered categories (e.g. `Education = ['High School', 'Bachelors', 'PhD']`).
- **Regression Target**: Continuous value (e.g. `House Price`).
- **Classification Target**: Discrete class label (e.g. `Spam vs Not Spam`).

### 3. Summary
Separating $X$ and $y$ and identifying feature variable types determines necessary encoding and scaling transformations.
