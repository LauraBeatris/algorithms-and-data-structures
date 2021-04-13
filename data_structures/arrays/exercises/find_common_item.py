""" 
==== KEY POINTS ====
- Return boolean if it finds common items 
- Input is a list of strings
- It's possible to have duplicated items
- Is there a change of the lists having more than 10 items? If so, is that a problem if we use a solution with quadratic complexity?
- Which one is more important: Space Complexity or Time Complexity?
"""

list_input_1 = ['a', 'b', 'c']
list_input_2 = ['d', 'e', 'f', 'c']
list_input_3 = ['g', 'y']

""" 
==== BRUTE FORCE SOLUTION ====
- Time Complexity: O(a*b)
- Space Complexity: O(1)
"""
def find_common_item_1(list1, list2): 
  for item in list1:
    if item in list2: return True

  return False    

""" 
==== SCALABLE SOLUTION ====
- Time Complexity: O(a + b)
- Space Complexity: O(a)
"""
def find_common_2(list1, list2): 
  list1_set = set(list1)

  for item in list2:
    if item in list1_set: return True

  return False    

print(find_common_2(list_input_1, list_input_2))
print(find_common_2(list_input_1, list_input_3))