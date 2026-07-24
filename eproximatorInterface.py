
#Import functions from various locations

from eproximator import run_approximator, bestApprox, steps
from eproximatorLoggingAlgorithm import growDataSet, searchDataSet

#Import useful modules

import time

#Colours

class bcolours:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'

colourList = [
    "HEADER",
    "OKBLUE",
    "OKGREEN",
    "WARNING",
    "FAIL",
]

#Key Variable Definitions

timeDelayVariable = 1
colourChangeVariable = "OKGREEN"


# Action selection Module

def actionSelector():
    while True:
        freeLines(1)
        print(f"{colourCode()}Please select an action:")
        for i, name in enumerate(actionList):
            print(f"{i+1}: {name}")
        choice = input(f"\n\nSelect an Action:")
        if choice.isdigit() and (int(choice)-1) in range(len(actionList)):
            action_name = actionList[int(choice)-1]
            function = functionList[action_name]
            function()
            time.sleep(timeDelayVariable)


        elif choice in actionList:
            function = functionList[choice]
            function()
            time.sleep(timeDelayVariable)

        else:
            print(f"Not a valid choice!")


#Run Eproximator Module

def runEproximatorHelper():
    value = (input("What are we approximating?"))
    if value.isdigit():
        run_approximator(int(value), bestApprox, steps)
    else:
        print ("Not an integer")
        runEproximatorHelper()


# Settings Page

def settingSelector():
    while True:
        print(f"Please select a setting:")
        for i, name in enumerate(settingList):
            print(f"{i+1}: {name}")

        choice = input("\nSelect an Action: ")

        # --- Number choice ---
        if choice.isdigit() and (int(choice) - 1) in range(len(settingList)):
            setting_name = settingList[int(choice)-1]
            func = settingFunctionList[setting_name]
            func()
            time.sleep(timeDelayVariable)
            freeLines(10)
            return

        # --- Name choice ---
        elif choice in settingList:
            func = settingFunctionList[choice]
            func()
            time.sleep(timeDelayVariable)
            freeLines(10)
            return

        else:
            print("Not a valid choice!\n")

def growDataSetScopeFunction():
    choice = int(input(f"Would you like to:\n1. Grow the Data Set from Zero\n2. Verify for a specific range"))
    if choice == 1:
        growDataSet(0,12345,12345)
    elif choice == 2:
        while True:
            minV = int(input(f"Enter Minimum Value: "))
            maxV = int(input(f"Enter Maximum Value: "))
            if maxV>minV:
                break
        growDataSet(0, minV, maxV)
        freeLines(10)
        return

def timeDelay():
    global timeDelayVariable
    newDelay = input(f"What would you like the time delay to be? Currently: {timeDelayVariable}\n")
    timeDelayVariable = int(newDelay)

def colourChange():
    global colourChangeVariable

    while True:
        print("Available colours:")
        for i, name in enumerate(colourList):
            print(f"{i + 1}: {name}")

        colourChoice = input(
            f"What colour would you like to use? (Current: {colourChangeVariable})\n"
        ).strip()

        # --- Case 1: User enters a number ---
        if colourChoice.isdigit():
            idx = int(colourChoice) - 1
            if 0 <= idx < len(colourList):
                new_colour = colourList[idx]
            else:
                print("Not a valid number.\n")
                continue

        # --- Case 2: User enters a name ---
        elif colourChoice in colourList:
            new_colour = colourChoice

        else:
            print("Not a valid choice!\n")
            continue

        # --- No change needed ---
        if new_colour == colourChangeVariable:
            print("That colour is already selected.\n")
            return

        # --- Apply change ---
        colourChangeVariable = new_colour
        time.sleep(timeDelayVariable)

        return

def colourCode():
    return getattr(bcolours, colourChangeVariable)

#Define list of Actions and variable names via a dictionary

actionList = [

    "Run Approximator",
    "Grow Data Set",
    "Search Data Set",
    "Settings",
]

functionList = {
    "Run Approximator": runEproximatorHelper,
    "Grow Data Set": growDataSetScopeFunction,
    "Search Data Set": searchDataSet,
    "Settings": settingSelector,

}

settingList = [
    "Time Delay",
    "Colour Change",
]

settingFunctionList = {
    "Time Delay": timeDelay,
    "Colour Change": colourChange,
}

#Handy rendering function

def freeLines(n):
    for i in range(n):
        print("\n")

#Welcome Page

print(f"{colourCode()}=========================================================================================================="
      f"\n"
      f"\n"
      f"                               Welcome to the (e)proximator API!"
      f"\n"
      f"\n"
      f"  This is a selection of optimised algorithms to get best approximations of values using exclusively e"
      f"\n"
      f"\n"
      f"==========================================================================================================="
      f"\n"
      f"\n"

)

actionSelector()







