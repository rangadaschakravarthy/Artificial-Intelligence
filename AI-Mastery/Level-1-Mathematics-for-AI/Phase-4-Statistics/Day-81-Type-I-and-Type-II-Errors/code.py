import numpy as np
from statsmodels.stats.power import TTestIndPower

def main():
    print("--- Day 81: Type I and Type II Errors & Power Analysis ---")
    
    # Setup Power Analysis Engine
    power_analysis = TTestIndPower()
    
    # 1. Calculate Required Sample Size per Group for A/B Test
    target_effect_size = 0.20 # Small effect size (Cohen's d)
    alpha = 0.05
    target_power = 0.80
    
    required_n = power_analysis.solve_power(
        effect_size=target_effect_size,
        alpha=alpha,
        power=target_power,
        ratio=1.0
    )
    
    print("1. A/B Test Sample Size Determination:")
    print(f"  Target Effect Size d:  {target_effect_size:.2f}")
    print(f"  Significance Level a:  {alpha:.2f}")
    print(f"  Target Power (1-beta): {target_power*100:.1f}%")
    print(f"  Required Sample Size:  {np.ceil(required_n):.0f} users per group (Total: {2*np.ceil(required_n):.0f})")
    
    # 2. Calculate Achieved Power for Fixed Sample Size n = 100
    fixed_n = 100
    achieved_power = power_analysis.solve_power(
        effect_size=target_effect_size,
        nobs1=fixed_n,
        alpha=alpha,
        ratio=1.0
    )
    
    print(f"
2. Fixed Sample Size Power Check (n = {fixed_n}):")
    print(f"  Achieved Power:        {achieved_power*100:.2f}% ({'UNDERPOWERED (< 80%)' if achieved_power < 0.8 else 'SUFFICIENT POWER'})")
    print(f"  Type II Error Rate b:  {(1 - achieved_power)*100:.2f}%")

if __name__ == "__main__":
    main()
