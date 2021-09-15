# Black-Owned Restaurant Finder: Functions exercises

############################################ Exercise 1 ############################################
# Let's imagine that we want to calculate the distance between two points on a grid: the coordinates
# for your home (home_x, home_y) and the coordinates for a restaurant (restaurant_x, restaurant_y).
# Write a function that takes in these 4 arguments and returns the Euclidean distance between the
# two points using this formula:
#
#                     √(home_x - restaurant_x)^2 + (home_y - restaurant_y)^2

def calculate_distance(home_x, home_y, restaurant_x, restaurant_y):
  # REPLACE "pass" WITH YOUR CODE
  pass

print(calculate_distance(0, 0, 5, 5))

############################################ Exercise 2 ############################################
# Write a function that takes in 3 restaurant names and 3 distances, then prints out 3 lines in the
# following format (the actual distances may vary):
#
# 1. Brown Sugar Kitchen is 7.1 miles away
# 2. alaMar Kitchen & Bar is 10.6 miles away
# 3. Kingston 11 Cuisine is 3.6 miles away

def print_distances(restaurant1, distance1, restaurant2, distance2, restaurant3, distance3):
  # REPLACE "pass" WITH YOUR CODE
  pass

distance1 = calculate_distance(0, 0, 5, 5)
distance2 = calculate_distance(0, 0, 7, 8)
distance3 = calculate_distance(0, 0, 3, 2)
print_distances(
  'Brown Sugar Kitchen', distance1,
  'alaMar Kitchen & Bar', distance2,
  'Kingston 11 Cuisine', distance3)
