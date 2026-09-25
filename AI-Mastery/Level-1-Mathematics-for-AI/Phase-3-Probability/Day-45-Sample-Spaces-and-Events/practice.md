# Practice Problems — Sample Spaces and Events

## Level 1: Basic Concept Checks
1. Define a sample space $\Omega$.
2. What set operation corresponds to "Event A AND Event B"?
3. What is the complement of event $A$ in sample space $\Omega$?
4. What does $A \cap B = \emptyset$ signify?
5. State whether $\Omega = \{x \in \mathbb{R} \mid x \ge 0\}$ is discrete or continuous.

## Level 2: Direct Calculations
6. Write the sample space for rolling a 4-sided die twice.
7. Given $\Omega = \{1, 2, 3, 4, 5, 6, 7, 8, 9, 10\}$, $A = \{2, 4, 6, 8, 10\}$, $B = \{6, 7, 8, 9, 10\}$. Find $A \cap B$.
8. For the sets in Q7, find $A \cup B$.
9. For the sets in Q7, find $A \setminus B$.
10. If $|A| = 15$, $|B| = 10$, and $|A \cap B| = 4$, find $|A \cup B|$.

## Level 3: Conceptual & Multi-Step Problems
11. Prove De Morgan's Law: $(A \cup B)^c = A^c \cap B^c$.
12. Three components $C_1, C_2, C_3$ can each pass (1) or fail (0). Write sample space $\Omega$.
13. Define event $E$: "At least 2 components pass" from Q12.
14. Show that $P(A \cup B) = P(A) + P(B) - P(A \cap B)$ using disjoint sets.
15. If $A_1, A_2, A_3$ form a partition of $\Omega$, what two conditions must they satisfy?

## Level 4: AI & ML Applications
16. Bounding box $A$ area = 50, $B$ area = 50, overlap area = 25. Calculate IoU score.
17. In object detection, if IoU threshold for True Positive is 0.50, does the prediction in Q16 pass?
18. In NLP sentiment classification with classes $\Omega = \{	ext{Pos}, 	ext{Neu}, 	ext{Neg}\}$, define event $E$: "Not negative".
19. Explain why multi-label classification requires independent sigmoid heads rather than a single Softmax over $\Omega$.
20. In an anomaly detection system, event $A$ is CPU usage $> 90\%$ and event $B$ is Memory usage $> 90\%$. Express event "System under stress (either high CPU or high Memory)" in set notation.

## Level 5: Interview Questions
21. Explain how IoU (Intersection over Union) serves as a Jaccard index in computer vision evaluation.
22. Define a $\sigma$-algebra $\mathcal{F}$ over sample space $\Omega$.
23. Why can continuous sample spaces have single outcomes with $P(\{x\}) = 0$ while the overall event interval has $P([a, b]) > 0$?
