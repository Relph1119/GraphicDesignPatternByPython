from abc import ABCMeta, abstractstaticmethod

class Display(metaclass=ABCMeta):
    @abstractstaticmethod
    def getColumns(self):
        pass

    @abstractstaticmethod
    def getRows(self):
        pass

    @abstractstaticmethod
    def getRowText(self, row):
        pass

    def show(self):
        for i in range(int(self.getRows())):
            print(self.getRowText(i))