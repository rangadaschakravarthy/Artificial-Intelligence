# Code — Day 223: Utility & Decision Theory

class InferenceEngine:
    def __init__(self):
        self.facts = set()
        self.rules = []

    def add_fact(self, fact):
        self.facts.add(fact)

    def add_rule(self, antecedents, consequent):
        self.rules.append((set(antecedents), consequent))

    def run_forward_chaining(self):
        new_facts_derived = True
        while new_facts_derived:
            new_facts_derived = False
            for antecedents, consequent in self.rules:
                if consequent not in self.facts:
                    if antecedents.issubset(self.facts):
                        self.facts.add(consequent)
                        print("Derived new fact:", consequent, "from", antecedents)
                        new_facts_derived = True
        return self.facts


if __name__ == "__main__":
    engine = InferenceEngine()
    engine.add_fact("fever")
    engine.add_fact("cough")
    engine.add_rule(["fever", "cough"], "respiratory_infection")
    engine.add_rule(["respiratory_infection"], "prescribe_rest")

    print("Initial Facts:", engine.facts)
    final_facts = engine.run_forward_chaining()
    print("Final Derived Knowledge Base:", final_facts)
