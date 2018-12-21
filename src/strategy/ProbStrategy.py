from Strategy import Strategy
import random
from Hand import Hand


class ProbStrategy(Strategy):
    def __init__(self, seed):
        random.seed(seed)

    prevHandValue = 0
    currentHandValue = 0
    history = [
        [1, 1, 1],
        [1, 1, 1],
        [1, 1, 1],
    ]

    def nextHand(self):
        bet = random.randint(0, self.getSum(self.currentHandValue))
        if bet < self.history[self.currentHandValue][0]:
            handvalue = 0
        elif bet < self.history[self.currentHandValue][0] + self.history[self.currentHandValue][1]:
            handvalue = 1
        else:
            handvalue = 2
        self.prevHandValue = self.currentHandValue
        self.currentHandValue = handvalue
        return Hand.get_hand(handvalue)

    def getSum(self, hv):
        sum = 0
        for i in range(3):
            sum += self.history[hv][i]
        return sum

    def study(self, win):
        if win:
            self.history[self.prevHandValue][self.currentHandValue] += 1
        else:
            self.history[self.prevHandValue][(self.currentHandValue + 1) % 3] += 1
            self.history[self.prevHandValue][(self.currentHandValue + 2) % 3] += 1
