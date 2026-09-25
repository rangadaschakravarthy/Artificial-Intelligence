# Theory — Sample Spaces and Events

## 1. Simple Definition
A **sample space** is the set of all possible outcomes of a random experiment. An **event** is any specific outcome or group of outcomes you are interested in measuring.

## 2. Intuition
If an AI system analyzes a customer review, the sample space of sentiment predictions might be $\Omega = \{	ext{Positive}, 	ext{Neutral}, 	ext{Negative}\}$. An event could be "The review is not negative," which corresponds to the subset $\{	ext{Positive}, 	ext{Neutral}\}$.

## 3. Mathematical Definition
Let $\Omega$ be the universal set of outcomes.
- An event $A$ is a subset of $\Omega$ ($A \subseteq \Omega$).
- The event space $\mathcal{F}$ is a $\sigma$-algebra of subsets of $\Omega$.

## 4. Notation
- $\Omega$: Sample space.
- $A, B$: Events.
- $A \cup B$: Union ($A$ or $B$ or both).
- $A \cap B$: Intersection (both $A$ and $B$).
- $A^c$ or $\overline{A}$: Complement (not $A$).
- $\emptyset$: Empty set / Impossible event.

## 5. Formula
- **Union**: $A \cup B = \{x \in \Omega \mid x \in A 	ext{ or } x \in B\}$
- **Intersection**: $A \cap B = \{x \in \Omega \mid x \in A 	ext{ and } x \in B\}$
- **Complement**: $A^c = \Omega \setminus A = \{x \in \Omega \mid x 
otin A\}$
- **Mutually Exclusive**: $A \cap B = \emptyset$
- **Exhaustive**: $A_1 \cup A_2 \cup \dots \cup A_k = \Omega$

## 6. Symbol Explanation
- $\in$: Element of.
- $\setminus$: Set difference.
- $\emptyset$: Null/Empty set.

## 7. Step-by-Step Calculation
Experiment: Rolling a 6-sided die. $\Omega = \{1, 2, 3, 4, 5, 6\}$.
- Event $A$ (Even): $\{2, 4, 6\}$.
- Event $B$ (Greater than 3): $\{4, 5, 6\}$.
- $A \cap B = \{4, 6\}$.
- $A \cup B = \{2, 4, 5, 6\}$.
- $A^c = \{1, 3, 5\}$.

## 8. Second Example (Computer Vision Detection)
Bounding box prediction for object detection:
- $\Omega$: Continuous 2D image coordinate region.
- Event $A$: True Object Box. Event $B$: Predicted Box.
- Intersection over Union (IoU) metric: $	ext{IoU} = rac{|A \cap B|}{|A \cup B|}$.

## 9. Common Mistakes
- Confusing mutually exclusive ($A \cap B = \emptyset$) with independent events.
- Omitting outcomes from the sample space.

## 10. AI Connection
In multi-class classification, class predictions are defined as mutually exclusive and collectively exhaustive events over the label space.

## 11. Algorithm Connection
IoU in Object Detection (YOLO, Faster R-CNN) measures overlapping area of event sets $A$ and $B$.

## 12. Practical Interpretation
A classification head using Softmax assumes classes are mutually exclusive (each image belongs to exactly one class). Multi-label classification relaxes this assumption.

## 13. Interview Insight
**Q**: What is the difference between mutually exclusive and independent events?
**A**: Mutually exclusive means events cannot happen together ($A \cap B = \emptyset$). Independent means occurrence of one does not affect probability of the other ($P(A \cap B) = P(A)P(B)$).

## 14. Summary
Sample spaces frame all possibilities; events group outcomes. Set operations (union, intersection, IoU) form the backbone of probabilistic AI metrics.
