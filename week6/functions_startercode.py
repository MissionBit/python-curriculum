#----------------------------------------------------------
# Challenge 1: Addition function
#----------------------------------------------------------

# Create a function called add_two that takes in two numbers "num1" and "num2" as parameters and returns the sum.

# Write your code here:



#Uncomment the print statements when done to test your function:

#print(add_two(3, 4))

#should print 7

#print(add_two(200, 1))

#should print 201




#----------------------------------------------------------
# Challenge 2: List sum
#----------------------------------------------------------

# Create a function called list_length that takes in a list called "lst" as a parameter and returns the sum of all of the numbers in the list.

# Write your code here:



#Uncomment the print statements when done to test your function:

#print(list_length([2,4,7,8,5]]))

#should print 26

#print(list_length([1,5,7,32,9]]))

#should print 54





#----------------------------------------------------------
# Challenge 3: Printing function
#----------------------------------------------------------

# Create a function called greeting that takes in someone's name as a string "name" as a parameter and returns a greeting to the person



# Write your code here:



#Uncomment the print statements when done to test your function:

#print(greeting("Alice"))

#should print "Hello Alice!" or similar

#print(greeting("Bob"))

#should print "Hello Bob!" or similar




#----------------------------------------------------------
# Challenge 4: Conditional function
#----------------------------------------------------------

# Create a function called driving_age that takes in an integer for age called "age". Return true if the age of the person is old enough to drive, and false if they are not


# Write your code here:



#Uncomment the print statements when done to test your function:

#print(driving_age(11))

#should print False

#print(driving_age(30))

#should print True




#----------------------------------------------------------
# Challenge 5: Compute distance
#----------------------------------------------------------

# Create a function called distance_formula that takes in two lists of coordinates called "place1" and "place2". Each list should have one integer for latitude and one integer for longitude. Using the distance formula, calculate the distance between place 1 and place 2 and return it.

#Note: The distance formula is 
#square root((latitude1-latitude2)^2 + (longitude1-longitude2)^2)


# Write your code here:



#Uncomment the print statements when done to test your function:

#print(distance_formula([35, 123], [74, 45]]))

#should print 87.2

#print(distance_formula([230, 6], [85, 90]]))

#should print 167.5




#----------------------------------------------------------
# Challenge 6: Scheduling calculator
#----------------------------------------------------------

# Create a function called scheduling_calculator that calculates how many hours you have to spend on a project a day to get it done. Your function should take in two integers - "hours" which represents the total number of hours your project is going to take, and "days" which represents the number of days you have to do it. Your function should return how many hours a day you should spend on the project by splitting the time up evenly for each day


# Write your code here:



#Uncomment the print statements when done to test your function:

#print(scheduling_calculator(7, 14))

#should print 0.5

#print(scheduling_calculator(20, 10))

#should print 2


#----------------------------------------------------------
# Challenge 7: Email template generator
#----------------------------------------------------------

# Create a function called email_creator that takes in a greeting name "recipient" and a signature "sender" that creates an email out of a pre-written template in your function using the recipient and sender's name.


# Write your code here:



#Uncomment the print statements when done to test your function:

#print(email_creator("Jack, "Anna"))

#should print something like:

#Hi Jack, 
#Let's schedule a meeting to catch up some time next week. Let me know when you are free!


#Best, Anna

#print(email_creator("Alison", "Luke"))

#should print something like:

#Hi Alison, 
#Let's schedule a meeting to catch up some time next week. Let me know when you are free!

#Best, Luke


#----------------------------------------------------------
# Challenge 8: Tip Calculator
#----------------------------------------------------------

# Create a function called tip_calculator that takes in a total cost parameter called "bill" and a tip percentage cost called "tip_percent". Your function should return the amount of tip you should pay. 


# Write your code here:



#Uncomment the print statements when done to test your function:

#print(tip_calculator(30, 20))

#should print 6

#print(scheduling_calculator(15, 15))

#should print 2.25



#----------------------------------------------------------
# Challenge 9: Book a flight
#----------------------------------------------------------

# Create a function called book_flight that takes in a string parameter "location" and a string parameter "day". Your function should look at the dictionary flight_scheduleprovided of days(key) to a list of places(value). If there is a flight to the location requested on the day requested, return the string "Booking a flight!" Else return: "Sorry, try another day"


# Write your code here:

flight_schedule = {"Monday" : ['New York', 'Los Angeles', 'San Francisco', 'London', 'Austin'], 
"Tuesday" : ['Hawaii', 'New York', 'Los Angeles', 'San Francisco', 'Seattle', 'London'], 
"Wednesday" : ['Hawaii', 'New York', 'Los Angeles', 'London', 'Austin'], 
"Thursday" : ['Hawaii', 'New York', 'Los Angeles', 'San Francisco', 'Seattle', 'London', 'Austin'], 
"Friday" : ['Hawaii', 'New York', 'Los Angeles', 'San Francisco', 'Seattle', 'Austin'], 
"Saturday": ['Hawaii', 'New York', 'Los Angeles', 'San Francisco', 'Seattle', 'London', 'Austin'], 
"Sunday" : ['Los Angeles', 'San Francisco', 'Seattle', 'London', ]}



#Uncomment the print statements when done to test your function:

#print(book_flight('New York', 'Saturday'))

#should print: "Booking a flight!"

#print(book_flight('Seattle', 'Wednesday'))

#should print "Sorry, try another day"

#----------------------------------------------------------
# Challenge 10: Grocery list
#----------------------------------------------------------

# Create a function called groceries that takes in an integer parameter "amount_to_spend" and returns a list of foods that cost less than or equal to that price that you can buy. Your function should initialize a dictionary of foods and prices and use it to determine which ones can be bought with the "amount_to_spend".


# Write your code here:



#Uncomment the print statements when done to test your function:

#print(groceries(30))

#example output:
#['Chicken', 'Cake', 'Cereal', 'Apple', 'Orange Juice']

#print(groceries(5))

#example output:
# ['Apple']



# RUN CODE BY TYPING THIS IN THE CONSOLE: 

# python3 week6/functions_startercode.py