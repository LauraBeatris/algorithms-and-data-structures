class Array:
  def __init__(self):
    self.length = 0
    self.data = dict()

  def push(self, item):
    self.data[self.length] = item
    self.length += 1
    return self.data

  def get(self, index):
    return self.data.get(index)

  def pop(self): 
    lastItem = self.data.popitem()[1]
    self.length -= 1
    
    return lastItem

  def unshift(self, item):
    i = self.length - 1

    while i >= 0:
      self.data[i + 1] = self.data.get(i)
      i -= 1
    
    self.data[0] = item
    self.length += 1

    return self.length

  def delete(self, index):
    i = index
    deletedItem = self.get(index)

    while i < self.length - 1:
      self.data[i] = self.get(i + 1)
      i += 1

    self.data.pop(index)
    self.length -= 1

    return deletedItem

array1 = Array()

# ["Hello", "What's up", "What's your name?"]
array1.push("Hello")
array1.push("What's up")
array1.push("What's your name?")
print(f"Push: {array1.data}, Array length: {array1.length}")

# ["Hello", "What's up"]
array1.pop() 
print(f"Pop: {array1.data}, Array length: {array1.length}")

# ["Hello", "What's up", "Nice!"]
array1.push("Nice!")
print(f"Push: {array1.data}, Array length: {array1.length}")

# [1, "Hello", "What's up", "Nice!"]
array1.unshift(1)
print(f"Unshift: {array1.data}, Array length: {array1.length}")

# [1, "Hello", "Nice!"]
array1.delete(2)
print(f"Delete: {array1.data}, Array length: {array1.length}")