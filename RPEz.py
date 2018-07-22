# Lifting Weight Calculator for computing the total weight being lifted by
# the user dependent on One Rep Max, Rep count, and RPE.
#
# Note: The weight being utilized in this program is in pounds (lb) not
#       kilograms (kg).  Kilograms will be added as an option in a
#       future update.
#
# AUTHOR: Willy Saronamihardja


'''
Lifting Chart dictionary works as follows:
Key: (Rep, RPE) -> Value: Percentage as a Decimal
'''
liftingChart = {(1, 6.5): .88, (1, 7.0): .89, (1, 7.5): .91, (1, 8.0): .92,
                (1, 8.5): .94, (1, 9.0): .96, (1, 9.5): .98, (1, 10.0): 1.00,
                (2, 6.5): .85, (2, 7.0): .86, (2, 7.5): .88, (2, 8.0): .89,
                (2, 8.5): .91, (2, 9.0): .92, (2, 9.5): .94, (2, 10.0): .96,
                (3, 6.5): .82, (3, 7.0): .84, (3, 7.5): .85, (3, 8.0): .86,
                (3, 8.5): .88, (3, 9.0): .89, (3, 9.5): .91, (3, 10.0): .92,
                (4, 6.5): .80, (4, 7.0): .81, (4, 7.5): .82, (4, 8.0): .84,
                (4, 8.5): .85, (4, 9.0): .86, (4, 9.5): .88, (4, 10.0): .89,
                (5, 6.5): .77, (5, 7.0): .79, (5, 7.5): .80, (5, 8.0): .81,
                (5, 8.5): .82, (5, 9.0): .84, (5, 9.5): .85, (5, 10.0): .86,
                (6, 6.5): .75, (6, 7.0): .76, (6, 7.5): .77, (6, 8.0): .79,
                (6, 8.5): .80, (6, 9.0): .81, (6, 9.5): .82, (6, 10.0): .84,
                (7, 6.5): .72, (7, 7.0): .74, (7, 7.5): .75, (7, 8.0): .76,
                (7, 8.5): .77, (7, 9.0): .79, (7, 9.5): .80, (7, 10.0): .81,
                (8, 6.5): .69, (8, 7.0): .71, (8, 7.5): .72, (8, 8.0): .74,
                (8, 8.5): .75, (8, 9.0): .76, (8, 9.5): .77, (8, 10.0): .79,
                (9, 6.5): .67, (9, 7.0): .68, (9, 7.5): .69, (9, 8.0): .71,
                (9, 8.5): .72, (9, 9.0): .74, (9, 9.5): .75, (9, 10.0): .76,
                (10, 6.5): .64, (10, 7.0): .65, (10, 7.5): .67,
                (10, 8.0): .68, (10, 8.5): .69, (10, 9.0): .71,
                (10, 9.5): .72, (10, 10.0): .74}


def printStartingMessage():
    '''
    Print to the user information regarding the program.
    '''
    print("----------  RPEz  ----------")
    print("Author: Willy Saronamihardja\n")
    print("No rest for the strong.")
    print("----------------------------\n\n")


# -------------------------- User Input Functions --------------------------


def obtainOneRepMax() -> int:
    '''
    Obtains the user's One Rep Max for his/her current lift.
    '''
    oneRepMax = input("Enter your One Rep Max (1RM) for the current lift: ")

    try:
        oneRepMax = int(oneRepMax)
    except:
        print("Please enter a valid number.")
        return obtainOneRepMax()
    else:      
        if oneRepMax < 0:
            print("Please enter a number above 0.")
            return obtainOneRepMax()
        else:
            return oneRepMax


def obtainTotalReps() -> int:
    '''
    Obtains the amount of reps the user will be doing per set.
    '''
    totalReps = input("Enter the amount of reps per set (1-10): ")

    try:
        totalReps = int(totalReps)
    except:
        print("Please enter a valid number.")
        return obtainTotalReps()
    else:
        if (totalReps < 0 or totalReps > 10):
            print("Please enter a number in-between and including 1 and 10.")
            return obtainTotalReps()
        else:
            return totalReps


def obtainRPE() -> float:
    '''
    Obtains the RPE the user will be doing for this workout.
    '''
    RPE = input("Enter the RPE per set (6.5-10 in increments of .5): ")

    try:
        RPE = float(RPE)
    except:
        print("Please enter a valid number.")
        return obtainRPE()
    else:
        if RPE < 6.5 or RPE > 10.0:
            print("Please enter a number in-between and including 6.5 and 10.0.")
            return obtainRPE()

        elif RPE % 0.5 != 0:
            print("Please enter a number with an increment of 0.5.")
            return obtainRPE()

        else:
            return RPE


def obtainNextAction() -> str:
    '''
    Obtains the user's input to determine next action of program execution.
    '''
    print("Type \"q\" without parentheses to end the program.")
    print("Type anything else to run the program again.")
    userInput = input()
    return userInput


# ----------------------- Weight Calculating Functions ----------------------


def calculateLiftingPercentage(reps, RPE) -> float:
    '''
    Determines the percentage of the One Rep Max for the working weight.
    '''
    return liftingChart[(reps, RPE)]

    
def calculateWorkingWeight(percentage, maxWeight) -> float:
    '''
    Calculates the working weight given One Rep Max and working percentage.
    '''
    return percentage * maxWeight


def calculateRoundedWorkingWeight(workingWeight) -> int:
    '''
    Calculates the rounded working weight into a number that can be
    properly met utilizing weights.
    '''
    remainder = workingWeight % 5

    if remainder > 2.4:
        toAdd = 5 - remainder
        roundedWorkingWeight = workingWeight + toAdd
    else:
        roundedWorkingWeight = workingWeight - remainder

    return int(roundedWorkingWeight)


def runCalculations(oneRepMax, reps, RPE) -> int:
    '''
    Calculates the actual working weight the user will be lifting per set and
    finds the weight needed to be loaded per side of the bar.
    '''
    percentage = calculateLiftingPercentage(reps, RPE)
    workingWeight = calculateWorkingWeight(percentage, oneRepMax)
    roundedWeight = calculateRoundedWorkingWeight(workingWeight)
    return roundedWeight


def calculateWeightPerSide(roundedWorkingWeight) -> float:
    '''
    Calculates the amount of weight the user should be putting on each
    individual side of the bar.
    '''
    return ((roundedWorkingWeight - 45) / 2)


def findWeightsToLoad(sideWeight, listOfWeights) -> list:
    '''
    Adds the weights needed to be added onto each side of the bar and adds
    the weight numbers into a list.
    '''
    if sideWeight == 0:
        listOfWeights.reverse()
        listOfWeights.append(0)
        return listOfWeights
    elif sideWeight - 45 >= 0:
        listOfWeights.append(45)
        findWeightsToLoad(sideWeight - 45, listOfWeights)
    elif sideWeight - 35 >= 0:
        listOfWeights.append(35)
        findWeightsToLoad(sideWeight - 35, listOfWeights)
    elif sideWeight - 25 >= 0:
        listOfWeights.append(25)
        findWeightsToLoad(sideWeight - 25, listOfWeights)
    elif sideWeight - 10 >= 0:
        listOfWeights.append(10)
        findWeightsToLoad(sideWeight - 10, listOfWeights)
    elif sideWeight - 5 >= 0:
        listOfWeights.append(5)
        findWeightsToLoad(sideWeight - 5, listOfWeights)
    elif sideWeight - 2.5 >= 0:
        listOfWeights.append(2.5)
        findWeightsToLoad(sideWeight - 2.5, listOfWeights)


# ------------------------- Weight Display Functions -------------------------

def printEndBar():
    '''
    Prints the end of one side of the bar.
    '''
    print("           _")
    print("          | |")
    print("          | |")

def printTwoPointFive():
    '''
    Prints a 2.5 lb weight.
    '''
    print("         _____")
    print("        /     \\")
    print("        | 2.5 |")
    print("        \_____/")

def printFive():
    '''
    Prints a 5 lb weight.
    '''
    print("       _______")
    print("      /       \\")
    print("      |   5   |")
    print("      \_______/")

def printTen():
    '''
    Prints a 10 lb weight.
    '''
    print("       ________")
    print("      /        \\")
    print("      |   10   |")
    print("      \________/")

def printTwentyFive():
    '''
    Prints a 25 lb weight.
    '''
    print("     ____________")
    print("    /            \\")
    print("    |     25     |")
    print("    \____________/")

def printThirtyFive():
    '''
    Prints a 35 lb weight.
    '''
    print("   ________________")
    print("  /                \\")
    print("  |       35       |")
    print("  \________________/")

def printFortyFive():
    '''
    Prints a 45 lb weight.
    '''
    print(" ____________________")
    print("/                    \\")
    print("|         45         |")
    print("\____________________/")

def printCenterBar():
    '''
    Prints the "center" of the bar.
    '''
    print("          | |")
    print("          | |")
    print("          | |")
    print("          | |")
    

def printBarImage(listOfWeights):
    '''
    Prints the image of the bar that the user should be lifting.
    '''
    printEndBar()

    if len(listOfWeights) == 0:
        printCenterBar()

    else:
        for weight in listOfWeights:
            if weight == 45:
                printFortyFive()
            elif weight == 35:
                printThirtyFive()
            elif weight == 25:
                printTwentyFive()
            elif weight == 10:
                printTen()
            elif weight == 5:
                printFive()
            elif weight == 2.5:
                printTwoPointFive()
            elif weight == 0:
                printCenterBar()

def printWorkingSet(workingWeight, totalReps, RPE):
    '''
    Prints the information of the working set being lifted.
    '''
    if workingWeight <= 45:
        print("\nWorking Set:", 45)
    else:
        print("\nWorking Set:", workingWeight)
    print("Reps per Set:", totalReps, "at RPE", RPE, '\n')
    
# ----------------------- Main Function and Execution -----------------------

def runProgram():
    '''
    Uses the previously defined functions to execute the program.
    '''
    userInput = "z"
    printStartingMessage()

    while userInput != "q":
        oneRepMax = obtainOneRepMax()
        totalReps = obtainTotalReps()
        RPE = obtainRPE()
        
        roundedWeight = runCalculations(oneRepMax, totalReps, RPE)
        sideWeight = calculateWeightPerSide(roundedWeight)
        listOfWeights = list()
        findWeightsToLoad(sideWeight, listOfWeights)

        printBarImage(listOfWeights)
        printWorkingSet(roundedWeight, totalReps, RPE)
        
        userInput = obtainNextAction()
        
        print('\n')

    print("Thanks for using RPEz!")



runProgram()
