from Entry import Entry

class File(Entry):
    def __init__(self, name, size):
        self.name = name
        self.size = size

    def getName(self):
        return self.name

    def getSize(self):
        return self.size

    def printList(self, prefix=""):
        print("{0}/{1}".format(prefix, self))
