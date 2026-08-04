# e-proximator - Numerical Approximation Using Only e

A CLI tool that approximates any target value using a sequence of operations built exclusively from Euler's number (e), via a greedy hill-climbing search over a defined operator set.

## Overview
The e-proximator functions by searching all possible next-steps, and choosing the optimal path forward - prioritising order of magnitude adjustments, and then refining from there.

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
- Currently, uses greedy hill-climbing, one step at a time with no backtracking to minimise error at each step, stopping after N non-improving steps

## Current Limitations
- Single-path search with no backtracking, and can therefore miss shorter paths for exponential/multiplicative methods

## How to Run
```bash
python eproximatorInterface.py
```

## Requirements 
- Python 3.x
- Pytest


## Roadmap
- [x] Pytest testing
- [ ] Alternate search algorithms
- [ ] Faster data look-up approach

## Key Learnings
- Hill-Climbing algorithmic search
- Floating-point precision handling
- CLI menu design
- File-based caching