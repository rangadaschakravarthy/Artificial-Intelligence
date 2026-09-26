# Code — Day 210: AI Problem Solving Foundations

class AIProblem:
    def __init__(self, initial_state, goal_state):
        self.initial_state = initial_state
        self.goal_state = goal_state

    def actions(self, state):
        raise NotImplementedError

    def result(self, state, action):
        raise NotImplementedError

    def is_goal(self, state):
        return state == self.goal_state


class WaterJugProblem(AIProblem):
    def __init__(self):
        super().__init__(initial_state=(0, 0), goal_state=2)

    def actions(self, state):
        j1, j2 = state
        acts = []
        if j1 < 4: acts.append("FILL_1")
        if j2 < 3: acts.append("FILL_2")
        if j1 > 0: acts.append("EMPTY_1")
        if j2 > 0: acts.append("EMPTY_2")
        if j1 > 0 and j2 < 3: acts.append("POUR_1_TO_2")
        if j2 > 0 and j1 < 4: acts.append("POUR_2_TO_1")
        return acts

    def result(self, state, action):
        j1, j2 = state
        if action == "FILL_1": return (4, j2)
        if action == "FILL_2": return (j1, 3)
        if action == "EMPTY_1": return (0, j2)
        if action == "EMPTY_2": return (j1, 0)
        if action == "POUR_1_TO_2":
            transfer = min(j1, 3 - j2)
            return (j1 - transfer, j2 + transfer)
        if action == "POUR_2_TO_1":
            transfer = min(j2, 4 - j1)
            return (j1 + transfer, j2 - transfer)
        return state

    def is_goal(self, state):
        return state[0] == self.goal_state


if __name__ == "__main__":
    prob = WaterJugProblem()
    print("Initial State:", prob.initial_state)
    print("Actions from initial:", prob.actions(prob.initial_state))
    next_s = prob.result(prob.initial_state, "FILL_1")
    print("State after FILL_1:", next_s)
    print("Is Goal?", prob.is_goal(next_s))
