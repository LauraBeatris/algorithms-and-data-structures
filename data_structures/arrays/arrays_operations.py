"""
=== Speed Complexity by Operation === 

- Lookup -> O(1) - Unshift -> O(n)
- Push -> O(1) - Insert -> O(n)
- Pop -> O(1) - Delete -> O(n)
"""

import collections

list1 = [1, 2, 3]

"""
 Deque is preferred over list in the cases where we need quicker append and pop operations from both the ends of container, 
 as deque provides an O(1) time complexity for append and pop operations as compared to list which provides O(n) time complexity.
"""
deque1 = collections.deque(list1)

## Lookup
print("Lookup", list1[0])

## Push
list1.append(1)
print("Push", list1)

## Pop
deque1.pop()
print("Pop", deque1)

## Unshift
deque1.appendleft(4)
print("Unshift", deque1)

## Shift
deque1.popleft()
print("Shift", deque1)