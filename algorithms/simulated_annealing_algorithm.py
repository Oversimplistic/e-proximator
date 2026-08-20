import math
import random

from algorithms.generalfunctions import operations, op_names, goodOperation, methodCompression, symbolMap

def randomCycle(term):
    '''
    Generates a random term and its output
    Args:
        term: the goal term
    Returns:
        Result: the output of the operation
        op_names[idx]: the operator used in this instance
    '''
    indices = list(range(len(operations)))
    random.shuffle(indices)

    for idx in indices:
        op = operations[idx]
        result = goodOperation(op, term)
        if result is not None:
            return result, op_names[idx]

    return None, None

def run_simulated_annealing(goal: float, startApprox=math.e, startingSteps = 0,
                            initial_temp = 1000.0,
                            cooling_rate = 0.995,
                            min_temp = 1e-8,
                            reheat_time = 200,
                            max_reheats = 300,
                            hard_stall_limit = 5_000_000):

    '''Runs the Simulated Annealing Algorithm
    Args:
        goal: the goal term
    Returns:
        overallBest: the best approximation so far
        overallBestPath: the best path so far
        steps: number of steps taken
        accepted: number of moves accepted
    '''

    currentApprox = startApprox
    currentError = abs(currentApprox - goal)
    currentPath = []

    overallBest = currentApprox
    overallBestError = currentError
    overallBestPath = []

    temp = initial_temp
    steps = startingSteps
    accepted = 0
    stepsSinceImprovement = 0
    reheatCount = 0


    while steps < 100_100_100:

        if steps % 100_000 == 0 and steps != 0:
            print(f"Step {steps}: best error so far = {overallBestError:.10f}, temp = {temp:.6f}")

        steps += 1

        newApprox, op = randomCycle(currentApprox)

        if newApprox is None:
            continue

        newError = abs(newApprox - goal)
        delta = newError - currentError

        if temp > min_temp:
            if delta < 0:
                acceptProbability = 1.0
            else:
                acceptProbability = math.exp(-delta / temp)

        else:
            acceptProbability = 1.0 if delta < 0 else 0.0

        if random.random() < acceptProbability:
            currentApprox = newApprox
            currentError = newError
            currentPath.append(op)
            accepted += 1

            if currentError < overallBestError:
                overallBest = currentApprox
                overallBestError = currentError
                overallBestPath = currentPath.copy()
                stepsSinceImprovement = 0
            else:
                stepsSinceImprovement += 1
        else:
            stepsSinceImprovement += 1

        temp *= cooling_rate

        if stepsSinceImprovement >= reheat_time:
            temp = initial_temp * 0.5
            stepsSinceImprovement = 0
            reheatCount += 1

            if reheatCount >= max_reheats:
                print(f"Stuck: no improvement after {max_reheats} reheat steps"
                      f"({steps} total steps). Best Error: {overallBestError:.10f}")
                break

        if steps - startingSteps > hard_stall_limit and stepsSinceImprovement > hard_stall_limit // 10:
            print(f"Hard Stall at step {steps}."
                  f"Best Error: {overallBestError:.10f}")
            break

        if overallBestError < 1e-8:
            break

    error = abs(goal-overallBest)

    bestPathCondensedFormatted = []
    bestPathCondensed, repeatedSteps = methodCompression(overallBestPath)
    for item in bestPathCondensed:
        if "x " in item:
            count, op_name = item.split("x ")
            bestPathCondensedFormatted.append(f"{count}x {symbolMap[op_name]}")
        else:
            bestPathCondensedFormatted.append(symbolMap[item])

    return bestPathCondensedFormatted, overallBest, steps, error



