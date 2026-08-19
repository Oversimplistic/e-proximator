# e-proximator - Numerical Approximation Using Only e

A CLI tool that approximates any target value using a sequence of operations built exclusively from Euler's number (e), via a range of algorithms acting with a defined operator set.

## Overview
The e-proximator currently uses a Greedy Hill Climbing Algorithm, a Beam Search Algorithm, and Simulated Annealing. Together these algorithms produce their own approximations of the desired number, with the most precise being put forward to the user.

The e-proximator stemmed mainly from boredom, and was a project first built months before it's first commit. I have now revived the project to refine it, and explore more options in combinatorial approximation.

## Sample Output

```
You were aiming for: 335637131
Best Approximation: 335637130.48715204
Best Path -> ['+100000000', '2x +10000000', '3x +1000000', '5x +100000', '3x -10000', '4x +1000', '-']
```
## How it works
- Uses a set of base operators (add/sub/mul/div/pow/root/log against e)
- Uses (±10^p * e) for large-magnitude convergence
- Supports:
  - Greedy hill-climbing: Progresses from each step based on the optimal next move, stopping after N non-improving steps. No backtracking or foresight
  - Beam Search: Explores a decision tree, maintaining N many optimal branches as possible nodes for progression
  - Simulated Annealing: A probabilistic model to find the global optimum by modelling heat and cooling in metallurgy

## Current Limitations
- Just three algorithms to chose from
- Simulated Annealing has a capped run-time, meaning there is some variation between instances in the precision of the approximation
- Logging, while functional, is unpolished

## How to Run
```bash
python eproximatorInterface.py
```

## Requirements 
- Python 3.x
- Pytest


## Roadmap
- [x] Pytest testing
- [x] Alternate search algorithms
- [ ] Faster data look-up approach

## Key Learnings
- Hill-Climbing algorithmic search
- Beam Search Algorithm
- Simulated Annealing
- Floating-point precision handling
- CLI menu design
- File-based caching