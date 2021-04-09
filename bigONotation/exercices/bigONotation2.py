""""
    What's the Big O Notation of the following algorithm?
"""

def anotherFunChallenge(input):
  a = 5 # O(1)
  b = 10 # O(1)
  c = 50 # O(1)

  i = 0 # O(1)
  while i < input:  # O(n)
    x = i + 1 # O(n)
    y = i + 2 # O(n)
    z = i + 3 # O(n)

  j = 0 # O(1)
  while j < input: # O(n)
    p = j * 2 # O(n)
    q = j * 2 # O(n)
  
  whoAmI = "I don't know" # O(1)

bestCaseScenarioInput = 1
averageCaseScenarioInput = 10
worstCaseScenarioInput = 1000

anotherFunChallenge(worstCaseScenarioInput)

# Big O Notation: O(7 + 7n) = O(n)