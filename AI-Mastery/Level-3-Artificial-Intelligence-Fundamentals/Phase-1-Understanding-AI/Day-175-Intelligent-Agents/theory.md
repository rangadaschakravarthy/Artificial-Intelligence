# Day 175 Theory: Intelligent Agents

### 1. What Is It?
An Intelligent Agent is anything that perceives its environment through sensors and acts upon that environment through actuators to achieve specified goals.

### 2. Why Does It Exist?
The agent abstraction provides a unified engineering framework for designing AI systems regardless of whether the system is a software web crawler, a game bot, or a physical warehouse robot.

### 3. Intuition
- **Sensors**: Cameras, microphones, infrared sensors, file readers (Inputs).
- **Actuators**: Wheels, robotic arms, screen displays, API call outputs (Outputs).
- **Agent Program**: The internal software algorithm mapping inputs to outputs.

### 4. PEAS Specification Framework
To design an intelligent agent, you must specify its **PEAS**:
- **P**: Performance Measure (How success is evaluated).
- **E**: Environment (The external domain in which the agent operates).
- **A**: Actuators (The mechanisms the agent uses to execute actions).
- **S**: Sensors (The devices used to perceive environmental state).

#### Example: Automated Taxi Driver PEAS
- **Performance**: Safe, fast, legal, comfortable trip, maximized profits.
- **Environment**: Roads, traffic, pedestrians, weather, customers.
- **Actuators**: Steering wheel, accelerator, brake, signal lights, horn.
- **Sensors**: Cameras, LiDAR, radar, GPS, speedometer, accelerometer.

### 5. Environment Properties Classification
1. **Observable**: Fully (complete state visible) vs Partially (noisy/incomplete sensors).
2. **Agents**: Single-agent (Crossword puzzle) vs Multi-agent (Chess, Driving).
3. **Determinism**: Deterministic (next state fixed by action) vs Stochastic (randomness involved).
4. **Episodic**: Episodic (current action doesn't affect future episodes) vs Sequential (actions impact future decisions).
5. **Change**: Static (environment doesn't change while agent thinks) vs Dynamic (changes continuously).
6. **Granularity**: Discrete (finite states/actions like Chess) vs Continuous (smooth values like steering angle).

### 6. The 5 Agent Architectures
1. **Simple Reflex Agent**: Acts strictly on current percept ($I \to A$).
2. **Model-Based Reflex Agent**: Maintains internal state tracking unobserved environment aspects.
3. **Goal-Based Agent**: Combines state tracking with explicit goal targets to plan action sequences.
4. **Utility-Based Agent**: Uses a continuous utility function $U(s)$ to trade off competing goals.
5. **Learning Agent**: Separates learning element from execution element to improve performance over time.

### 7. Summary
Intelligent agents interact with environments defined by PEAS specifications across 7 environmental dimensions.
