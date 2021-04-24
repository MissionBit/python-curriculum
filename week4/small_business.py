# Example of DICTIONARY

# You want to create a pricebook for your store so when people click on one of your products they
# can see a price!

# Create a pricebook
my_product_prices = {}

# Add the products and their prices to the pricebook
my_product_prices["t_shirt"] = "$20"
my_product_prices["sweatshirt"] = "$30"
my_product_prices["face_mask"] = "$5"

# Someone clicks on the t_shirt! Call the code to get and print the price
print("Price of t_shirt is: " + my_product_prices.get("t_shirt"))
# Someone clicks on the sweatshirt! Call the code to get and print the price
print("Price of sweatshirt is: " + my_product_prices.get("sweatshirt"))
# Someone clicks on the face_mask! Call the code to get and print the price
print("Price of face_mask is: " + my_product_prices.get("face_mask"))


# RUN CODE BY TYPING THIS IN THE CONSOLE: 

# python3 week4/small_business.py