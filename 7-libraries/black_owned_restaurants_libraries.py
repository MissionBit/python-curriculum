# Black-Owned Restaurant Finder: Libraries exercises

############################################ Exercise 1 ############################################
# Use the csv.reader library to read in the CSV file of black-owned restaurants and store it in a
# list of dictionaries, similar to Exercise 2 of the "functions" exercises. Print the first ten
# restaurants in the list. The columns of the CSV file are as follows:
# Column 0: Name
# Column 1: Short form of the address
# Column 2: Full address, including the full county, state, and country names
# Column 3: Latitude
# Column 4: Longitude
# Column 5: Comma-separated list of cuisines that are provided (e.g. "Caribbean, African, Southern")
# Column 6: Comma-separated list of services that are provided (e.g. "Takeout, Delivery")
# Documentation here: https://docs.python.org/3/library/csv.html#csv.reader

# YOUR CODE HERE

############################################ Exercise 2 ############################################
# Write code that asks the user for their address, then use the geopy.geocoders library to retrieve
# the latitude and longitude of that address.
# Documentation here: https://geopy.readthedocs.io/en/stable/#module-geopy.geocoders

# YOUR CODE HERE

############################################ Exercise 3 ############################################
# With the user's address coordinates from Exercise 2 and the list of restaurant dictionaries from
# Exercise 1, use the geopy.distance.distance function to calculate the distance between the user's
# address and any restaurant of your choice. Then print the string "<RESTAURANT> is <DISTANCE> miles
# away from you"; for example, "Brown Sugar Kitchen is 8.2 miles away from you".
# Documentation here: https://geopy.readthedocs.io/en/stable/#module-geopy.distance

# YOUR CODE HERE

############################################ Exercise 4 ############################################
# In order to open directions on Google Maps, you can open the URL:
# https://www.google.com/maps/dir/<ADDRESS 1>/<ADDRESS 2>
# substituting <ADDRESS 1> and <ADDRESS 2> for the two addresses. In Python, you can also use
# `webbrowser.open(<URL>)` in order to open a URL from your script. Documentation here:
# https://docs.python.org/3/library/webbrowser.html
# With the user's address from Exercise 2 and the address of the restaurant from Exercise 3, open
# the directions using Google Maps.

# YOUR CODE HERE

############################################ Exercise 5 ############################################
# You should now know enough to build the full project :) Happy coding!


# RUN CODE BY TYPING THIS IN THE CONSOLE: 

# python3 week7/black_owned_restaurants.py
