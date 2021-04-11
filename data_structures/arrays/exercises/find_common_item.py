# ==== KEY POINTS ====
# Return boolean if it finds common items 
# Input is a list of strings
# It's possible to have duplicated items
# Is there a change of the lists having more than 10 items? If so, is that a problem if we use a solution with quadratic complexity?
# Which one is more important: Space Complexity or Time Complexity?

list_input_1 = ['a', 'b', 'c']
list_input_2 = ['d', 'e', 'f', 'c']
list_input_3 = ['g', 'y']

# Brute Force Solution
# Time Complexity: O(a*b)
# Space Complexity: O(1)
def find_common_item_1(list1, list2): 
  for item in list1:
    if item in list2: return True

  return False    

def transform_list_hash_map(list1):
  list_hash_map = dict()

  for index, value in enumerate(list1):
    list_hash_map[value] = index
  
  return list_hash_map

# Better Solution regarding Time Complexity
# Time Complexity: O(a + b)
# Space Complexity: O(a)
def find_common_2(list1, list2): 
  list1_hash_map = transform_list_hash_map(list1)

  for item in list2:
    if item in list1_hash_map: return True

  return False    

print(find_common_2(list_input_1, list_input_2))
print(find_common_2(list_input_1, list_input_3))