from DisplayImpl import DisplayImpl


class StringDisplayImpl(DisplayImpl):
    def __init__(self, string):
        self.string = string
        self.width = len(string)

    def rawOpen(self):
        self.printLine()

    def rawPrint(self):
        print("|{0}|".format(self.string))

    def rawClose(self):
        self.printLine()

    def printLine(self):
        print("+", end='')
        for i in range(self.width):
            print("-", end='')
        print("+")
