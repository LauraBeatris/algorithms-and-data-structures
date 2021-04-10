""""
    What's the Big O Notation of the following algorithm?
"""

def another_function():
    return

def fun_challenge(input): 
    a = 10 # O(1)
    a = 50 + 3 # O(1)

    for i in range(len(input)): # O(n)
        another_function() # O(n)
        stranger = True # O(n) 
        a += 1 # O(n)
    
    return a # O(1)

best_case_scenario_input = [1]
average_case_scenario_input = [1] * 10
worst_case_scenario_input = [1] * 1000

fun_challenge(worst_case_scenario_input) 

# Big O Notation: O(3 + 4n) = O(n)