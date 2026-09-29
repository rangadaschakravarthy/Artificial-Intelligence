# Theory — Statistical Tests (Z-Test, t-Test, Chi-Square Test)

## 1. Test Selection Decision Tree

```
                      What type of data do you have?
                                    |
          +-------------------------+-------------------------+
          |                                                   |
     Categorical                                          Continuous
          |                                                   |
  Chi-Square Test                              Are you comparing groups?
  - Independence (r x c)                                      |
  - Goodness-of-Fit                             +-------------+-------------+
                                                |                           |
                                           1 Group                     2 Groups
                                                |                           |
                                          1-Sample Test              Are groups paired?
                                          - Z-Test (Known sigma)            |
                                          - t-Test (Unknown sigma)    +-----+-----+
                                                                      |           |
                                                                   Paired     Independent
                                                                      |           |
                                                                  Paired     2-Sample t-Test
                                                                  t-Test     (Student / Welch)
```

## 2. Statistical Test Formulas Summary

| Test | Data Type | Test Statistic Formula | Degrees of Freedom |
| :--- | :--- | :--- | :--- |
| **1-Sample $Z$-Test** | Continuous | $Z = \frac{ar{x} - \mu_0}{\sigma / \sqrt{n}}$ | N/A |
| **1-Sample $t$-Test** | Continuous | $t = \frac{ar{x} - \mu_0}{s / \sqrt{n}}$ | $df = n - 1$ |
| **2-Sample Independent $t$-Test** | Continuous | $t = \frac{ar{x}_1 - ar{x}_2}{\sqrt{\frac{s_1^2}{n_1} + \frac{s_2^2}{n_2}}}$ | Welch $df$ |
| **Paired $t$-Test** | Continuous Paired | $t = \frac{ar{d} - 0}{s_d / \sqrt{n}}$ | $df = n - 1$ |
| **2-Sample Proportion $Z$-Test** | Binary | $Z = \frac{\hat{p}_1 - \hat{p}_2}{\sqrt{\hat{p}_{pool}(1-\hat{p}_{pool})(\frac{1}{n_1} + \frac{1}{n_2})}}$ | N/A |
| **Chi-Square Independence** | Categorical | $\chi^2 = \sum \frac{(O - E)^2}{E}$ | $df = (r-1)(c-1)$ |

## 3. Summary
Matching data types and study designs to the correct statistical test enables valid $p$-value computation and decision making.
