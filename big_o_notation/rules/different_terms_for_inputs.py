"""
=== Big O Notations Rules - Different Terms for Inputs === 

What if an algorithm receives two different inputs and it depends on the size of both?
In that case, the Big O Notation should have different variables for each input, like the following:
- O(a + b)
- O(n*m)
"""

def compressBoxesTwice(boxes1, boxes2): # O(2a + 2b) => O(a + b)
  for box in boxes1: # O(a)
    print(f'Compress {box}') # O(a)

  for box in boxes2: # O(b)
    print(f'Compress {box}') # O(b)
