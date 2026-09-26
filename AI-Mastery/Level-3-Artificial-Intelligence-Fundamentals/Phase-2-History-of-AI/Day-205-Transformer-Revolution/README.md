# Day 205 — Transformer Revolution

## Learning Objectives
- Examine the 2017 Transformer architecture breakthrough ("Attention Is All You Need").
- Understand how Self-Attention and parallelization replaced sequential Recurrent Neural Networks (RNNs).
- Trace the evolution from BERT and GPT to modern Large Language Models (LLMs).

## Prerequisites
- Day 204: Deep Learning Revolution

## Topics Covered
- Limitations of Sequential RNNs/LSTMs: Sequential $O(N)$ execution bottleneck preventing GPU parallel scaling over long context windows
- The 2017 Landmark Paper: Vaswani et al. (*Attention Is All You Need*)
- Self-Attention Mechanism concept: Computing pairwise token relevance matrices $Q, K, V$ in parallel
- Emergence of Foundation Models: BERT (Bi-directional encoder), GPT (Autoregressive decoder)
- Scaling Laws: Performance scaling predictably with parameters, dataset size, and compute

## Difficulty
Intermediate
