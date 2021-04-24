# Example of API

# You want to ask for a donation for your pet rescue but don't have code to transfer money to your
# nonprofit. Use Paypal!

# donations start at $0
pet_rescue_donations = 0

# You create a way for people to donate


def donate(amount):
    paypal.transfermoney(amount, pet_rescue_donations)


# people now donate!

donate(10)
donate(100)
donate(25)

# You now have $135 in donations!


# RUN CODE BY TYPING THIS IN THE CONSOLE: 

# python3 week7/donation.py