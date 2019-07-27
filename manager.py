from random import randint
from door import Door

class Manager:
    def __init__(self, num_doors=3):
        self.num_doors = num_doors
        self.doors = []
        self.money_door = randint(0,2)
        for i in range(0, self.num_doors):
            if i == self.money_door:
                self.doors.append(Door(True))
            else:
                self.doors.append(Door())

    def list_doors(self):
        for i in range(0, len(self.doors)):
            print(self.doors[i].open())
    
    def no_money(self, choose):
        for i in range(0, len(self.doors)):
            if i != choose and not self.doors[i].open():
                return i