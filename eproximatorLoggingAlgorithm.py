from eproximator import run_approximator
import numpy as np
import time

t1 = 0
t2 = 0
finalt = 0

increment = 0

# Open file in append + read mode
f = open("eproximatorlog.txt", "a+")


def check(term):
    f.seek(0)
    content = f.readlines()
    if term < len(content):
        return content[term]
    else:
        return None

def growDataSet(increment, minV, maxV):

    if increment == 0 and maxV == minV:
        increment = 0
        maxV = 10000000000000000000000000000000000
    else:
        increment = minV


    while increment <= maxV:
        found_line = check(increment)
        if found_line:
            print(f"Found previous entry: {found_line.strip()}")
        else:
            t1 = time.time()
            newValue, path, totalSteps = run_approximator(increment)

            # Ensure numeric
            if totalSteps is None:
                totalSteps = 0

            # Logging
            t2 = time.time()
            tfinal = t2 - t1
            log_line = f"Goal: {increment}, Best Approximation: {newValue}, Delta: {newValue - increment}, Path: {path}, Total Steps: {totalSteps}, Time Taken: {tfinal}\n"
            f.write(log_line)
            f.flush()
            print(f"Logged new value: {increment}")

        increment += 1

def searchDataSet():
    global increment

    value = int(input("Enter the value to search: "))
    found_line = check(value)
    if found_line:
        print(f"Found previous entry: {found_line.strip()}")

    else:
        print(f"No previous entry")
        print(f"Calculating value now...")
        run_approximator(value)


#growDataSet()

