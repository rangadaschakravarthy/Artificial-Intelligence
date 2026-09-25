# Worked Examples — Bayes' Theorem

## Example 1: Classic Medical Diagnostic Test
**Problem**: Disease prevalence $P(D) = 0.005$. Test sensitivity $P(+|D) = 0.99$. False positive rate $P(+|D^c) = 0.02$. Calculate $P(D|+)$.
**Solution**:
1. Prior: $P(D) = 0.005, P(D^c) = 0.995$.
2. Likelihoods: $P(+|D) = 0.99, P(+|D^c) = 0.02$.
3. Evidence $P(+) = (0.99)(0.005) + (0.02)(0.995) = 0.00495 + 0.01990 = 0.02485$.
4. Posterior $P(D|+) = rac{0.00495}{0.02485} pprox 0.1992 = 19.92\%$.

## Example 2: Spam Filter Single Word
**Problem**: $P(	ext{Spam}) = 0.40$. Word "Free" appears: $P(	ext{"Free"}|	ext{Spam}) = 0.60$, $P(	ext{"Free"}|	ext{Ham}) = 0.10$. Find $P(	ext{Spam}|	ext{"Free"})$.
**Solution**:
1. $P(	ext{Spam}) = 0.40, P(	ext{Ham}) = 0.60$.
2. Numerator: $(0.60)(0.40) = 0.24$.
3. Denominator: $(0.60)(0.40) + (0.10)(0.60) = 0.24 + 0.06 = 0.30$.
4. $P(	ext{Spam}|	ext{"Free"}) = rac{0.24}{0.30} = 0.80 = 80\%$.

## Example 3: Manufacturing Defect Tracking
**Problem**: Machine A produces $60\%$ of parts (defect rate $1\%$). Machine B produces $40\%$ (defect rate $3\%$). A part is defective ($E$). Find probability it came from Machine B.
**Solution**:
1. $P(M_A) = 0.60, P(M_B) = 0.40$.
2. $P(E|M_A) = 0.01, P(E|M_B) = 0.03$.
3. $P(E) = (0.01)(0.60) + (0.03)(0.40) = 0.006 + 0.012 = 0.018$.
4. $P(M_B|E) = rac{P(E|M_B)P(M_B)}{P(E)} = rac{0.012}{0.018} = rac{2}{3} pprox 0.6667$.

## Example 4: Sequential Bayesian Update
**Problem**: Start with prior $P(A) = 0.50$. Observe evidence $E_1$ with likelihood ratio $rac{P(E_1|A)}{P(E_1|A^c)} = 3$. Update posterior, then use it as new prior for $E_2$ with likelihood ratio 2. Find final posterior.
**Solution**:
1. Odds formulation: $	ext{Prior Odds} = rac{0.5}{0.5} = 1$.
2. After $E_1$: $	ext{Posterior Odds}_1 = 1 	imes 3 = 3 \implies P(A|E_1) = rac{3}{1+3} = 0.75$.
3. After $E_2$: $	ext{Posterior Odds}_2 = 3 	imes 2 = 6 \implies P(A|E_1, E_2) = rac{6}{1+6} = rac{6}{7} pprox 0.8571$.

## Example 5: AI Security Anomaly Detection
**Problem**: $P(	ext{Intrusion}) = 0.001$. Sensor flags alert: $P(	ext{Alert}|	ext{Intrusion}) = 0.95$, $P(	ext{Alert}|	ext{Normal}) = 0.01$. Find probability alert indicates actual intrusion.
**Solution**:
1. $P(	ext{Alert}) = (0.95)(0.001) + (0.01)(0.999) = 0.00095 + 0.00999 = 0.01094$.
2. $P(	ext{Intrusion}|	ext{Alert}) = rac{0.00095}{0.01094} pprox 0.0868 = 8.68\%$.
