
#Import functions from various locations

from algorithms.generalfunctions import bestApprox, steps
from algorithms.hill_climbing_algorithm import run_hill_climber
from datahandling.logging.eproximatorLoggingAlgorithm import growDataSet, searchDataSet, wipeCache
from interface.comparison import compare

#Import useful modules

import time

#Colours

#Colours for text interface
class bcolours:

    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'

#List for colour selection, not all colour values in bcolours are currently enabled as options
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
    '''
    A function to allow selection of actions
    Currently specialised, but with the ability to be generalised to any actions list
    '''

    while True:
        freeLines(1)
        print(f"{colourCode()}Please select an action:")

        #Lists options
        for i, name in enumerate(actionList):
            print(f"{i+1}: {name}")
        choice = input(f"\n\nSelect an Action:")

        #Allows for numerical selection of actions from the list
        if choice.isdigit() and (int(choice)-1) in range(len(actionList)):
            action_name = actionList[int(choice)-1]
            function = functionList[action_name]
            function()
            time.sleep(timeDelayVariable)

        #Allows for string selection of actions from the list
        elif choice in actionList:
            function = functionList[choice]
            function()
            time.sleep(timeDelayVariable)

        #Handles non-valid action selections
        else:
            print(f"Not a valid choice! Must be a positive integer")



def runEproximatorHelper():
    '''
    A helper function to run the Eproximator
    Currently only supports integer values due to internal logic
    '''

    value = int((input("What are we approximating?")))
    run_hill_climber(int(value), bestApprox, steps)
    compare(value, 0)



def settingSelector():
    '''
    A function to allow the selection of settings
    '''
    while True:
        print(f"Please select a setting:")
        for i, name in enumerate(settingList):
            print(f"{i+1}: {name}")

        choice = input("\nSelect an Action: ")

        #  Allows for numerical selection
        if choice.isdigit() and (int(choice) - 1) in range(len(settingList)):
            setting_name = settingList[int(choice)-1]
            func = settingFunctionList[setting_name]
            func()
            time.sleep(timeDelayVariable)
            freeLines(10)
            return

        # Allows for string selection
        elif choice in settingList:
            func = settingFunctionList[choice]
            func()
            time.sleep(timeDelayVariable)
            freeLines(10)
            return

        # Support for incorrect selections
        else:
            print("Not a valid choice!\n")

def growDataSetScopeFunction():
    '''
    A function to allow the growth of the approximations cache
    '''
    while True:
        choice = (input(f"Would you like to:\n1. Grow the Data Set from Zero\n2. Verify for a specific range"))
        if choice.isdigit():
            choice = int(choice)
            break
        elif not choice.isdigit():
            print("Must be a positive integer")
        else:
            print("Not a valid choice!")

    if choice == 1:
        growDataSet(0,12345,12345)
    elif choice == 2:
        while True:

            while True:
                minV = input(f"Enter Minimum Value: ")
                if minV.isdigit():
                    minV = int(minV)
                    break
                elif not minV.isdigit():
                    print("Must be a positive integer")
                else:
                    print("Not a valid choice!")


            while True:
                maxV = (input(f"Enter Maximum Value: "))
                if maxV.isdigit():
                    maxV = int(maxV)
                    break
                elif not maxV.isdigit():
                    print("Must be a positive integer")
                else:
                    print("Not a valid choice!")

            if maxV>minV:
                break
            elif maxV==minV:
                print("Those are the same values. Maximum and Minimum cannot be equal")
            elif maxV<minV:
                print("Maximum cannot be less than minimum")
            else:
                print("Error in grow data set CLI query")

        growDataSet(0, minV, maxV)
        freeLines(5)
        return

def timeDelay():
    '''
    Adds a delay to print statements
    '''
    global timeDelayVariable
    newDelay = input(f"What would you like the time delay to be? Currently: {timeDelayVariable}\n")
    timeDelayVariable = int(newDelay)

def colourChange():
    '''
    Allows for colours in the CLI to be changed
    :return:
    '''
    global colourChangeVariable

    while True:
        print("Available colours:")
        for i, name in enumerate(colourList):
            print(f"{i + 1}: {name}")

        colourChoice = input(
            f"What colour would you like to use? (Current: {colourChangeVariable})\n"
        ).strip()

        # Numerical Selection
        if colourChoice.isdigit():
            idx = int(colourChoice) - 1
            if 0 <= idx < len(colourList):
                new_colour = colourList[idx]
            else:
                print("Not a valid number.\n")
                continue

        # String Selection
        elif colourChoice in colourList:
            new_colour = colourChoice

        # Edge cases
        else:
            print("Not a valid choice!\n")
            continue

        # Same colour
        if new_colour == colourChangeVariable:
            print("That colour is already selected.\n")
            return

        # Actions colour change
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
    "Wipe Cache"
]

settingFunctionList = {
    "Time Delay": timeDelay,
    "Colour Change": colourChange,
    "Wipe Cache": wipeCache
}

#Handy rendering function

def freeLines(n):
    '''
    Prints n lines of blank text
    Args:
        n (int): Number of lines to print
    '''

    for i in range(n):
        print("\n")


print(f"{colourCode()}=========================================================================================================="
      f"\n"
      f"\n"
      f"                                 Welcome to the (e)proximator!"
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







