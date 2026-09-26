def main():
    print("=== Day 176: Rational Agent Expected Utility Demonstration ===")
    eu_option_a = 0.9 * 100 + 0.1 * (-500) # 90 - 50 = 40
    eu_option_b = 0.5 * 50 + 0.5 * 0       # 25
    print(f"Expected Utility Option A: {eu_option_a}")
    print(f"Expected Utility Option B: {eu_option_b}")
    print("Rational Agent chooses Option A.")

if __name__ == "__main__":
    main()
