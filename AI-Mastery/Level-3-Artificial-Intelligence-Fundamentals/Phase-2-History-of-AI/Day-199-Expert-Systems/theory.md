# Day 199 Theory: Expert Systems

### 1. What Is It?
An Expert System is a computer program that uses knowledge-engineering techniques to solve problems within a specialized domain that would otherwise require human expert expertise.

### 2. Certainty Factors (MYCIN Approach)
To handle partial uncertainty, rules attach Certainty Factors $CF \in [-1.0, +1.0]$:

$$
\text{IF } A \text{ AND } B \text{ THEN } C \text{ WITH } CF = 0.8
$$

Combining evidence for hypothesis $H$ from two rules with certainty $CF_1$ and $CF_2$:

$$
CF_{\text{combine}} = CF_1 + CF_2 \cdot (1 - CF_1) \quad (\text{for } CF_1, CF_2 > 0)
$$

### 3. Summary
Expert Systems encapsulated human expert rule bases, introducing certainty factors for handling domain uncertainty.
