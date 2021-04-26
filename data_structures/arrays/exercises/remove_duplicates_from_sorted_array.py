"""
==== KEY POINTS ====
- Given a sorted array nums, remove the duplicates in-place such that 
  each element appears only once and returns the new length.
- Output: The length of the nums array without duplicates
- nums is sorted in ascending order.
"""

"""
=== SCALABLE SOLUTION (IN-PLACE) ===
- Time Complexity: O(n)
- Space Complexity: O(1)
"""
def remove_duplicates1(nums):
  # Start index at second element because the first one is already unique
  i = 1

  while i < len(nums):
    is_unique = nums[i] != nums[i - 1]

    # Doesn't need to increase index if element is going to be deleted
    if is_unique:
      i += 1
    else:
      nums.pop(i)

  print(nums)

  return len(nums)

remove_duplicates1([1,1,2])
remove_duplicates1([0,0,1,1,1,2,2,3,3,4])

"""
=== ALLOCATING MEMORY ===
- Time Complexity: O(n)
- Space Complexity: O(n)
"""
def remove_duplicates2(nums):
  nums[:] = sorted(set(nums))

  print(nums)

  return len(nums)

remove_duplicates2([1,1,2])
remove_duplicates2([0,0,1,1,1,2,2,3,3,4])