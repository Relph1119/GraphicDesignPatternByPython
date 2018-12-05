from Strategy import Strategy
import random
from Hand import Hand

class WinningStrategy(Strategy):

    def __init__(self, seed):
        self.prevHand = Hand(0)
        random.seed(seed)

    won = False

    def nextHand(self):
        if not self.won:
            randomInt = random.randint(0, 2)
            self.prevHand = Hand.get_hand(randomInt)
        return self.prevHand

    def study(self, win):
        self.won = win



