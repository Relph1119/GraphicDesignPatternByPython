from BigChar import BigChar
from BigCharFactory import BigCharFactory

class BigString():
    def __init__(self, string):
        self.bigchars = [ 0 for i in range(len(string))]
        factory = BigCharFactory()
        for i in range(len(string)):
            self.bigchars[i] = factory.getBigChar(string[i])

    def print(self):
        for i in range(len(self.bigchars)):
            self.bigchars[i].print()