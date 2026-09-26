# Day 173 Theory: Introduction to Artificial Intelligence

### 1. What Is It?
Artificial Intelligence (AI) is the subfield of computer science dedicated to building hardware and software systems capable of performing tasks that typically require human intelligence, such as visual perception, speech recognition, decision-making, and language translation.

### 2. Why Does It Exist?
Human cognitive bandwidth, memory retention, and mathematical processing speeds are constrained by biological limits. AI systems exist to automate complex decision-making, operate at scale, process vast non-linear data spaces, and solve NP-hard search problems.

### 3. Intuition
Imagine a chess player: a human uses intuition, visual pattern memory, and tactical evaluation. An AI system represents the board as a mathematical state space, evaluates millions of future move trees, computes utility values, and selects the optimal path.

### 4. Syntax (Conceptual Agent Framework)
```python
class SimpleAIAgent:
    def __init__(self, environment):
        self.environment = environment
    def perceive(self):
        return self.environment.get_state()
    def decide(self, percept):
        return self.select_optimal_action(percept)
    def act((self, action):
        self.environment.apply(action)
```

### 5. Parameters / Operational Environment
- **Percept Sequence**: The complete history of sensory inputs received by the agent.
- **Agent Function**: Mathematical mapping from percept history to selected action ($f: \mathcal{P}^* 	o \mathcal{A}$).
- **Performance Measure**: Objective criterion evaluating environmental outcome quality.

### 6. How It Works: The 4 Quadrants of AI
Russell & Norvig categorize AI definitions across two dimensions: **Thought vs Action** and **Human-like vs Rationality**:

| Dimension | Thinking | Acting |
|---|---|---|
| **Human-like** | **Thinking Humanly**: Cognitive modeling, neural simulation | **Acting Humanly**: Turing Test, natural language, robotics |
| **Rationality** | **Thinking Rationally**: Laws of thought, formal logic, inference | **Acting Rationally**: Rational Agents, expected utility maximization |

### 7. Simple Example
A thermostat measures temperature ($75^\circ	ext{F}$). If temperature $> 72^\circ	ext{F}$, it triggers cooling. This is basic reactive rule-based control.

### 8. Intermediate Example
An autonomous vehicle perceives camera pixels, radar ranges, and GPS coordinates; predicts pedestrian trajectories using probabilistic models; plans a smooth collision-free path using A* search; and actuates steering/braking controls.

### 9. Output Interpretation
AI system output is an action, prediction, or decision that maximizes the expected value of its target utility function given current percepts.

### 10. Common Mistakes
- Believing AI requires consciousness or biological feeling.
- Assuming any software script containing an `if/else` block is "Artificial Intelligence".

### 11. Data Science Connection
Data Science provides the structured datasets, feature distributions, and cleaning pipelines that feed AI decision engines.

### 12. AI/ML Connection
Machine Learning is the subset of AI where agent functions $f: \mathcal{P}^* 	o \mathcal{A}$ are learned automatically from data rather than hand-coded by human engineers.

### 13. Interview Insight
Question: "How do you define Artificial Intelligence in a technical interview?"
Answer: Define AI through the **Rational Agent paradigm**: An AI system is an agent that perceives its environment through sensors, processes percepts to compute utility-maximizing decisions, and executes actions through actuators to achieve goals.

### 14. Summary
Artificial Intelligence encompasses systems designed to think or act humanly or rationally, centered modernly on rational agents maximizing utility.
