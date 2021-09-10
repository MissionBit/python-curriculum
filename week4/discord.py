# Example of DICTIONARIES

# You want to continue to hang out with your friends on discord and want to know which friends are a part of which servers. Update your friends list to be a dictionary of server channel to friend to keep track of which friends are on which servers



class Discord_Account:
    friends_list = {}
    server_list = []

    def add_friend(self, server, friend):
        self.friends_list.add(server, friend)

    def add_server(self, server):
        self.server_list.append(server)


# Run the code!

my_account = Discord_Account()

# You want to add servers so you add two servers to your empty server list
my_account.add_server("Gaming")
my_account.add_server("Social")

# You want to add friends so you add two friends to your empty friend list. Add one to each server
my_account.add_friend("Gaming", "Friend1")
my_account.add_friend("Social", "Friend2")


# Now your account has two friends and two servers!
print(my_account.friends_list)
print(my_account.server_list)
