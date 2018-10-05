class Trouble:
    def __init__(self, number):
        self.number = number

    def getNumber(self):
        return self.number

    def __str__(self):
        return "[Trouble {0}]".format(self.number)