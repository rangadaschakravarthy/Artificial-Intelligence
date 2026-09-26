import random

def main():
    print("=== Day 173: Introduction to AI Agent Simulation ===")
    
    class SimpleReflexAgent:
        def act(self, percept):
            location, status = percept
            if status == "Dirty":
                return "Suck"
            elif location == "A":
                return "Move Right"
            else:
                return "Move Left"

    agent = SimpleReflexAgent()
    percepts = [("A", "Dirty"), ("A", "Clean"), ("B", "Dirty"), ("B", "Clean")]
    
    for p in percepts:
        action = agent.act(p)
        print(f"Percept: {p} -> Selected Action: {action}")

if __name__ == "__main__":
    main()
