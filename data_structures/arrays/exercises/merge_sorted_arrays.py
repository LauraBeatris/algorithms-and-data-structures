""" 
==== KEY POINTS ====
- Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.
- Input: The number of elements initialized in nums1 and nums2 are m and n respectively. 
- nums1 has a size equal to m + n such that it has enough space to hold additional elements from nums2

- It's not needed to return the value but instead, reassign nums1 argument
"""

def should_merge_directly(n):
  if (n == 0): return True

"""
- Time Complexity: O(n + m)
- Space Complexity: O(1) - nums1 is already stored with additional space for later be merged with nums2
"""
def merge_sorted_arrays1(nums1, m, nums2, n):
  if should_merge_directly(n): 
    nums1 = nums1 + nums2
    print(nums1)

    return

  nums1[:] = sorted(nums1[:m] + nums2)
  print(nums1)

# merge_sorted_arrays1([1,2,3,0,0,0], 3, [4, 3.5, 9], 3)
# merge_sorted_arrays1([1,2,3,4,0,0], 4, [5, 0], 2)
# merge_sorted_arrays1([1,2,3], 3, [], 0)

"""
- Time Complexity: O(n + m)
- Space Complexity: O(1) 
"""
def merge_sorted_arrays2(nums1, m, nums2, n):
  if should_merge_directly(n): 
    nums1 = nums1 + nums2
    print(nums1)

    return

  nums1_size_with_merged_items = m + n
  for index in range(nums1_size_with_merged_items):
    if not index >= m: continue 

    nums1[index] = nums2.pop()

  nums1.sort()
  print(nums1)

merge_sorted_arrays2([1,2,3,0,0,0], 3, [4, 3.5, 9], 3)
merge_sorted_arrays2([1,2,3,4,0,0], 4, [5, 0], 2)
merge_sorted_arrays2([1,2,3], 3, [], 0)