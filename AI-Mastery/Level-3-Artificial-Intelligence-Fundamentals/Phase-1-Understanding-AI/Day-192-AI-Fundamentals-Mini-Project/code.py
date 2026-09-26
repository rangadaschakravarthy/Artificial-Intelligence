import random

def main():
    print("=== Day 192: Smart Task Router Mini Project ===")
    
    def route_request(req):
        if req.startswith("COMMAND_"):
            return "Automation Pipeline", "Executed deterministic script"
        elif "refund" in req.lower() and "policy" in req.lower():
            return "Symbolic Logic Engine", "Applied formal refund rules"
        else:
            return "ML Intent Model", f"Predicted intent for: '{req}'"
            
    requests = [
        "COMMAND_BACKUP_DB",
        "Requesting refund per company policy terms",
        "Can you recommend a good laptop under $1000?"
    ]
    
    for r in requests:
        engine, status = route_request(r)
        print(f"Request: '{r}'
  -> Assigned Engine: [{engine}]
  -> Status: {status}
")

if __name__ == "__main__":
    main()
