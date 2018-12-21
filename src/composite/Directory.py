from Entry import Entry


class Directory(Entry):
    def __init__(self, name):
        self.name = name
        self.directory = list()

    def getName(self):
        return self.name

    def getSize(self):
        size = 0
        for i in range(len(self.directory)):
            size += self.directory[i].getSize()
        return size

    def add(self, entry):
        self.directory.append(entry)

    def printList(self, prefix=""):
        print("{0}/{1}".format(prefix, self))
        for i in range(len(self.directory)):
            entry = self.directory[i]
            entry.printList("{0}/{1}".format(prefix, self.name))
