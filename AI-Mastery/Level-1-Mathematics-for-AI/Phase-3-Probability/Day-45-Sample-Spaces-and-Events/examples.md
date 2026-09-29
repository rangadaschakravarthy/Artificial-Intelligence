# Worked Examples — Sample Spaces and Events

## Example 1: Discrete Sample Space (Coin Tossing)
**Problem**: Write the sample space $\Omega$ for tossing 3 coins. List event $A$: "At least 2 Heads".
**Solution**:
1. $\Omega = \{HHH, HHT, HTH, HTT, THH, THT, TTH, TTT\} \implies |\Omega| = 8$.
2. Event $A = \{HHH, HHT, HTH, THH\}$.
3. $|A| = 4$. $P(A) = \frac{4}{8} = 0.5$.

## Example 2: Set Operations (Card Drawing)
**Problem**: Let $A$ be drawing a Red card, $B$ be drawing a Face card (J, Q, K). Find $|A \cap B|$ and $|A \cup B|$.
**Solution**:
1. Standard deck: 52 cards ($26$ Red, $26$ Black).
2. Face cards per suit: 3. Total face cards $= 3 	imes 4 = 12$.
3. $A \cap B$: Red Face cards $= 3 	ext{ Hearts} + 3 	ext{ Diamonds} = 6$.
4. $|A \cup B| = |A| + |B| - |A \cap B| = 26 + 12 - 6 = 32$.

## Example 3: Mutually Exclusive Verification
**Problem**: Are $E = 	ext{Rolling an odd number}$ and $F = 	ext{Rolling an even number}$ mutually exclusive and exhaustive on a 6-sided die?
**Solution**:
1. $E = \{1, 3, 5\}$, $F = \{2, 4, 6\}$.
2. $E \cap F = \emptyset \implies$ Mutually Exclusive.
3. $E \cup F = \{1, 2, 3, 4, 5, 6\} = \Omega \implies$ Exhaustive.

## Example 4: AI Example (Intersection over Union - IoU)
**Problem**: A bounding box $A$ has area 100 pixels. Predicted box $B$ has area 120 pixels. Overlap area $|A \cap B| = 80$ pixels. Calculate IoU.
**Solution**:
1. $|A \cup B| = |A| + |B| - |A \cap B| = 100 + 120 - 80 = 140$.
2. $	ext{IoU} = \frac{|A \cap B|}{|A \cup B|} = \frac{80}{140} = \frac{4}{7} pprox 0.5714$.

## Example 5: Continuous Sample Space
**Problem**: An AI response latency $T$ is measured in seconds between 0 and 5. Define $\Omega$ and event $E$: "Response time under 2 seconds".
**Solution**:
1. Continuous sample space: $\Omega = [0, 5] \subset \mathbb{R}$.
2. Event $E = [0, 2) = \{t \in \mathbb{R} \mid 0 \le t < 2\}$.
