"""
==== KEY POINTS ====
- Given an array of integers nums and an integer target, 
  return indices of the two numbers such that they add up to target
- Output: The array with the pair indexes & they don't need to be in order
- Each input would have exactly one solution,
"""

"""
==== SCALABLE SOLUTION ====
- Time Complexity: O(n)
- Space Complexity: O(n)
"""
def two_sum1(nums, target):
  complement_hash_map = {}

  for i, num in enumerate(nums):
    is_complement = num in complement_hash_map

    if is_complement:
      pair_i = complement_hash_map[num]

      return [pair_i, i]

    complement_hash_map[target - num] = i

# print(two_sum1([2,7,11,15], 9))
# print(two_sum1([3,2,4], 6))
# print(two_sum1([3,3], 6))

"""
==== BRUTE FORCE SOLUTION ====
- Time Complexity: O(n^2) 
- Space Complexity: O(1)
"""
def two_sum2(nums, target):
  nums_range = range(len(nums))

  for i in nums_range:
    num1 = nums[i]

    for j in nums_range[1:]:
      num2 = nums[j]

      if num1 + num2 == target:
        return [i, j]

print(two_sum2([2,7,11,15], 9))
print(two_sum2([3,2,4], 6))
print(two_sum2([3,3], 6))