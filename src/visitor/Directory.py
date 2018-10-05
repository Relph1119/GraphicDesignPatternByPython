from visitor.Entry import Entry

class Directory(Entry):
    def __init__(self, name):
        self.dir = list()
        self.name = name

    def getName(self):
        return self.name

    def getSize(self):
        size = 0;
        for i in range(len(self.dir)):
            size += self.dir[i].getSize()
        return size

    def add(self, entry):
        self.dir.append(entry)
        return self

    def accept(self, visitor):
        visitor.visit(self)