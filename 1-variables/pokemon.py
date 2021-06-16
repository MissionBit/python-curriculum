# Example of VARIABLES


# You want to make a Pokemon game, and want people to have a way to choose which Pokemon they would
# prefer
# You create a way to assign attack, defense, speed and hp
class Pokemon:
    attack = 0
    defense = 0
    speed = 0
    hp = 0

    def __init__(self, attack, defense, speed, hp):
        self.attack = attack
        self.defense = defense
        self.speed = speed
        self.hp = hp


pikachu = Pokemon(55, 40, 90, 35)
bulbasaur = Pokemon(49, 49, 45, 45)
charmander = Pokemon(52, 43, 65, 39)

# RUN CODE BY TYPING THIS IN THE CONSOLE: 

# python3 week1/pokemon.py