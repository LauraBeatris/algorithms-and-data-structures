"""
An algorithm has a complexity of O(n^2) if the runtime is quadratic according
to the input size. Refer to the following examples:
"""

arrayInput = ['a', 'b', 'c', 'd', 'e']

def logAllArrayPairs(array): # O(n^2) 
  firstPairElementIndex = 0
  secondPairElementIndex = 0

  while firstPairElementIndex < len(array):
    firstPairElement = array[firstPairElementIndex]

    while secondPairElementIndex < len(array):
      secondPairElement = array[secondPairElementIndex]
      print(f'{firstPairElement},{secondPairElement}')
      secondPairElementIndex += 1

    firstPairElementIndex += 1

def compressBoxesTwice(boxes1, boxes2): # O(a*b)
  for box in boxes1: 
    print(f'Compress {box}') 

    for box in boxes2: 
      print(f'Compress {box}') 

