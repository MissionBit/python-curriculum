# Example of LISTS

# You want to hang out on Discord with your friends and decide to make an account.
# Each account comes with an empty list of friends and servers


class Discord_Account:
    friends_list = []
    server_list = []

    def add_friend(self, friend):
        self.friends_list.append(friend)

    def add_server(self, server):
        self.server_list.append(server)


# Run the code!

my_account = Discord_Account()

# You want to add friends so you add two friends to your empty friend list
my_account.add_friend("Friend1")
my_account.add_friend("Friend2")

# You want to add servers so you add two servers to your empty friend list
my_account.add_server("Gaming")
my_account.add_server("Social")

# Now your account has two friends and two servers!
print(my_account.friends_list)
print(my_account.server_list)


# RUN CODE BY TYPING THIS IN THE CONSOLE: 

# python3 week3/discord.py