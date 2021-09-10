# Real Life Example of VARIABLES. No coding, just explain

# You have a pet rescue and you want people to know what each Dog is like!
# You create a way to assign playfulness, affection, and shedding level to each different dog
# so prospective parents can view their qualities!


class Dog:
    playfulness = 0
    affection = 0
    shedding = 0

    def __init__(self, playfulness, affection, shedding):
        self.playfulness = playfulness
        self.affection = affection
        self.shedding = shedding


golden_retriever = Dog(10, 10, 10)
pug = Dog(6, 9, 3)
poodle = Dog(4, 10, 1)
