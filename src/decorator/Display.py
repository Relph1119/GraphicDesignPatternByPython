class Display(object):
    @classmethod
    def getColumns(cls):
        raise NotImplementedError

    @classmethod
    def getRows(cls):
        raise NotImplementedError

    @classmethod
    def getRowText(cls, row):
        raise NotImplementedError

    def show(self):
        for i in range(int(self.getRows())):
            print(self.getRowText(i))
