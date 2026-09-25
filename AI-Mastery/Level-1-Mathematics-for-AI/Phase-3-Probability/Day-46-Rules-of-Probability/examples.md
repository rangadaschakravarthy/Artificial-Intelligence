# Worked Examples — Rules of Probability

## Example 1: Complement Rule (At Least One)
**Problem**: A biased coin lands on Heads with $P(H) = 0.7$. If flipped 4 times, find the probability of getting at least one Tails.
**Solution**:
1. $P(	ext{No Tails}) = P(	ext{All Heads}) = (0.7)^4 = 0.2401$.
2. $P(	ext{At least 1 Tails}) = 1 - P(	ext{All Heads}) = 1 - 0.2401 = 0.7599$.

## Example 2: Addition Rule (Medical Diagnosis)
**Problem**: In a patient dataset, $20\%$ have condition A, $15\%$ have condition B, and $5\%$ have both. What percentage have condition A or B?
**Solution**:
1. $P(A) = 0.20$, $P(B) = 0.15$, $P(A \cap B) = 0.05$.
2. $P(A \cup B) = P(A) + P(B) - P(A \cap B) = 0.20 + 0.15 - 0.05 = 0.30$.
3. $30\%$ of patients have A or B.

## Example 3: Multiplication Rule (Dependent Events)
**Problem**: An urn contains 5 red balls and 5 black balls. Draw 2 balls without replacement. What is $P(	ext{Both Red})$?
**Solution**:
1. $P(R_1) = rac{5}{10} = 0.5$.
2. $P(R_2 | R_1) = rac{4}{9}$.
3. $P(R_1 \cap R_2) = P(R_1) \cdot P(R_2 | R_1) = rac{5}{10} 	imes rac{4}{9} = rac{20}{90} = rac{2}{9} pprox 0.2222$.

## Example 4: AI Example (Sensor Failure Risk)
**Problem**: An autonomous vehicle relies on LIDAR ($P(	ext{fail}) = 0.01$) and Radar ($P(	ext{fail}) = 0.02$). Failures are independent. Vehicle fails if BOTH fail. What is vehicle system failure probability?
**Solution**:
1. $P(	ext{System Fail}) = P(L_{	ext{fail}} \cap R_{	ext{fail}}) = 0.01 	imes 0.02 = 0.0002$.
2. System failure risk is $0.02\%$.

## Example 5: Ensemble Classification Voting
**Problem**: An ensemble uses 3 independent models with accuracy $0.80$ each. The ensemble predicts correctly if at least 2 models are correct. Find ensemble accuracy.
**Solution**:
1. Case 1: All 3 correct $\implies (0.8)^3 = 0.512$.
2. Case 2: Exactly 2 correct $\implies inom{3}{2} (0.8)^2 (0.2)^1 = 3 	imes 0.64 	imes 0.2 = 0.384$.
3. $P(	ext{Ensemble Correct}) = 0.512 + 0.384 = 0.896$. (Ensemble improves accuracy from $80\%$ to $89.6\%$).
