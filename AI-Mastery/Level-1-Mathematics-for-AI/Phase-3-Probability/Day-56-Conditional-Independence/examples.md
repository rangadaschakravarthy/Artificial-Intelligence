# Worked Examples — Conditional Independence

## Example 1: Common Cause (Reading Ability & Shoe Size given Age)
**Problem**: Let $X$ = Shoe size, $Y$ = Reading level, $Z$ = Age. Given $P(X=10, Y=5 | Z=10) = 0.20$, $P(X=10 | Z=10) = 0.40$, $P(Y=5 | Z=10) = 0.50$. Verify conditional independence.
**Solution**:
1. Check product: $P(X=10|Z=10) 	imes P(Y=5|Z=10) = 0.40 	imes 0.50 = 0.20$.
2. Matches joint conditional probability $0.20$.
3. $X$ and $Y$ are conditionally independent given $Z$.

## Example 2: Naive Bayes Feature Likelihood Calculation
**Problem**: Target $Y \in \{	ext{Spam}, 	ext{Ham}\}$. Features $X_1=	ext{"free"}, X_2=	ext{"money"}$.
Given $P(X_1=1|	ext{Spam})=0.8, P(X_2=1|	ext{Spam})=0.6$. Calculate $P(X_1=1, X_2=1 | 	ext{Spam})$ under Naive Bayes.
**Solution**:
1. By Naive Bayes assumption: $P(X_1=1, X_2=1 | 	ext{Spam}) = P(X_1=1 | 	ext{Spam}) 	imes P(X_2=1 | 	ext{Spam})$.
2. $= 0.8 	imes 0.6 = 0.48 = 48\%$.

## Example 3: Chain Structure (Markov Property)
**Problem**: In a sequence $X ightarrow Y ightarrow Z$, $X$ is weather today, $Y$ is weather tomorrow, $Z$ is weather day after tomorrow. Write $P(Z | Y, X)$ using conditional independence.
**Solution**:
1. Weather day after tomorrow ($Z$) depends only on tomorrow's weather ($Y$).
2. Given $Y$, $Z$ is conditionally independent of today's weather $X$.
3. $P(Z | Y, X) = P(Z | Y)$.

## Example 4: Collider / Explaining Away (Common Effect)
**Problem**: $X$ = Battery dead, $Y$ = Fuel empty, $Z$ = Car won't start. $X$ and $Y$ are marginally independent ($P(X, Y) = P(X)P(Y)$). If car won't start ($Z=1$) and you check battery and find it IS dead ($X=1$), what happens to $P(Y=1 | Z=1, X=1)$?
**Solution**:
1. Finding battery dead ($X=1$) "explains away" why car won't start ($Z=1$).
2. This reduces the probability that fuel is empty ($Y=1$).
3. $X$ and $Y$ become conditionally DEPENDENT given collider $Z$!

## Example 5: Parameter Reduction in Naive Bayes
**Problem**: A binary classification model has $d = 20$ binary features. Compare parameter count for full joint distribution vs Naive Bayes.
**Solution**:
1. Full joint distribution requires $2^{20} - 1 = 1,048,575$ parameters.
2. Naive Bayes requires $2 	imes d = 2 	imes 20 = 40$ conditional probabilities plus 1 prior $P(Y)$.
3. Parameters reduced from $> 1$ million down to 41!
