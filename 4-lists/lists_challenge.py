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

print("--- Challenge 1 Results ---")
print(numbers)
# ----------------------------------------------------------
# Challenge 2: Larger List
# ----------------------------------------------------------

# Did you know that many of the world's first programmers were women and that their contributions
# helped end World War II and get John Glenn safely into orbit around the Earth? Learn more about
# these incredible women below: 
# ENIAC programmers: https://www.nytimes.com/2019/02/13/magazine/women-coding-computer-programming.html
# The real Black Women behind "Hidden Figures": https://www.nasa.gov/modernfigures

# Write a function that accepts two parameters (`list1` and `list2`) and prints the last element of
# whichever list that contains more elements. If both lists are the same size, it should print the
# last element of `list1`.

# You may see lists coded in either of the following two ways -- both are accepted by Python!

# Each element on its own line
eniac_programmers = [
    "Kathleen McNulty", 
    "Jean Jennings", 
    "Betty Snyder", 
    "Marlyn Wescoff", 
    "Frances Bilas", 
    "Ruth Lichterman"
    ]

# elements continue one after the other
nasa_human_computers = ["Mary W. Jackson", "Katherine Johnson", "Dorothy Vaughan"]

def last_element_of_larger_list(list1, list2):
  # REPLACE "pass" WITH YOUR CODE
  pass

print("--- Challenge 2 Results ---")
last_element_of_larger_list(eniac_programmers, nasa_human_computers)

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

print("--- Challenge 3 Results ---")
more_than_n(numbers, item, n)

#----------------------------------------------------------
# Challenge 4: Append Size
#----------------------------------------------------------

# Write a function that accepts a list with an input parameter called `the_list`. Your 
# function will append the size of the input list to the end of the input list. The function 
# should then print this new list. For example, if the input list was ["apple", "orange", "banana"],
# the code should print ["apple", "orange", "banana", 3] because the size of the input list was 3.

def append_size(the_list):
  # REPLACE "pass" WITH YOUR CODE
  pass

print("--- Challenge 4 Results ---")
print("The results of the append on the ENIAC programmers list is:")
append_size(eniac_programmers)

print("The results of the append on the NASA human computers list is:")
append_size(nasa_human_computers)

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

print("--- Challenge 5 Results ---")
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

print("--- Challenge 6 Results ---")
print(average_president_age(president_ages))

#----------------------------------------------------------
# Challenge 7: Name lengths
#----------------------------------------------------------

# Write a function that accepts a list of names, and returns the longest name in the list. Call the
# function with the names of 5 friends.

def longest_name(names):
  # REPLACE "pass" WITH YOUR CODE
  pass

names = ["Ron", "Donna", "April", "Leslie", "Ann"]

print("--- Challenge 7 Results ---")
print(longest_name(names))
