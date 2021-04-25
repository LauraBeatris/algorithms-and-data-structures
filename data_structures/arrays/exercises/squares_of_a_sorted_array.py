""" 
==== KEY POINTS ====
- Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.
- Input is a list of positive/negative numbers
- nums.length <= 10^4
- nums[i] <= 10^4
- nums is sorted in non-decreasing order.
"""

"""
- Time Complexity: O(n) 
- Space Complexity: O(n)
"""
def squares_of_a_sorted_array(nums):
  return sorted(map(lambda num: num * num, nums))

# print(squares_of_a_sorted_array([-4,-1,0,3,10]))
# print(squares_of_a_sorted_array([-7,-3,2,3,11]))
