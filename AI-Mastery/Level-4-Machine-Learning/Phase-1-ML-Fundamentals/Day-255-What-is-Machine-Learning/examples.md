# Examples — Day 255: What Is Machine Learning?

## Example 1 — Extremely Simple (Rule vs ML)
- Task: Classify positive vs negative temperature.
- Rule Approach: `if temp > 0: return 'Warm' else: return 'Cold'`
- ML Approach: Train model on $(temp, label)$ pairs.

## Example 2 — Basic Numerical Example (Learning Slope)
- Given points $(1, 3), (2, 5), (3, 7)$.
- Model hypothesis: $\hat{y} = w \cdot x + b$.
- Learning extracts parameters: $w = 2, b = 1 \implies y = 2x + 1$.

## Example 3 — Real Dataset Example (Housing Prices)
- Features: Square footage, bedrooms, age.
- Target: Price in USD.
- Learned Model: $\text{Price} = 150(\text{sqft}) + 10000(\text{beds}) - 500(\text{age}) + 20000$.

## Example 4 — Machine Learning Example (Email Classification)
- Input: Email containing "Claim your 1000 free bonus cash".
- Feature Extraction: `{'free': 1, 'bonus': 1, 'cash': 1}`.
- Predicted Probability of Spam: $0.98 \implies \text{Spam}$.

## Example 5 — Real-World Scenario (Credit Card Fraud Detection)
- Traditional: Rule `transaction > $10,000` catches large fraud but misses small stealth fraud.
- ML: Analyzes location, device ID, spending velocity, time of day to catch fraud patterns automatically.

## Example 6 — Interview-Style Example (Tom Mitchell Framework for Autonomous Driving)
- **Task ($T$)**: Driving autonomously on a highway.
- **Experience ($E$)**: Video streams and sensor data from human driving recordings.
- **Performance ($P$)**: Average distance traveled without human safety intervention.
