# Examples — Day 210: AI Problem Solving Foundations

## Example 1: Route Finding Formulations
Problem: Find optimal driving path from City A to City B.
- $S$: Set of all cities/intersections on the map.
- $s_0$: City A.
- $A(s)$: Roads connected to city $s$.
- $T(s, a)$: The neighboring city reached by road $a$.
- $G(s)$: $s == \text{City B}$.
- $c(s, a, s')$: Distance or driving time between city $s$ and city $s'$.

## Example 2: Cleaning Robot Problem Formulation
Problem: Autonomous floor cleaner.
- $S$: $\{(x, y, \text{battery\_level}, \text{dirt\_map})\}$.
- $s_0$: $(0, 0, 100\%, \text{initial\_dirt\_matrix})$.
- $A(s)$: $\{\text{North}, \text{South}, \text{East}, \text{West}, \text{Clean}, \text{Recharge}\}$.
- $T(s, a)$: Updates robot coordinates and dirt matrix.
- $G(s)$: $\text{dirt\_map} == 0$.

## Example 3: Water Jug Problem (4-liter & 3-liter jugs)
Problem: Measure exactly 2 liters using a 4L jug and a 3L jug.
- $S$: $(x, y)$ where $0 \le x \le 4$, $0 \le y \le 3$.
- $s_0$: $(0, 0)$.
- $A(s)$: Fill jug 1, Fill jug 2, Empty jug 1, Empty jug 2, Pour jug 1 into 2, Pour jug 2 into 1.
- $G(s)$: $x == 2$.

## Example 4: Missionaries and Cannibals
3 Missionaries and 3 Cannibals must cross a river using a boat holding at most 2 people.
- $S$: $(M_L, C_L, B)$ where $M_L, C_L \in [0..3]$, $B \in \{0, 1\}$.
- Validity Constraint: In any bank, $M=0$ or $M \ge C$.
- Goal: $(0, 0, 0)$.

## Example 5: Sudoku Solver Problem Formulation
- $S$: 9x9 grid partially or fully filled.
- $s_0$: Given puzzle grid.
- $A(s)$: Place digit 1..9 in first empty cell satisfying row/col/box constraints.
- $G(s)$: Grid completely filled without constraint violations.
