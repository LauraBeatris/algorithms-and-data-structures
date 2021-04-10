def return_squares(numbers_list): # Big O => O(n) => The algorithm has to allocate memory for the same number of items as in the input list
  square_list = []

  for num in numbers_list:
    square_list.append(num * num)

  return square_list

return_squares([1, 2, 3, 4, 5])