""" 
==== KEY POINTS ====
- Given two non-empty arrays of integers, write a function that determines
  whether the second array is a subsequence of the first one.
- [1, 3, 4] form a subsequence of the array [1, 2, 3, 4]
"""

"""
- Time Complexity: O(n)
- Space Complexity: O(1)
"""
def is_valid_subsequence1(array, sequence):
  sequence_i = 0

  for num in array:
      if sequence_i == len(sequence):
        break

      has_sequence_num = num == sequence[sequence_i]

      if has_sequence_num:
          sequence_i += 1

  return sequence_i == len(sequence)


# print(is_valid_subsequence1([5, 1, 22, 25, 6, -1, 8, 10], [1, 6, -1, 10]))
# print(is_valid_subsequence1([5, 1, 22, 25, 6, -1, 8, 10], [5, 1, 22, 25, 6, -1, 8, 10, 12]))

"""
- Time Complexity: O(n)
- Space Complexity: O(1)
"""
def is_valid_subsequence2(array, sequence):
  sequence_i = 0
  array_i = 0

  while array_i < len(array) and sequence_i < len(sequence):
      array_num = array[array_i]
      sequence_num = sequence[sequence_i]

      has_sequence_num = array_num == sequence_num

      if has_sequence_num:
          sequence_i += 1

      array_i += 1

  return sequence_i == len(sequence)


print(is_valid_subsequence2([5, 1, 22, 25, 6, -1, 8, 10], [1, 6, -1, 10]))
print(is_valid_subsequence2(
    [5, 1, 22, 25, 6, -1, 8, 10], [5, 1, 22, 25, 6, -1, 8, 10, 12]))
