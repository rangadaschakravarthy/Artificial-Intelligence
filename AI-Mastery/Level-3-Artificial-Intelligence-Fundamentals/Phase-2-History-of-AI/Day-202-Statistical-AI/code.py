def main():
    print("=== Day 202: Statistical AI & Bayes Rule Demonstration ===")
    prior = 0.05
    likelihood = 0.90
    evidence = 0.10
    posterior = (likelihood * prior) / evidence
    print(f"Prior: {prior} | Posterior: {posterior}")

if __name__ == "__main__":
    main()
