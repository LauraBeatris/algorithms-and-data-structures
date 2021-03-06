"""
==== KEY POINTS ====
- Input: Collection of positive/negative/float numbers
- Output: boolean indicating if the pair was found 
- The memory isn't limited, so we can favor Time Complexity instead of Space Complexity
"""

list_without_pair_sum = [1, 2, 3, 9]
list_with_pair_sum = [1, 2, 4, 4]
sum_input = 8

""" 
==== BRUTE FORCE SOLUTION ====
- Time Complexity: O(n^2) 
- Space Complexity: O(1)
"""
def has_pair_with_sum_1(numbersList, targetSum): 
  for number1 in numbersList: 
    for number2 in numbersList[1:]:
      if (number1 + number2) == targetSum:
        return True 

  return False 

""" 
==== SCALABLE SOLUTION ====
- Time Complexity: O(n)
- Space Complexity: O(n)
"""
def has_pair_with_sum_2(numbersList, targetSum): 
  sum_complement_set = set([])

  for number in numbersList: 
    if number in sum_complement_set: return True

    sum_complement_set.add(targetSum - number)

  return False 

print(has_pair_with_sum_2(list_with_pair_sum, sum_input))
print(has_pair_with_sum_2(list_without_pair_sum, sum_input))
