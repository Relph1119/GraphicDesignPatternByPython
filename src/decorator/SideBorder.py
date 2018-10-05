from Border import Border
from decorator.Display import Display

class SideBorder(Border, Display):
    def __init__(self, display, ch):
        super(SideBorder, self).__init__(display)
        self.borderChar = ch

    def getColumns(self):
        return 1 + self.display.getColumns() + 1

    def getRows(self):
        return self.display.getRows()

    def getRowText(self, row):
        return self.borderChar + self.display.getRowText(row) + self.borderChar
