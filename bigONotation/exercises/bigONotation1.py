""""
    What's the Big O Notation of the following algorithm?
"""

def anotherFunction():
    return

def funChallenge(input): 
    a = 10 # O(1)
    a = 50 + 3 # O(1)

    for i in range(len(input)): # O(n)
        anotherFunction() # O(n)
        stranger = True # O(n) 
        a += 1 # O(n)
    
    return a # O(1)

bestCaseScenarioInput = [1]
averageCaseScenarioInput = [1] * 10
worstCaseScenarioInput = [1] * 1000

funChallenge(worstCaseScenarioInput) 

# Big O Notation: O(3 + 4n) = O(n)