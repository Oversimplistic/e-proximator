from algorithms.generalfunctions import operations, op_names, goodOperation, methodCompression, symbolMap

beamWidth = 3 #Number of pathways pursued
maxDepth = 50 #Safety net to catch run away values

def nextSteps(currentValue):
    '''
    Generates the list of possible next steps by generating a list of what each function would produce
    Args:
        CurrentValue: The current value
    Returns:
        stepSelection: A list of possible next steps
        operator: A list of operators which mirrors the order in stepSelection
    '''
    stepSelection = []
    operator = []
    for i in range(len(operations)):
        op = operations[i]
        o = op_names[i]
        r = goodOperation(op, currentValue)
        if r is not None:
            stepSelection.append(r)
            operator.append(o)
        else:
            stepSelection.append(float("inf"))
            operator.append(o)
    return stepSelection, operator

def scoreFunction(currentValue, goal):
    '''
    Calculates the delta from the current value to the goal
    Args:
        currentValue: The current value
        goal: The goal value
    Returns:
        delta: The delta from the current value to the goal
    '''
    return abs(currentValue - goal)

def scoreSelection(goal, stepSelection):
    '''
    Creates a list of scores for every possible step
    Args:
        goal: The goal value
        stepSelection: A list of possible steps
    Returns:
        stepSelectionScore: a list of scores for the step selection
    '''
    stepSelectionScore = []
    for i in range(len(stepSelection)):
        step = stepSelection[i]
        if step == float("inf"):
            x = float("inf")
        else:
            x = scoreFunction(step, goal)
        stepSelectionScore.append(x)
    return stepSelectionScore

def beamSearch(goal, startingValue):
    '''
    Beam Search Algorithm
    Args:
        goal: the target value we're trying to reach
        startingValue: the value we start from
    Returns:
        bestValue: the closest value found to the goal
        bestPath: the list of operators that produced it, in order
    '''

    #Generates the scores for the possible next steps
    stepSelection, operator = nextSteps(startingValue)
    scores = scoreSelection(goal, stepSelection)

    #Sorts and pairs steps and operations by their scores
    sortedPairs = sorted(zip(stepSelection, operator, scores), key=lambda p: p[2])

    #Initalises the beam and adds pathways
    beam = []
    for i in range(beamWidth):
        value, op, score = sortedPairs[i]
        beam.append((value, [op], score))

    #Tracks the overall best value so far
    bestValue, bestPath, bestScore = min(beam, key=lambda c: c[2])

    depth = 1
    while depth < maxDepth:

        #A stop if the value is hit exactly
        if bestScore == 0:
            break

        #Finds the best possible candidates by indexing through pathways
        candidates = []
        for value, path, score in beam:
            stepSelection, operator = nextSteps(value)
            scores = scoreSelection(goal, stepSelection)
            for newValue, op, newScore in zip(stepSelection, operator, scores):
                if newValue == float("inf"):
                    continue
                candidates.append((newValue, path + [op], newScore))

        if not candidates:
            break

        #Sorts the candidates by their newScore
        candidates.sort(key=lambda c: c[2])
        beam = candidates[:beamWidth]

        roundBestValue, roundBestPath, roundBestScore = beam[0]
        if roundBestScore < bestScore:
            bestValue, bestPath, bestScore = roundBestValue, roundBestPath, roundBestScore

        depth += 1

    error = abs(goal - bestValue)

    bestPathCondensedFormatted = []
    bestPathCondensed, repeatedSteps = methodCompression(bestPath)
    for item in bestPathCondensed:
        if "x " in item:
            count, op_name = item.split("x ")
            bestPathCondensedFormatted.append(f"{count}x {symbolMap[op_name]}")
        else:
            bestPathCondensedFormatted.append(symbolMap[item])

    return bestPathCondensedFormatted, bestValue, depth, error

