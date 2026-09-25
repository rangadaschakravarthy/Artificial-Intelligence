# Worked Examples — Probability AI Mini-Project

## Example 1: Tokenization and Vocabulary Building
**Input Emails**:
1. "Free lottery winner"
2. "Meeting project report"
**Vocabulary $D$**: `['free', 'lottery', 'winner', 'meeting', 'project', 'report']` ($D = 6$).

## Example 2: Naive Bayes Log-Score Calculation
For document "free winner":
- $	ext{Score}(	ext{Spam}) = \ln(0.5) + \ln P(	ext{"free"}|S) + \ln P(	ext{"winner"}|S)$.
- $	ext{Score}(	ext{Ham}) = \ln(0.5) + \ln P(	ext{"free"}|H) + \ln P(	ext{"winner"}|H)$.
- Higher log-score determines predicted class.

## Example 3: Sequential Risk Updating
- Base Prior: $P(D) = 0.03 \implies 	ext{Odds} = rac{0.03}{0.97} pprox 0.0309$.
- After Evidence 1 (LR = 8): $	ext{Odds}_1 = 0.0309 	imes 8 = 0.2472 \implies P(D|E_1) = rac{0.2472}{1.2472} pprox 0.1982 = 19.82\%$.
- After Evidence 2 (LR = 5): $	ext{Odds}_2 = 0.2472 	imes 5 = 1.236 \implies P(D|E_1,E_2) = rac{1.236}{2.236} pprox 0.5528 = 55.28\%$.
