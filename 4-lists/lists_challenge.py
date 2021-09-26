# ----------------------------------------------------------
# Challenge 1: Append Sum
# ----------------------------------------------------------

# Write a function that accepts a list called `numbers` and adds the last two elements of `numbers`
# together and appends the result to `numbers`. For example, if the list started as [1, 1, 2], 
# calling this function three times would produce [1, 1, 2, 3, 5, 8].

def add_and_append(numbers):
  # REPLACE "pass" WITH YOUR CODE
  pass

numbers = [1, 1, 2]
add_and_append(numbers)
add_and_append(numbers)
add_and_append(numbers)
print(numbers)

# ----------------------------------------------------------
# Challenge 2: Larger List
# ----------------------------------------------------------

# Write a function that accepts two parameters (`list1` and `list2`) and prints the last element of
# whichever list that contains more elements. If both lists are the same size, it should print the
# last element of `list1`.

list1 = [4, 10, 2, 5]
list2 = [-10, 2, 5, 10]

def last_element_of_larger_list(list1, list2):
  # REPLACE "pass" WITH YOUR CODE
  pass

last_element_of_larger_list(list1, list2)

# ----------------------------------------------------------
# Challenge 3: More Than N
# ----------------------------------------------------------

# Write a function that accepts three parameters: `numbers`, `item`, and `n`. The function should
# print True if `item` appears in `numbers` more than `n` times, and False otherwise.

def more_than_n(numbers, item, n):
  # REPLACE "pass" WITH YOUR CODE
  pass

numbers = [2, 4, 6, 2, 3, 2, 1, 2]
item = 2
n = 3
more_than_n(numbers, item, n)

#----------------------------------------------------------
# Challenge 4: Append Size
#----------------------------------------------------------

# Write a function that accepts a list called `numbers` and appends the size of `numbers` to the end
# of `numbers`. The function should then print this new list. For example, if `numbers` was
# [23, 42, 108], the code should print [23, 42, 108, 3] because the size of `numbers` was 3.

def append_size(numbers):
  # REPLACE "pass" WITH YOUR CODE
  pass

numbers = [23, 42, 108]
append_size(numbers)

#----------------------------------------------------------
# Challenge 5: Combine Sort
#----------------------------------------------------------

# Write a function that combines two lists into one new list, sorts the result, and returns the new
# sorted list.

def combine_and_sort(list1, list2):
  # REPLACE "pass" WITH YOUR CODE
  pass

list1 = [4, 10, 2, 5]
list2 = [-10, 2, 5, 10]
print(combine_and_sort(list1, list2))

#----------------------------------------------------------
# Challenge 6: Average age
#----------------------------------------------------------

# Write a function that accepts a list of president ages, then returns the average age of those
# presidents. Call the function with the ages of the last 5 presidents.

def average_president_age(president_ages):
  # REPLACE "pass" WITH YOUR CODE
  pass

president_ages = [46, 54, 47, 70, 78]
print(average_president_age(president_ages))

#----------------------------------------------------------
# Challenge 7: Name lengths
#----------------------------------------------------------

# Write a function that accepts a list of names, and returns the longest name in the list. Call the
# function with the names of 5 friends.

def longest_name(names):
  # REPLACE "pass" WITH YOUR CODE
  pass

names = ["Leslie", "Ron", "Ann", "April", "Donna"]
print(longest_name(names))
