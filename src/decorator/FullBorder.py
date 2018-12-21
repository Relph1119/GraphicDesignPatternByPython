from decorator.Display import Display
from decorator.Border import Border


class FullBorder(Border, Display):
    def getColumns(self):
        return 1 + self.display.getColumns() + 1

    def getRows(self):
        return 1 + self.display.getRows() + 1

    def getRowText(self, row):
        if row == 0:
            return "+{0}+".format(self.makeLine('-', self.display.getColumns()))
        elif row == self.display.getRows() + 1:
            return "+{0}+".format(self.makeLine('-', self.display.getColumns()))
        else:
            return "|{0}|".format(self.display.getRowText(row - 1))

    def makeLine(self, ch, count):
        buf = ""
        for i in range(count):
            buf += ch
        return buf
