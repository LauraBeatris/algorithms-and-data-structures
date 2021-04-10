"""
=== Big O Notations Rules - Remove Constants === 

The Big O Notation of a certain algorithm is always going to be one of the following:
- O(1) 
- O(log n)
- O(n)
- O(n log n)
- O(n^2) 
- O(2^n) 
- O(n!) 

That's why we remove constants, refer to the following examples:
- O(4n) = O(n)
- O(4n + 100) = O(n)

When referring to the Bio O Chart, what matters is how the line of operations moves
according to the input size and constants always remain the same when the input size gets bigger
"""

def compressBoxesTwice(boxes): # Big O = O(4n) => O(n)
  for box in boxes: # O(n)
    print(f'Compress {box}') # O(n)

  for box in boxes: # O(n)
    print(f'Compress {box}') # O(n)

def printFirstItemThenFirstHalfThenSayHiTen100Times(items): # Big O = O(7 + 3O(n/2)) => O(n)
  print(items[0]) # O(1)

  middleIndex = int(len(items) / 2) # O(1)
  i = 0 # O(1)

  while (i < middleIndex): # O(n/2)
    print(items[i]) # O(n/2)
    i += 1 # O(n/2)

  j = 0 # O(1)
  while j < 100: # O(1)
    print('hi') # O(1)
    j += 1  # O(1)