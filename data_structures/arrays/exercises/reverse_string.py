""" 
==== KEY POINTS ====
- Given a string, return its reversed version
- Input: A string. It can't not be empty such as "" or null
- Is it possible to receive a string with less than 2 characters? Of so, validate this case
- The input can have multiple spaces such as "Hello,    my name is Laura"
"""

""" 
=== SOLUTIONS COMPLEXITIES ===
- Time Complexity: O(n)
- Space Complexity: O(n)
"""

def validate_string(string):
  is_invalid_string = len(string) < 2

  if (is_invalid_string): raise ValueError('Invalid String - The string needs to have at least 2 characters') 

# Using join + reversed built-in function
def reverse_string_1(string):
  validate_string(string)

  reversed_string = ''.join(reversed(string))

  return reversed_string 

# reverse_string_1("Hello Laura") # "aruaL olleH"
# reverse_string_1("Hello Laura,   what's up?") # "?pu s'tahw   ,aruaL olleH"
# reverse_string1("H") - Should raise error

# Using loop
def reverse_string_2(string):
  validate_string(string)

  reversed_string = ''

  index = len(string) - 1

  while index >= 0:
    reversed_string += string[index]
    index -= 1

  return reversed_string

# reverse_string_2("Hello Laura") # "aruaL olleH"
# reverse_string_2("Hello Laura,   what's up?") # "?pu s'tahw   ,aruaL olleH"

# Using slicing
def reverse_string_3(string):
  validate_string(string)

  """
    The slice statement means start at string length, end at position 0, move with the step -1
  """
  reversed_string = string[len(string):0:-1]

  return reversed_string

# reverse_string_3("Hello Laura") # "aruaL olleH"
# reverse_string_3("Hello Laura,   what's up?") # "?pu s'tahw   ,aruaL olleH"