from BigChar import BigChar
from BigCharFactory import BigCharFactory

class BigString():
    def __init__(self, string):
        self.bigchars = [ 0 for i in range(len(string))]
        factory = BigCharFactory()
        for i, str in enumerate(string):
            self.bigchars[i] = factory.getBigChar(str)

    def print(self):
        for i, bigchar in enumerate(self.bigchars):
            bigchar.print()