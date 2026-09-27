# Code — Day 294: Semi-Supervised Learning Methods
import numpy as np

class SimpleQTableAgent:
    """Tabular Q-Learning Agent Demonstration."""
    def __init__(self, n_states=6, n_actions=2, alpha=0.1, gamma=0.9, epsilon=0.1):
        self.n_states = n_states
        self.n_actions = n_actions
        self.alpha = alpha
        self.gamma = gamma
        self.epsilon = epsilon
        self.q_table = np.zeros((n_states, n_actions))

    def choose_action(self, state):
        if np.random.rand() < self.epsilon:
            return np.random.randint(self.n_actions)
        return np.argmax(self.q_table[state])

    def update(self, state, action, reward, next_state):
        best_next_q = np.max(self.q_table[next_state])
        td_target = reward + self.gamma * best_next_q
        td_error = td_target - self.q_table[state, action]
        self.q_table[state, action] += self.alpha * td_error

def demonstrate_rl():
    print("--- Day 294: Semi-Supervised Learning Methods Demo ---")
    agent = SimpleQTableAgent()
    
    # Simulate 5 steps of environment interaction
    state = 0
    for step in range(5):
        action = agent.choose_action(state)
        next_state = (state + 1) % 6
        reward = 10.0 if next_state == 5 else 0.0
        
        agent.update(state, action, reward, next_state)
        print(f"Step {step+1}: State {state} -> Action {action} -> Reward {reward} -> Next State {next_state}")
        state = next_state
        
    print("\nUpdated Q-Table Matrix:\n", np.round(agent.q_table, 2))

if __name__ == "__main__":
    demonstrate_rl()
