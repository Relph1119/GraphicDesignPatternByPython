import copy

class Memento:
    def __init__(self, money):
        self.money = money
        self.fruits = list()

    def getMoney(self):
        return self.money

    def addFruit(self, fruit):
        self.fruits.append(fruit)

    def getFruits(self):
        return copy.deepcopy(self.fruits)