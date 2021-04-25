import math

""" 
==== KEY POINTS ====
- Given an array nums of integers, return how many of them contain an even number of digits.
- Input is a list of positive numbers
- nums.length <= 500
- nums[i] <= 10^5
"""

def is_even(num):
  return num % 2 == 0

def get_digits_quantity(num):
  return math.floor(math.log10(num)) + 1

""" 
- Time Complexity: O(n) 
- Space Complexity: O(1)
"""
def find_numbers_with_even_number_of_digits1(nums):
  result = 0

  for num in nums:
    if not is_even(get_digits_quantity(num)): continue 

    result += 1

  return result

# print(find_numbers_with_even_number_of_digits1([12,345,2,6,7896]))
# print(find_numbers_with_even_number_of_digits1([555,901,482,1771]))

""" 
- Time Complexity: O(n) 
- Space Complexity: O(1)
"""
def find_numbers_with_even_number_of_digits2(nums):
  return sum(is_even(get_digits_quantity(n)) for n in nums)

print(find_numbers_with_even_number_of_digits2([12,345,2,6,7896]))
print(find_numbers_with_even_number_of_digits2([555,901,482,1771]))