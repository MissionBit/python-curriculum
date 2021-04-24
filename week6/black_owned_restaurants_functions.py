# Black-Owned Restaurant Finder: Functions exercises

############################################ Exercise 1 ############################################
# With functions, we can generalize the code that we wrote from the previous while-loop exercise to
# ask the user *any* question and make sure they choose from *any* list of options. Using your code
# from the previous exercise, write a function that accepts a prompt and a list of options. The
# function should repeatedly ask the user the prompt until the user has typed in one of the options,
# at which point the function should return what the user typed in. Use your function to ask the
# user whether they would like takeout or delivery, then to ask which cuisine they would like (for
# the cuisine question, come up with a list of 3 supported cuisines).

# YOUR CODE HERE

############################################ Exercise 2 ############################################
# Functions can even take another function as an input! https://tinyurl.com/iheardyoulikefunctions
# For example, the built-in `sorted` function accepts a function named `key` which it will apply to
# every element of the list before sorting it. Let's say we have the following list of restaurant
# dictionaries; write code that alphabetizes that list by restaurant name and prints it out.
# Documentation here: https://docs.python.org/3/howto/sorting.html#key-functions

restaurants = [
  { "Name": "Brown Sugar Kitchen", "Distance": 8.2 },
  { "Name": "AlaMar Kitchen & Bar", "Distance": 5.0 },
  { "Name": "Kingston 11 Cuisine", "Distance": 1.3 },
  { "Name": "Zella's Soulful Kitchen", "Distance": 2.0 },
  { "Name": "Roux", "Distance": 4.7 },
  { "Name": "Chakula Eats", "Distance": 3.1 },
]

# YOUR CODE HERE

############################################ Exercise 3 ############################################
# Now, instead of sorting the list of restaurants alphabetically, sort them by distance and print
# out the resulting list.

# YOUR CODE HERE


# RUN CODE BY TYPING THIS IN THE CONSOLE: 

# python3 week6/black_owned_restaurants.py