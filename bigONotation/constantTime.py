candies = ['chocolate', 'marshmallow', 'strawberry with chocolate'] * 1000000

def logFirstCandyFromList(candies):
    print(f'First candy: {candies[0]}') # O(1)

def logFirstTwoCandiesFromList(candies):
    print(f'First candy: {candies[0]}') # O(1)
    print(f'Second candy: {candies[1]}') # O(1)

logFirstCandyFromList(candies)

"""
logFirstCandyFromList Worst Case Scenario (1000000 candies): O(1) Constant Time  

logFirstTwoCandiesFromList Worst Case Scenario (1000000 candies): O(1) Constant Time 
"""

"""
=== What Big O Notation is used to represent Constant Time? === 

O(1)

=== When an operation has Constant Time? === 

Constant Time happens when the amount of operations remains the same (constant) even when the input size gets bigger 

=== What happens when an algorithm has more than one operation with Constant Time? ===  

In the end, O(3) which can be the sum of 3 Constant Time operations,
it's going to be summarize to O(1) because even if the input gets bigger, 
3 operations are going to be executed 
"""