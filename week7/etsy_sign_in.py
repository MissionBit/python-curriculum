# Example of API

# You want creators to sign in to their etsy account, but you don't want to have to fill out all of
# the information
# Have them sign in through google!

etsy_name = ""
etsy_email = ""
etsy_picture = ""


def sign_in_to_etsy():
    profile = Google.signin
    # You can assign all of the google information to their etsy account now
    etsy_name = profile.getName()
    etsy_email = profile.getEmail()
    etsy_picture = profile.getPicture()


# Now sign in!
sign_in_to_etsy()

# RUN CODE BY TYPING THIS IN THE CONSOLE: 

# python3 week7/etsy_sign_in.py