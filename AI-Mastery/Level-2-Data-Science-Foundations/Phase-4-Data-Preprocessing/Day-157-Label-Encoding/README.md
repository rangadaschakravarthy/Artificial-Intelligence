# Day 157 — Label Encoding

## Learning Objectives
- Map ordered categorical variables to sequential integers using Label / Ordinal Encoding.
- Use `sklearn.preprocessing.LabelEncoder` and `OrdinalEncoder`.
- Identify when Label Encoding is appropriate (Ordinal Data / Tree Models) and when it causes invalid magnitude bias (Linear Models).

## Prerequisites
- Day 156: Encoding

## Topics Covered
- Label Encoding vs Ordinal Encoding definition
- `LabelEncoder` for 1D target vectors vs `OrdinalEncoder` for 2D feature matrices
- Defining explicit category order maps (`{'Low': 0, 'Medium': 1, 'High': 2}`)
- The Magnitude Bias Pitfall: Why mapping `Red=0, Blue=1, Green=2` tricks linear models into assuming `Green > Red`
- Using Ordinal Encoding safely with Decision Trees and Random Forests

## Practical Work
- Perform explicit Ordinal Encoding on an education feature column using Pandas `.map()`.

## Difficulty
Intermediate
