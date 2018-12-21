from NumberGenerator import NumberGenerator
import random


class RandomNumberGenerator(NumberGenerator):
    def __init__(self):
        super().__init__()
        self.number = 0

    def getNumber(self):
        return self.number

    def execute(self):
        for i in range(20):
            self.number = random.randint(0, 50)
            self.notifyObservers()
