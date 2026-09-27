# Day 298 — Rewards, Returns & Discounting

## Learning Objectives
- Master the concepts, mathematical formulations, and Python implementations of rewards, returns & discounting.
- Understand training signals, state-action interactions, and Bellman update equations.
- Build scratch Python implementations and interactive environment simulations.

## Prerequisites
- Days 255-293: ML Foundations, Supervised & Unsupervised Learning.
- Level 3 AI: Intelligent Agents, Problem Spaces, State Graphs.

## Topics Covered
1. Paradigm Intuition & Structural Framework
2. Mathematical Formulations & Objective Derivations
3. Step-by-Step Calculation Examples
4. Python Implementation from Scratch

## Why This Matters
Immediate rewards $r_t$, cumulative return $G_t = \sum_{k=0}^{\infty} \gamma^k r_{t+k+1}$, discount factor $\gamma \in [0, 1)$, and horizon modeling.

## Connection to Previous Levels
- **Level 1 Math**: Expected value $\mathbb{E}[R]$, geometric series sum $\sum \gamma^k$, Markov transition probability matrices.
- **Level 3 AI**: Agent-environment perception-action loops and state search trees.

## Completion Checklist
- [ ] I can explain rewards, returns & discounting without memorizing definitions.
- [ ] I can trace update equations step-by-step.
- [ ] I can implement the algorithm in Python.
- [ ] I can solve 15+ practice questions.
