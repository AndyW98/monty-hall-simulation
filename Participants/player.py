from random import randint

class Player:
    def __init__(self, name):
        self.name = name

    def choose(self):
        print(randint(0,10))