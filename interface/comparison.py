from algorithms.hill_climbing_algorithm import run_hill_climber
from algorithms.beam_search_algorithm import beamSearch
from algorithms.simulated_annealing_algorithm import run_simulated_annealing

def compare(goal, startingValue):
    results = [None, None, None]

    results[0] = run_hill_climber(goal, startingValue, 0)
    results[1] = run_simulated_annealing(goal, startingValue)
    results[2] = beamSearch(goal, startingValue)

    methods = ["Hill Climbing Algorithm", "Simulated Annealing Algorithm", "Beam Search Algorithm"]

    print("Hill climbing results:")
    print(results[0])
    print("Simulated annealing results:")
    print(results[1])
    print("Beam search results:")
    print(results[2])

    errors = [results[0][3], results[1][4], results[2][2]]

    bestMethod = errors.index(min(errors))
    print(f"Best Method: {methods[bestMethod]}. Error of {errors[bestMethod]}")
    print(f"Optimal Path is: {results[bestMethod][0]}")


def logCompare(goal, startingValue):
    results = [None, None, None]

    results[0] = run_hill_climber(goal, startingValue, 0)
    results[1] = run_simulated_annealing(goal, startingValue)
    results[2] = beamSearch(goal, startingValue)

    errors = [results[0][3], results[1][3], results[2][3]]
    bestMethod = errors.index(min(errors))

    return results[bestMethod]
