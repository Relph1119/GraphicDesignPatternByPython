class Player:
    wincount = 0
    losecount = 0
    gamecount = 0

    def __init__(self, name, strategy):
        self.name = name
        self.strategy = strategy

    def nextHand(self):
        return self.strategy.nextHand()

    def win(self):
        self.strategy.study(True)
        self.wincount += 1
        self.gamecount += 1

    def lose(self):
        self.strategy.study(False)
        self.losecount += 1
        self.gamecount += 1

    def even(self):
        self.gamecount += 1

    def __str__(self):
        return "[{0}:{1} games, {2} win, {3} lose]"\
            .format(self.name, self.gamecount, self.wincount, self.losecount)
