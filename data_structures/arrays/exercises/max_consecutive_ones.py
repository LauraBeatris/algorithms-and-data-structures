"""
==== KEY POINTS ====
- Given a binary array of numbers, return the maximum number of consecutive 1's in the array.
- Output: The maximum number of consecutive 1's in the array.
- nums[i] is either 0 or 1.
"""

""" 
- Time Complexity: O(n) 
- Space Complexity: O(1)
"""
def max_consecutive_ones1(binaryNums):
  result = 0
  count = 0 

  for num in binaryNums: 
    # If num is zero, then it's going to reset the count
    count = (count + num) * num
    result = max(count, result)

  return result

# print(max_consecutive_ones1([1, 1, 0, 1, 1, 1]))
# print(max_consecutive_ones1([1 ,0, 1, 1, 0, 1]))

""" 
- Time Complexity: O(n) 
- Space Complexity: O(1)
"""
def max_consecutive_ones2(binaryNums):
  result = 0
  count = 0 

  for num in binaryNums: 
    if num == 1:
      count += 1
      continue 

    """
    Handle consecutive 1's in the end of the list since it won't stop on a zero number
    """
    result = max(count, result)
    count = 0

  result = max(count, result)

  return result

print(max_consecutive_ones2([1, 1, 0, 1, 1, 1]))
print(max_consecutive_ones2([1 ,0, 1, 1, 0, 1]))