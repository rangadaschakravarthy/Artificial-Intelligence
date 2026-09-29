# Theory — Probability AI Mini-Project Architecture

## 1. Project Overview
This mini-project implements two real-world probabilistic AI systems:
1. **Multinomial Naive Bayes Spam Classification System**: Takes raw text emails, converts them into Bag-of-Words count vectors, trains a Multinomial Naive Bayes model with Laplace smoothing ($lpha=1$), and computes class probabilities in log-space.
2. **Bayesian Credit Risk Inference Engine**: Dynamically updates customer default probability $P(	ext{Default} | 	ext{Evidence})$ as financial risk indicators (missed payments, high credit utilization) are observed sequentially.

## 2. Naive Bayes Spam Architecture
- **Preprocessing**: Tokenize lowercase text, build Vocabulary $D$.
- **Prior Calculation**:
  

$$
P(	ext{Spam}) = \frac{N_{	ext{Spam}}}{N_{	ext{total}}}, \quad P(	ext{Ham}) = \frac{N_{	ext{Ham}}}{N_{	ext{total}}}
$$

- **Likelihood Fitting with Laplace Smoothing**:
  

$$
P(W_i \mid c) = \frac{	ext{Count}(W_i, c) + 1}{\sum_j 	ext{Count}(W_j, c) + D}
$$

- **Log-Space Prediction**:
  

$$
ext{Score}(c) = \ln P(c) + \sum_{w \in 	ext{doc}} \ln P(w \mid c)
$$

## 3. Bayesian Credit Risk Architecture
- **Prior**: Base default rate $P(D) = 0.03$.
- **Evidence 1 (Missed Payment)**: Likelihood ratio $\frac{P(E_1|D)}{P(E_1|D^c)} = 8.0$.
- **Evidence 2 (Credit Utilization > 90%)**: Likelihood ratio $\frac{P(E_2|D)}{P(E_2|D^c)} = 5.0$.
- Dynamic posterior update using Bayes' Theorem Odds Formulation.

## 4. Summary
This mini-project demonstrates how probability theory powers real-world classification, risk engine evaluation, and log-domain inference.
