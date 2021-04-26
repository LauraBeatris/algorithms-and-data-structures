""" 
==== KEY POINTS ====
- Given a fixed length array arr of integers, duplicate each occurrence of zero, shifting the remaining elements to the right. 
- Do the above modifications to the input array in place, do not return anything from your function.
- arr.length <= 10000
- arr[i] <= 9
"""

"""
==== BRUTE FORCE SOLUTION (IN-PLACE) ====
Time Complexity: O(n^2) 
Space Complexity: O(1)
"""
def duplicate_zeros1(arr):
  length = len(arr)
  highest_length = length - 1

  for i in range(highest_length, -1, -1): 
    num = arr[i]
    should_duplicate_zero = num == 0 and i < highest_length

    if should_duplicate_zero:
      for j in range(highest_length, i, -1):
        is_out_of_range = j >= highest_length

        if not is_out_of_range:  
          arr[j + 1] = arr[j]

        j -= 1

      arr[i + 1] = 0
      
  print(arr)

# duplicate_zeros1([1, 0, 2, 3, 0, 4, 5, 0])
# duplicate_zeros1([1, 2, 3])

"""
==== SCALABLE SOLUTION (IN-PLACE) ====
Time Complexity: O(n) 
Space Complexity: O(1)
"""
def duplicate_zeros2(arr):
  length = len(arr)
  with_zeros_length = length + arr.count(0)
  
  i = length - 1
  j = with_zeros_length - 1
  while j >= 0:
      if j < length: arr[j] = arr[i]
      j -= 1

      if arr[i] == 0: 
          if j < length: arr[j] = arr[i]
          j -= 1
          
      i -= 1

  print(arr)


# duplicate_zeros2([1, 0, 2, 3, 0, 4, 5, 0])
# duplicate_zeros2([1, 2, 3])

"""
==== SCALABLE SOLUTION (EXTRA SPACE) ====
Time Complexity: O(n) 
Space Complexity: O(n)
"""
def duplicate_zeros3(arr):
  source = arr[:]

  i = j = 0
  n = len(arr)

  while j < n:
      arr[j] = source[i]
      j += 1

      if source[i] == 0: 
          if j < n: arr[j] = source[i]
          j += 1

      i += 1

  print(arr)

duplicate_zeros3([1, 0, 2, 3, 0, 4, 5, 0])
duplicate_zeros3([1, 2, 3])