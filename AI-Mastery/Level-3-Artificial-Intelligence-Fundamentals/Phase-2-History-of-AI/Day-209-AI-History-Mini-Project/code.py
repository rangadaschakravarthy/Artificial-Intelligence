def main():
    print("=== Day 209: Rule-Based Expert System Mini Project ===")
    
    class ExpertSystem:
        def __init__(self):
            self.facts = set()
            self.rules = []
            self.trace = []
            
        def add_fact(self, fact):
            self.facts.add(fact)
            
        def add_rule(self, rule_id, if_set, then_fact):
            self.rules.append({"id": rule_id, "if": if_set, "then": then_fact})
            
        def run_forward_chaining(self):
            changed = True
            while changed:
                changed = False
                for r in self.rules:
                    if r["if"].issubset(self.facts) and r["then"] not in self.facts:
                        self.facts.add(r["then"])
                        self.trace.append(f"Fired {r['id']}: Matched {r['if']} -> Added {r['then']}")
                        changed = True

    es = ExpertSystem()
    es.add_fact("symptom_fever")
    es.add_fact("symptom_cough")
    es.add_rule("R1", {"symptom_fever", "symptom_cough"}, "flu_suspected")
    es.add_rule("R2", {"flu_suspected"}, "action_isolate_and_rest")
    
    es.run_forward_chaining()
    
    print("Final Fact Base:", es.facts)
    print("
Explanation Trace:")
    for t in es.trace:
        print("  -", t)

if __name__ == "__main__":
    main()
