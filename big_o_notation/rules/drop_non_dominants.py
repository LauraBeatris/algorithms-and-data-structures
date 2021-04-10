"""
=== Big O Notations Rules - Drop Non Dominants === 

Drop non dominants terms since these aren't going to change significantly 
the amount of operations according to the input size

In Big O, our main concern is scalability and as the input size gets larger, 
then we should analyze the operations that are going to significantly increase more

As you can see in the example below, the dominant operation is a nested for loop, which
has a quadratic complexity and can significantly increase more according to the input size
"""

def printAllNumbersThenAllPairSums(numbers): # Big O = O(n + n^2) => O(n^2)
  for number in numbers: # O(n)
    print(number)

  for number1 in numbers: # O(n^2) 
    for number2 in numbers:
      print(f'Pair sum: {number1 + number2}')

printAllNumbersThenAllPairSums([1, 2, 3, 4])