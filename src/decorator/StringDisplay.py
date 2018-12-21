from decorator.Display import Display


class StringDisplay(Display):
    def __init__(self, string):
        self.string = string

    def getColumns(self):
        return len(self.string)

    def getRows(self):
        return 1

    def getRowText(self, row):
        return self.string if row == 0 else None
