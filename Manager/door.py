class Door():
    def __init__(self, money=False):
        self.money = money

    def open(self):
        return self.money