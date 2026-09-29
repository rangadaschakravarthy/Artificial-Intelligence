# Worked Examples — Introduction to Probability

## Example 1: Very Easy (Coin Flip)
**Problem**: Calculate the probability of getting Heads on a single flip of a fair coin.
**Solution**:
1. $\Omega = \{	ext{Heads}, 	ext{Tails}\} \implies |\Omega| = 2$.
2. $A = \{	ext{Heads}\} \implies |A| = 1$.
3. $P(	ext{Heads}) = \frac{1}{2} = 0.5$.

## Example 2: Beginner (Card Draw)
**Problem**: What is the probability of drawing an Ace from a standard deck of 52 cards?
**Solution**:
1. $|\Omega| = 52$.
2. $|A| = 4$ (4 Aces in deck).
3. $P(	ext{Ace}) = \frac{4}{52} = \frac{1}{13} pprox 0.0769$.

## Example 3: Intermediate (Rolling Two Dice)
**Problem**: Find the probability that the sum of two fair 6-sided dice is 7.
**Solution**:
1. Sample space size $|\Omega| = 6 	imes 6 = 36$.
2. Favorable outcomes for sum = 7: $(1,6), (2,5), (3,4), (4,3), (5,2), (6,1)$.
3. $|A| = 6$.
4. $P(	ext{Sum}=7) = \frac{6}{36} = \frac{1}{6} pprox 0.1667$.

## Example 4: AI/ML Example (Spam Classifier Logits)
**Problem**: A binary classifier outputs logit $z = 1.3863$. Calculate the predicted probability of Spam using the Sigmoid function $\sigma(z) = \frac{1}{1 + e^{-z}}$.
**Solution**:
1. $e^{-1.3863} = 0.25$.
2. $P(	ext{Spam}) = \frac{1}{1 + 0.25} = \frac{1}{1.25} = 0.80$.
3. Probability of Spam is $80\%$.

## Example 5: Real-World System Reliability
**Problem**: A server cluster has 3 independent servers. Each has a probability of failure of $0.05$. What is the probability that all 3 operate successfully?
**Solution**:
1. Probability server 1 operates = $1 - 0.05 = 0.95$.
2. Since servers are independent, $P(	ext{All 3 operational}) = 0.95 	imes 0.95 	imes 0.95 = 0.95^3 = 0.857375$.
3. Cluster reliability is $85.74\%$.
