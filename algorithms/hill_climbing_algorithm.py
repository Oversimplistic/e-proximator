from algorithms.generalfunctions import *


def cycle(term, goal):
    '''
    Runs one cycle of approximations for greedy hill-climbing, finding the best operation and closest value
    Args:
        term (float): current term
        goal (float): goal term
    Returns:
        bestVal: Closest value so far
        bestOp: Op to find the best operation on this cycle
    '''
    results = []
    for op in operations:
        r = goodOperation(op, term)
        if r is not None:
            results.append(r)
        else:
            results.append(float("inf"))
    idx, bestVal = closest_value(results, goal)
    bestOp = op_names[idx]
    return bestVal, bestOp


def run_hill_climber(goal: float, bestApprox, steps):

    ''' Runs the Greedy Hill-Climbing algorithm.
    Args:
        goal (float): goal term
        bestApprox: bestApproximation so far
        steps: number of steps taken so far
    '''

    bestPath = []

    lastError = abs(bestApprox - goal)
    nonImprovingStreak = 0

    while True:
        newApprox, op = cycle(bestApprox, goal)
        newError = abs(newApprox - goal)
        steps += 1

        if newError < lastError:
            bestApprox = newApprox
            bestPath.append(op)
            lastError = newError
            nonImprovingStreak = 0

        else:
            nonImprovingStreak += 1
            if nonImprovingStreak >= 10:
                break

        if newError < 0.00000001 or steps>100000000:
            break

    bestPathCondensedFormatted = []
    bestPathCondensed, repeatedSteps = methodCompression(bestPath)
    for item in bestPathCondensed:
        if "x " in item:
            count, op_name = item.split("x ")
            bestPathCondensedFormatted.append(f"{count}x {symbolMap[op_name]}")
        else:
            bestPathCondensedFormatted.append(symbolMap[item])



    totalSteps = len(bestPath)

    error = abs(goal-bestApprox)
    return bestPathCondensedFormatted, bestApprox, totalSteps, error