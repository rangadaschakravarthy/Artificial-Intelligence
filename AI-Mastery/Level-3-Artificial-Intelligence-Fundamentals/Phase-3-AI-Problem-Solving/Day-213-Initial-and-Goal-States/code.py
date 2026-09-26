# Code — Day 213: Initial & Goal States

class DomainState:
    def __init__(self, name, data):
        self.name = name
        self.data = tuple(data)

    def __hash__(self):
        return hash((self.name, self.data))

    def __eq__(self, other):
        return isinstance(other, DomainState) and self.name == other.name and self.data == other.data

    def __repr__(self):
        return f"State({self.name}, {self.data})"


def get_successors(state):
    name, data = state.name, state.data
    val = data[0]
    return [
        DomainState(name, (val + 1,)),
        DomainState(name, (val - 1,))
    ]


if __name__ == "__main__":
    s0 = DomainState("Counter", (0,))
    print("Initial State:", s0)
    print("Successors:", get_successors(s0))
