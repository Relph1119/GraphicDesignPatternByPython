from Memento import Memento
import random

class Gamer:
    def __init__(self, money):
        self.money = money
        self.fruits = list()
        self.fruitsname = ["🍎", "🍇", "🍌", "🍊"]

    def getMoney(self):
        return self.money

    def bet(self):
        dice = random.randint(1, 6)
        if dice == 1:
            self.money += 100
            print("所持金钱增加了。")
        elif dice == 2:
            self.money /= 2
            print("所持金钱减半了。")
        elif dice == 6:
            f = self.__getFruit()
            print("获得了水果({0})".format(f))
            self.fruits.append(f)
        else:
            print("什么都没有发生。")

    def createMemento(self):
        m = Memento(self.money)
        for i in range(len(self.fruits)):
            f = self.fruits[i]
            if f.startswith("好吃的"):
                m.addFruit(f)
        return m

    def restoreMomento(self, memento):
        self.money = memento.money
        self.fruits = memento.fruits

    def __str__(self):
        return "[money={0}, fruits={1}]".format(self.money, self.fruits)

    def __getFruit(self):
        prefix = ""
        if random.randint(1,2) == True:
            prefix = "好吃的"
        return prefix + self.fruitsname[random.randint(0, len(self.fruitsname)-1)]
