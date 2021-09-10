# Real Life Example of A NESTED FOR LOOP. No coding, just explain

# You are selling tickets for your band concert. You want a way to let people know what the first
# available seat is

# Set up the number or rows and number of seats per row
rows = 100
seats_in_row = 30

# Create a 2D array with the numbers you just created
seats = [["not_taken" for x in range(seats_in_row)] for y in range(rows)]

# When someone is looking for the first available seat, run this code to see what is sold already
# When you find an empty seat, mark that one as sold to the current person so it cannot be sold
# again
for row in range(0, rows):
    for seat in range(0, seats_in_row):
        if seats[row][seat] != "sold":
            seats[row][seat] = "sold"
