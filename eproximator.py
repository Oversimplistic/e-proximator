import math

numSteps = 0
steps = 0
bestPath = []
bestPathCondensed = []
bestPathCondensedFormatted = []
bestApprox = math.e

symbolMap = {
    "add": "+",
    "sub": "-",
    "mul": "*",
    "div": "/",
    "pow": "^e",
    "root": "^1/e",
    "log": "ln",
}


# Helper Functions----------------------------------

def closest_value(my_list, target):
    '''
    Determines which value, from a selection, is cloest to the target
    Args:
        my_list: A list of numbers
        target: The target value
    Returns:
        The index of the closest value to the target
    '''
    idx = min(range(len(my_list)), key=lambda i: abs(my_list[i] - target))
    return idx, my_list[idx]


def goodOperation(func, term):
    '''
    Confirms that the output is a number, and is not infinite
    Args:
        func: the function being tested
        term: the term being tested
    Returns:
        If not a number or infinite: None
        If a number, and not infinite: val
        Else: None
    '''

    try:
        val = func(term)
        if val is None or math.isnan(val) or math.isinf(val):
            return None
        return val
    except:
        return None


def methodCompression(list):
    '''
    Condenses the list of steps to merge repeated steps into 'step x n'
    Args:
        list: list of steps taken
    Returns:
        if List is none: [] and 0
        if List is a list: Compressed list and the number of repeated steps
    '''
    repeatedSteps = 0
    if not list:
        return [], repeatedSteps

    compressed = []
    count = 1

    for i in range(1, len(list)):
        if list[i] == list[i - 1]:
            count += 1
        else:
            if count > 1:
                compressed.append(f"{count}x {list[i - 1]}")
                repeatedSteps = repeatedSteps + count
            else:
                compressed.append(list[i - 1])
            count = 1

    if count > 1:
        compressed.append(f"{count}x {list[-1]}")
    else:
        compressed.append(list[-1])

    return compressed, repeatedSteps


# Operations------------------------------------------

#Add an e
def add(term): return term + math.e

#Subtract an e
def sub(term): return term - math.e

#Multiply by e
def mul(term): return term * math.e

#Divide by e
def div(term): return term / math.e

#To the power of e
def power(term): return term ** math.e if term >= 0 else None

#Root by e
def root(term): return term ** (1 / math.e) if term >= 0 else None

#Take the Natural Log
def log(term): return math.log(term, math.e) if term > 0 else None

def generate_scale_ops(max_power=30):
    '''Generates magnitude adjustments up to 30 sig. fig.'''
    ops = []
    names = []

    for p in range(max_power + 1):
        scale = 10 ** p

        # add
        ops.append(lambda x, s=scale: x + s * math.e)
        names.append(f"add_{scale}")

        # subtract
        ops.append(lambda x, s=scale: x - s * math.e)
        names.append(f"sub_{scale}")

    return ops, names


scale_ops, scale_names = generate_scale_ops(30)

# Operator Names-----------------------------------------------------------

operations = [add, sub, mul, div, power, root, log] + scale_ops
op_names = ["add", "sub", "mul", "div", "pow", "root", "log"] + scale_names

# active_operations = operations
# active_op_names = op_names

for name in op_names:
    if name.startswith("add_"):
        scale = name.split("_")[1]
        symbolMap[name] = f"+{scale}"
    elif name.startswith("sub_"):
        scale = name.split("_")[1]
        symbolMap[name] = f"-{scale}"

assert len(operations) == len(op_names), "Mismatch in operations and op_names"


# Function for one cycle----------------------------------------------------------------

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

def run_approximator(goal: float, bestApprox, steps):
    ''' Runs the Greedy Hill-Climbing algorithm.
    Args:
        goal (float): goal term
        bestApprox: bestApproximation so far
        steps: number of steps taken so far
    '''
    bestPath = []
    bestPathCondensedFormatted = []
    lastError = abs(bestApprox - goal)
    sameOpCounter = 0
    lastOp = None

    while True:
        newApprox, op = cycle(bestApprox, goal)
        newError = abs(newApprox - goal)
        steps += 1

        if newError < lastError:
            bestApprox = newApprox
            bestPath.append(op)
            lastError = newError
            #print(f"{bcolours.OKGREEN} Step {steps}: {bestApprox:.6f} (via {op}) error={newError:.6f}")

        else:
            if op == lastOp:
                sameOpCounter += 1
            else:
                sameOpCounter = 0
            lastOp = op

            if sameOpCounter >= 5:
                #print("Stuck")
                break

        if newError < 0.00000001 or steps>100000000:
            #print("Done")
            break


    print(f"You were aiming for:", goal)
    print(f"Best Approximation:", bestApprox)

    bestPathCondensed, repeatedSteps = methodCompression(bestPath)
    for item in bestPathCondensed:
        if "x " in item:
            count, op_name = item.split("x ")
            bestPathCondensedFormatted.append(f"{count}x {symbolMap[op_name]}")
        else:
            bestPathCondensedFormatted.append(symbolMap[item])


    print(f"Best Path", "->", (bestPathCondensedFormatted))

    totalSteps = len(bestPath)

    return bestApprox, bestPathCondensedFormatted, totalSteps
